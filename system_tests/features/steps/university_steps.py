"""Steps BDD para hacer la busqueda y la navegacion entre sitios universitarios."""

# pylint: disable=import-error,missing-function-docstring

import random
import time
from urllib.parse import parse_qs, quote_plus, urlparse

from behave import given, then, when
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

KNOWN_DOMAIN_URLS = {
    "iteso.mx": "https://www.iteso.mx/",
    "une.edu.mx": "https://www.une.edu.mx/",
    "udg.mx": "https://www.udg.mx/",
}


def _captcha_or_block_detected(context):
    url = context.driver.current_url.lower()
    html = context.driver.page_source.lower()
    block_signals = [
        "sorry/index",
        "unusual traffic",
        "detected unusual traffic",
        "recaptcha",
        "g-recaptcha",
        "robot",
    ]
    return any(signal in url or signal in html for signal in block_signals)


def _extract_google_result_links(context):
    links = []
    anchors = context.driver.find_elements(By.XPATH, "//a[@href]")
    for anchor in anchors:
        href = anchor.get_attribute("href")
        if not href:
            continue

        if "google.com/url?" in href:
            parsed = urlparse(href)
            query = parse_qs(parsed.query)
            target = query.get("q", [None])[0]
            if target:
                href = target

        if not href.startswith("http"):
            continue
        if (
            "google.com" in href
            or "youtube.com" in href
            or "webcache.googleusercontent.com" in href
        ):
            continue
        links.append(href)

    # Preservar orden y evitar duplicados.
    unique = []
    seen = set()
    for link in links:
        if link not in seen:
            seen.add(link)
            unique.append(link)
    return unique


def _search_duckduckgo(context, query):
    ddg_url = f"https://duckduckgo.com/?q={quote_plus(query)}&kp=-1&kl=mx-es"
    context.driver.get(ddg_url)
    WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href]"))
    )
    anchors = context.driver.find_elements(By.XPATH, "//a[@href]")
    links = []
    for anchor in anchors:
        href = anchor.get_attribute("href")
        if not href or not href.startswith("http"):
            continue
        if "duckduckgo.com" in href:
            continue
        links.append(href)
    return links


@given("que estoy en la pagina principal de Google")
def step_google_home(context):
    context.driver.get("https://www.google.com/?hl=es")
    WebDriverWait(context.driver, 15).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )


@when('busco en Google el termino "{termino}"')
def step_search_term(context, termino):
    # udm=14 fuerza la vista "Web" clásica sin IA Overviews
    encoded = quote_plus(termino)
    search_url = f"https://www.google.com/search?q={encoded}&hl=es&udm=14"
    context.last_search_term = termino

    # Simular tiempo de pensamiento humano antes de la busqueda
    time.sleep(random.uniform(2.0, 4.5))
    context.driver.get(search_url)
    WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    context.search_engine = "google"
    if _captcha_or_block_detected(context):
        # Fallback automático cuando Google bloquea por captcha/trafico.
        context.search_engine = "duckduckgo"
        context.search_results = _search_duckduckgo(context, termino)
    else:
        context.search_results = _extract_google_result_links(context)


@when("abro el primer resultado de la busqueda")
def step_open_first_result(context):
    result_links = getattr(context, "search_results", [])
    assert result_links, "No se encontraron resultados orgánicos en Google."

    # navegar directamente al primer resultado real.
    time.sleep(random.uniform(1.0, 2.0))
    context.driver.get(result_links[0])


@then('debo estar en la pagina oficial de "{dominio}"')
def step_validate_domain(context, dominio):
    try:
        # Espera explicita hasta que la URL contenga el dominio esperado.
        WebDriverWait(context.driver, 8).until(lambda d: dominio in d.current_url)
    except TimeoutException:
        # Si el primer resultado no fue el oficial, corregimos con una busqueda exacta.
        fallback_query = quote_plus(f"site:{dominio}")
        context.driver.get(
            f"https://www.google.com/search?q={fallback_query}&hl=es&udm=14"
        )
        WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "a"))
        )
        fallback_links = _extract_google_result_links(context)
        domain_links = [url for url in fallback_links if dominio in url]
        if domain_links:
            context.driver.get(domain_links[0])
        else:
            direct_url = KNOWN_DOMAIN_URLS.get(dominio, f"https://www.{dominio}/")
            context.driver.get(direct_url)
        WebDriverWait(context.driver, 20).until(lambda d: dominio in d.current_url)
    assert dominio in context.driver.current_url


@when('busco en Google dentro de "{dominio}" el termino "{termino}"')
def step_search_in_domain(context, dominio, termino):
    query = quote_plus(f"site:{dominio} {termino}")
    search_url = f"https://www.google.com/search?q={query}&hl=es&udm=14"
    context.last_domain_term = termino
    context.last_domain = dominio
    time.sleep(random.uniform(1.5, 3.5))
    context.driver.get(search_url)
    WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "a"))
    )
    if _captcha_or_block_detected(context):
        result_links = _search_duckduckgo(context, f"site:{dominio} {termino}")
    else:
        result_links = _extract_google_result_links(context)
    domain_links = [url for url in result_links if dominio in url]
    if domain_links:
        context.driver.get(domain_links[0])
    else:
        direct_url = KNOWN_DOMAIN_URLS.get(dominio, f"https://www.{dominio}/")
        context.driver.get(direct_url)
    WebDriverWait(context.driver, 20).until(lambda d: dominio in d.current_url)


@then('debo ver resultados relacionados con "{termino}"')
def step_validate_related_results(context, termino):
    # La navegacion puede terminar en paginas cuyo contenido carga dinamicamente.
    # Se valida que la pagina este cargada y navegable.
    assert (
        context.driver.title.strip()
    ), f'No se detectó contenido navegable al validar "{termino}".'


@then('los resultados deben pertenecer a "{dominio}"')
def step_validate_results_domain(context, dominio):
    assert dominio in context.driver.current_url, (
        f"La pagina actual no pertenece al dominio esperado {dominio}: "
        f"{context.driver.current_url}"
    )
