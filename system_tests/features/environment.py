"""BDD hooks config for Selenium tests."""

# pylint: disable=import-error,missing-function-docstring,broad-exception-caught,unused-argument

import undetected_chromedriver as uc
from selenium_stealth import stealth


def _build_options():
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--lang=es-MX")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")
    return options


def before_all(context):
    # Se fija la version mayor actual de Chrome local para evitar incompatibilidades
    # en la resolución automatica de undetected_chromedriver.
    context.driver = uc.Chrome(version_main=147, options=_build_options())

    stealth(
        context.driver,
        languages=["es-MX", "es"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )


def after_scenario(context, scenario):
    try:
        context.driver.delete_all_cookies()
    except Exception:
        pass
    try:
        context.driver.execute_script("window.localStorage.clear();")
    except Exception:
        pass


def after_all(context):
    if hasattr(context, "driver"):
        driver = context.driver
        try:
            driver.quit()
        except OSError:
            pass
        finally:
            # undetected_chromedriver vuelve a invocar quit() en __del__.
            # Se neutraliza para evitar ruido de WinError 6 al final.
            driver.quit = lambda: None
