import unittest
import class_exercises as wb  # importamos las funciones del archivo original (WhiteBox - wb)

class TestWhiteBoxExercises(unittest.TestCase):
    """
    Clase que contiene todas las pruebas unitarias para los ejercicios 1 al 21.
    """
    
    # ------ Ejercicio 1 ------
    # Verificar que la funcion clasifica correctamente numeros positivos, negativos y cero
    
    def test_check_number_status_positive(self):
        """Verificar que retorna 'Positive' cuando el numero es mayor a cero"""
        self.assertEqual(wb.check_number_status(5), "Positive")
    
    def test_check_number_status_negative(self):
        """Verificar que retorna 'Negative' cuando el numero es menor a cero"""
        self.assertEqual(wb.check_number_status(-3), "Negative")
    
    def test_check_number_status_zero(self):
        """Verificar que retorna 'Zero' cuando el numero es igual a cero"""
        self.assertEqual(wb.check_number_status(0), "Zero")
    
    # ------ Ejercicio 2 ------
    # Verificar que la funcion valida contraseñas segun:
    # longitud minima 8, mayuscula, minuscula, numero y caracter especial
    
    def test_validate_password_valid(self):
        """Verificar que acepta una contraseña que cumple todos los requisitos"""
        self.assertTrue(wb.validate_password("Pass123!@#"))
    
    def test_validate_password_too_short(self):
        """Verificar que rechaza contraseña con menos de 8 caracteres"""
        self.assertFalse(wb.validate_password("Pa1!"))
    
    def test_validate_password_no_uppercase(self):
        """Verificar que rechaza contraseña sin letras mayusculas"""
        self.assertFalse(wb.validate_password("password123!"))
    
    def test_validate_password_no_lowercase(self):
        """Verificar que rechaza contraseña sin letras minusculas"""
        self.assertFalse(wb.validate_password("PASSWORD123!"))
    
    def test_validate_password_no_digit(self):
        """Verificar que rechaza contraseña sin numeros"""
        self.assertFalse(wb.validate_password("Password!!!"))
    
    def test_validate_password_no_special(self):
        """Verificar que rechaza contraseña sin caracteres especiales"""
        self.assertFalse(wb.validate_password("Password123"))
    
    # ------ Ejercicio 3 ------
    # Verificar que la funcion aplica el descuento correcto segun el monto:
    # menor 100 = 0%, 100-500 = 10%, mayor 500 = 20%
    
    def test_calculate_total_discount_less_100(self):
        """Verificar que montos menores a 100 no tienen descuento"""
        self.assertEqual(wb.calculate_total_discount(50), 0)
    
    def test_calculate_total_discount_100_to_500(self):
        """Verificar que montos entre 100 y 500 reciben 10% de descuento"""
        self.assertEqual(wb.calculate_total_discount(200), 20)
        self.assertEqual(wb.calculate_total_discount(100), 10)
        self.assertEqual(wb.calculate_total_discount(500), 50)
    
    def test_calculate_total_discount_more_500(self):
        """Verificar que montos mayores a 500 reciben 20% de descuento"""
        self.assertEqual(wb.calculate_total_discount(600), 120)
    
    # ------ Ejercicio 4 ------
    # Verificar que la funcion calcula el total aplicando descuentos por cantidad:
    # 1-5 = sin descuento, 6-10 = 5%, mas de 10 = 10%
    
    def test_calculate_order_total_quantity_1_to_5(self):
        """Verificar calculo sin descuento para cantidades entre 1 y 5 unidades"""
        items = [{"quantity": 3, "price": 10}]
        self.assertEqual(wb.calculate_order_total(items), 30)
    
    def test_calculate_order_total_quantity_6_to_10(self):
        """Verificar calculo con 5% descuento para cantidades entre 6 y 10 unidades"""
        items = [{"quantity": 8, "price": 10}]
        self.assertEqual(wb.calculate_order_total(items), 76)
    
    def test_calculate_order_total_quantity_more_10(self):
        """Verificar calculo con 10% descuento para cantidades mayores a 10 unidades"""
        items = [{"quantity": 12, "price": 10}]
        self.assertEqual(wb.calculate_order_total(items), 108)
    
    def test_calculate_order_total_multiple_items(self):
        """Verificar calculo correcto con multiples items de diferentes cantidades"""
        items = [
            {"quantity": 3, "price": 10},
            {"quantity": 8, "price": 10},
            {"quantity": 12, "price": 10}
        ]
        self.assertEqual(wb.calculate_order_total(items), 30 + 76 + 108)
    
    # ------ Ejercicio 5 ------
    # Verificar que la funcion calcula el costo de envio segun peso y metodo:
    # standard: <=5=$10, 5-10=$15, >10=$20
    # express: <=5=$20, 5-10=$30, >10=$40
    
    def test_shipping_standard_weight_leq_5(self):
        """Verificar envio standard con peso total hasta 5kg cuesta $10"""
        items = [{"weight": 2}, {"weight": 3}]
        self.assertEqual(wb.calculate_items_shipping_cost(items, "standard"), 10)
    
    def test_shipping_standard_weight_5_to_10(self):
        """Verificar envio standard con peso entre 5 y 10kg cuesta $15"""
        items = [{"weight": 6}, {"weight": 4}]
        self.assertEqual(wb.calculate_items_shipping_cost(items, "standard"), 15)
    
    def test_shipping_standard_weight_gt_10(self):
        """Verificar envio standard con peso mayor a 10kg cuesta $20"""
        items = [{"weight": 8}, {"weight": 5}]
        self.assertEqual(wb.calculate_items_shipping_cost(items, "standard"), 20)
    
    def test_shipping_express_weight_leq_5(self):
        """Verificar envio express con peso hasta 5kg cuesta $20"""
        items = [{"weight": 2}, {"weight": 3}]
        self.assertEqual(wb.calculate_items_shipping_cost(items, "express"), 20)
    
    def test_shipping_express_weight_5_to_10(self):
        """Verificar envio express con peso entre 5 y 10kg cuesta $30"""
        items = [{"weight": 6}, {"weight": 4}]
        self.assertEqual(wb.calculate_items_shipping_cost(items, "express"), 30)
    
    def test_shipping_express_weight_gt_10(self):
        """Verificar envio express con peso mayor a 10kg cuesta $40"""
        items = [{"weight": 8}, {"weight": 5}]
        self.assertEqual(wb.calculate_items_shipping_cost(items, "express"), 40)
    
    def test_shipping_invalid_method(self):
        """Verificar que lanza error cuando se usa un metodo de envio invalido"""
        items = [{"weight": 5}]
        with self.assertRaises(ValueError):
            wb.calculate_items_shipping_cost(items, "invalid")
    
    # ------ Ejercicio 6 ------
    # Verificar que la funcion valida login segun longitud:
    # username 5-20 caracteres, password 8-15 caracteres
    
    def test_validate_login_successful(self):
        """Verificar login exitoso cuando ambos campos cumplen la longitud requerida"""
        self.assertEqual(wb.validate_login("username123", "password12"), "Login Successful")
    
    def test_validate_login_username_short(self):
        """Verificar login fallido cuando username tiene menos de 5 caracteres"""
        self.assertEqual(wb.validate_login("user", "password12"), "Login Failed")
    
    def test_validate_login_username_long(self):
        """Verificar login fallido cuando username tiene mas de 20 caracteres"""
        self.assertEqual(wb.validate_login("u" * 21, "password12"), "Login Failed")
    
    def test_validate_login_password_short(self):
        """Verificar login fallido cuando password tiene menos de 8 caracteres"""
        self.assertEqual(wb.validate_login("username123", "pass"), "Login Failed")
    
    def test_validate_login_password_long(self):
        """Verificar login fallido cuando password tiene mas de 15 caracteres"""
        self.assertEqual(wb.validate_login("username123", "p" * 16), "Login Failed")
    
    # ------ Ejercicio 7 ------
    # Verificar que la funcion determina elegibilidad segun edad (18 a 65 años)
    
    def test_verify_age_eligible_lower_bound(self):
        """Verificar que edad de 18 años es elegible"""
        self.assertEqual(wb.verify_age(18), "Eligible")
    
    def test_verify_age_eligible_upper_bound(self):
        """Verificar que edad de 65 años es elegible"""
        self.assertEqual(wb.verify_age(65), "Eligible")
    
    def test_verify_age_eligible_middle(self):
        """Verificar que edad dentro del rango (30 años) es elegible"""
        self.assertEqual(wb.verify_age(30), "Eligible")
    
    def test_verify_age_not_eligible_below(self):
        """Verificar que edad menor a 18 años no es elegible"""
        self.assertEqual(wb.verify_age(17), "Not Eligible")
    
    def test_verify_age_not_eligible_above(self):
        """Verificar que edad mayor a 65 años no es elegible"""
        self.assertEqual(wb.verify_age(66), "Not Eligible")
    
    # ------ Ejercicio 8 ------
    # Verificar que la funcion categoriza productos segun precio:
    # 10-50 = A, 51-100 = B, 101-200 = C, otros = D
    
    def test_categorize_product_category_a(self):
        """Verificar que precios entre 10 y 50 pertenecen a categoria A"""
        self.assertEqual(wb.categorize_product(10), "Category A")
        self.assertEqual(wb.categorize_product(30), "Category A")
        self.assertEqual(wb.categorize_product(50), "Category A")
    
    def test_categorize_product_category_b(self):
        """Verificar que precios entre 51 y 100 pertenecen a categoria B"""
        self.assertEqual(wb.categorize_product(51), "Category B")
        self.assertEqual(wb.categorize_product(75), "Category B")
        self.assertEqual(wb.categorize_product(100), "Category B")
    
    def test_categorize_product_category_c(self):
        """Verificar que precios entre 101 y 200 pertenecen a categoria C"""
        self.assertEqual(wb.categorize_product(101), "Category C")
        self.assertEqual(wb.categorize_product(150), "Category C")
        self.assertEqual(wb.categorize_product(200), "Category C")
    
    def test_categorize_product_category_d_below(self):
        """Verificar que precios menores a 10 pertenecen a categoria D"""
        self.assertEqual(wb.categorize_product(5), "Category D")
    
    def test_categorize_product_category_d_above(self):
        """Verificar que precios mayores a 200 pertenecen a categoria D"""
        self.assertEqual(wb.categorize_product(250), "Category D")
    
    # ------ Ejercicio 9 ------
    # Verificar que la funcion valida emails: longitud 5-50, debe contener @ y .
    
    def test_validate_email_valid(self):
        """Verificar que acepta un email con formato valido"""
        self.assertEqual(wb.validate_email("test@example.com"), "Valid Email")
    
    def test_validate_email_too_short(self):
        """Verificar que rechaza email con menos de 5 caracteres"""
        # Usamos emails con 4 caracteres o menos
        self.assertEqual(wb.validate_email("a@b."), "Invalid Email")   # 4 caracteres
        self.assertEqual(wb.validate_email("@.c"), "Invalid Email")    # 3 caracteres
        self.assertEqual(wb.validate_email("a@c"), "Invalid Email")    # 3 caracteres (sin punto)
    
    def test_validate_email_too_long(self):
        """Verificar que rechaza email con mas de 50 caracteres"""
        # Creamos un email con mas de 50 caracteres
        local_part = "a" * 40  # 40 caracteres
        domain = "example.com"  # 11 caracteres
        email = local_part + "@" + domain  # Total: 40 + 1 + 11 = 52 caracteres
        self.assertEqual(wb.validate_email(email), "Invalid Email")
    
    def test_validate_email_no_at(self):
        """Verificar que rechaza email sin el simbolo @"""
        self.assertEqual(wb.validate_email("testexample.com"), "Invalid Email")
    
    def test_validate_email_no_dot(self):
        """Verificar que rechaza email sin punto"""
        self.assertEqual(wb.validate_email("test@examplecom"), "Invalid Email")
    
    # ------ Ejercicio 10 ------
    # Verificar conversion de Celsius a Fahrenheit en rango -100 a 100
    
    def test_celsius_to_fahrenheit_valid_lower(self):
        """Verificar conversion correcta en el limite inferior (-100°C)"""
        self.assertEqual(wb.celsius_to_fahrenheit(-100), (-100 * 9/5) + 32)
    
    def test_celsius_to_fahrenheit_valid_upper(self):
        """Verificar conversion correcta en el limite superior (100°C)"""
        self.assertEqual(wb.celsius_to_fahrenheit(100), (100 * 9/5) + 32)
    
    def test_celsius_to_fahrenheit_valid_middle(self):
        """Verificar conversion correcta de 0°C a 32°F"""
        self.assertEqual(wb.celsius_to_fahrenheit(0), 32)
    
    def test_celsius_to_fahrenheit_invalid_below(self):
        """Verificar que rechaza temperaturas bajo -100°C"""
        self.assertEqual(wb.celsius_to_fahrenheit(-101), "Invalid Temperature")
    
    def test_celsius_to_fahrenheit_invalid_above(self):
        """Verificar que rechaza temperaturas sobre 100°C"""
        self.assertEqual(wb.celsius_to_fahrenheit(101), "Invalid Temperature")
    
    # ------ Ejercicio 11 ------
    # Verificar validacion de tarjetas: 13-16 digitos, solo numeros
    
    def test_validate_credit_card_valid_min(self):
        """Verificar que acepta tarjeta con 13 digitos"""
        self.assertEqual(wb.validate_credit_card("1" * 13), "Valid Card")
    
    def test_validate_credit_card_valid_max(self):
        """Verificar que acepta tarjeta con 16 digitos"""
        self.assertEqual(wb.validate_credit_card("1" * 16), "Valid Card")
    
    def test_validate_credit_card_invalid_short(self):
        """Verificar que rechaza tarjeta con menos de 13 digitos"""
        self.assertEqual(wb.validate_credit_card("1" * 12), "Invalid Card")
    
    def test_validate_credit_card_invalid_long(self):
        """Verificar que rechaza tarjeta con mas de 16 digitos"""
        self.assertEqual(wb.validate_credit_card("1" * 17), "Invalid Card")
    
    def test_validate_credit_card_invalid_characters(self):
        """Verificar que rechaza tarjeta con caracteres no numericos"""
        self.assertEqual(wb.validate_credit_card("1234-5678-9012"), "Invalid Card")
    
    # ------ Ejercicio 12 ------
    # Verificar validacion de fechas: año 1900-2100, mes 1-12, dia 1-31
    
    def test_validate_date_valid(self):
        """Verificar que acepta una fecha valida"""
        self.assertEqual(wb.validate_date(2000, 6, 15), "Valid Date")
    
    def test_validate_date_year_lower_bound(self):
        """Verificar que acepta año 1900"""
        self.assertEqual(wb.validate_date(1900, 1, 1), "Valid Date")
    
    def test_validate_date_year_upper_bound(self):
        """Verificar que acepta año 2100"""
        self.assertEqual(wb.validate_date(2100, 12, 31), "Valid Date")
    
    def test_validate_date_year_invalid_below(self):
        """Verificar que rechaza año menor a 1900"""
        self.assertEqual(wb.validate_date(1899, 6, 15), "Invalid Date")
    
    def test_validate_date_year_invalid_above(self):
        """Verificar que rechaza año mayor a 2100"""
        self.assertEqual(wb.validate_date(2101, 6, 15), "Invalid Date")
    
    def test_validate_date_month_invalid_below(self):
        """Verificar que rechaza mes menor a 1"""
        self.assertEqual(wb.validate_date(2000, 0, 15), "Invalid Date")
    
    def test_validate_date_month_invalid_above(self):
        """Verificar que rechaza mes mayor a 12"""
        self.assertEqual(wb.validate_date(2000, 13, 15), "Invalid Date")
    
    def test_validate_date_day_invalid_below(self):
        """Verificar que rechaza dia menor a 1"""
        self.assertEqual(wb.validate_date(2000, 6, 0), "Invalid Date")
    
    def test_validate_date_day_invalid_above(self):
        """Verificar que rechaza dia mayor a 31"""
        self.assertEqual(wb.validate_date(2000, 6, 32), "Invalid Date")
    
    # ------ Ejercicio 13 ------
    # Verificar elegibilidad para vuelos: edad 18-65 O viajero frecuente
    
    def test_check_flight_eligibility_age_eligible_only(self):
        """Verificar elegible por edad aunque no sea viajero frecuente"""
        self.assertEqual(wb.check_flight_eligibility(30, False), "Eligible to Book")
    
    def test_check_flight_eligibility_frequent_flyer_only(self):
        """Verificar elegible por viajero frecuente aunque edad no este en rango"""
        self.assertEqual(wb.check_flight_eligibility(17, True), "Eligible to Book")
    
    def test_check_flight_eligibility_both_conditions(self):
        """Verificar elegible cuando cumple ambas condiciones"""
        self.assertEqual(wb.check_flight_eligibility(30, True), "Eligible to Book")
    
    def test_check_flight_eligibility_neither_condition(self):
        """Verificar no elegible cuando no cumple ninguna condicion"""
        self.assertEqual(wb.check_flight_eligibility(17, False), "Not Eligible to Book")
    
    # ------ Ejercicio 14 ------
    # Verificar validacion de URL: maximo 255 caracteres, debe empezar con http:// o https://
    
    def test_validate_url_valid_http(self):
        """Verificar que acepta URL que comienza con http://"""
        self.assertEqual(wb.validate_url("http://example.com"), "Valid URL")
    
    def test_validate_url_valid_https(self):
        """Verificar que acepta URL que comienza con https://"""
        self.assertEqual(wb.validate_url("https://example.com"), "Valid URL")
    
    def test_validate_url_invalid_protocol(self):
        """Verificar que rechaza URL con protocolo diferente"""
        self.assertEqual(wb.validate_url("ftp://example.com"), "Invalid URL")
    
    def test_validate_url_too_long(self):
        """Verificar que rechaza URL con mas de 255 caracteres"""
        url = "http://" + "a" * 250 + ".com"
        self.assertEqual(wb.validate_url(url), "Invalid URL")
    
    # ------ Ejercicio 15 ------
    # Verificar descuentos por cantidad: 1-5 = sin, 6-10 = 5%, mas de 10 = 10%
    
    def test_calculate_quantity_discount_no_discount(self):
        """Verificar que cantidades de 1 a 5 no tienen descuento"""
        self.assertEqual(wb.calculate_quantity_discount(1), "No Discount")
        self.assertEqual(wb.calculate_quantity_discount(3), "No Discount")
        self.assertEqual(wb.calculate_quantity_discount(5), "No Discount")
    
    def test_calculate_quantity_discount_5_percent(self):
        """Verificar que cantidades de 6 a 10 tienen 5% descuento"""
        self.assertEqual(wb.calculate_quantity_discount(6), "5% Discount")
        self.assertEqual(wb.calculate_quantity_discount(8), "5% Discount")
        self.assertEqual(wb.calculate_quantity_discount(10), "5% Discount")
    
    def test_calculate_quantity_discount_10_percent(self):
        """Verificar que cantidades mayores a 10 tienen 10% descuento"""
        self.assertEqual(wb.calculate_quantity_discount(11), "10% Discount")
        self.assertEqual(wb.calculate_quantity_discount(20), "10% Discount")
    
    # ------ Ejercicio 16 ------
    # Verificar tamaño valido de archivo: 0 a 1,048,576 bytes
    
    def test_check_file_size_valid_min(self):
        """Verificar que acepta tamaño minimo de 0 bytes"""
        self.assertEqual(wb.check_file_size(0), "Valid File Size")
    
    def test_check_file_size_valid_middle(self):
        """Verificar que acepta tamaño intermedio valido"""
        self.assertEqual(wb.check_file_size(500000), "Valid File Size")
    
    def test_check_file_size_valid_max(self):
        """Verificar que acepta tamaño maximo de 1MB"""
        self.assertEqual(wb.check_file_size(1048576), "Valid File Size")
    
    def test_check_file_size_invalid_negative(self):
        """Verificar que rechaza tamaño negativo"""
        self.assertEqual(wb.check_file_size(-1), "Invalid File Size")
    
    def test_check_file_size_invalid_above(self):
        """Verificar que rechaza tamaño mayor a 1MB"""
        self.assertEqual(wb.check_file_size(1048577), "Invalid File Size")
    
    # ------ Ejercicio 17 ------
    # Verificar elegibilidad para prestamos segun ingreso y puntaje crediticio
    
    def test_check_loan_eligibility_income_below_30k(self):
        """Verificar que ingresos bajo 30,000 no son elegibles"""
        self.assertEqual(wb.check_loan_eligibility(25000, 800), "Not Eligible")
    
    def test_check_loan_eligibility_standard_loan(self):
        """Verificar prestamo standard: ingreso 30k-60k con buen credito"""
        self.assertEqual(wb.check_loan_eligibility(50000, 750), "Standard Loan")
    
    def test_check_loan_eligibility_secured_loan(self):
        """Verificar prestamo asegurado: ingreso 30k-60k con credito regular o bajo"""
        self.assertEqual(wb.check_loan_eligibility(50000, 700), "Secured Loan")
        self.assertEqual(wb.check_loan_eligibility(50000, 650), "Secured Loan")
    
    def test_check_loan_eligibility_premium_loan(self):
        """Verificar prestamo premium: ingreso alto con excelente credito"""
        self.assertEqual(wb.check_loan_eligibility(70000, 800), "Premium Loan")
    
    def test_check_loan_eligibility_high_income_standard(self):
        """Verificar prestamo standard: ingreso alto con credito no excelente"""
        self.assertEqual(wb.check_loan_eligibility(70000, 750), "Standard Loan")
    
    # ------ Ejercicio 18 ------
    # Verificar costo de envio segun peso y dimensiones
    
    def test_shipping_cost_small_package(self):
        """Verificar costo $5 para paquete pequeño (peso<=1 y dimensiones<=10)"""
        self.assertEqual(wb.calculate_shipping_cost(1, 10, 10, 10), 5)
    
    def test_shipping_cost_medium_package(self):
        """Verificar costo $10 para paquete mediano (peso 1-5 y dimensiones 11-30)"""
        self.assertEqual(wb.calculate_shipping_cost(3, 20, 20, 20), 10)
    
    def test_shipping_cost_large_package(self):
        """Verificar costo $20 para paquete grande (no cumple condiciones anteriores)"""
        self.assertEqual(wb.calculate_shipping_cost(6, 40, 40, 40), 20)
    
    def test_shipping_cost_weight_small_dimensions_large(self):
        """Verificar costo $20 cuando peso es pequeño pero dimensiones grandes"""
        self.assertEqual(wb.calculate_shipping_cost(1, 20, 20, 20), 20)
    
    def test_shipping_cost_weight_large_dimensions_small(self):
        """Verificar costo $20 cuando peso es grande pero dimensiones pequeñas"""
        self.assertEqual(wb.calculate_shipping_cost(6, 5, 5, 5), 20)
    
    # ------ Ejercicio 19 ------
    # Verificar calificacion de quiz segun respuestas correctas e incorrectas
    
    def test_grade_quiz_pass(self):
        """Verificar 'Pass' cuando hay al menos 7 correctas y maximo 2 incorrectas"""
        self.assertEqual(wb.grade_quiz(7, 2), "Pass")
        self.assertEqual(wb.grade_quiz(10, 0), "Pass")
    
    def test_grade_quiz_conditional_pass(self):
        """Verificar 'Conditional Pass' cuando hay 5-6 correctas y maximo 3 incorrectas"""
        self.assertEqual(wb.grade_quiz(5, 3), "Conditional Pass")
        self.assertEqual(wb.grade_quiz(6, 2), "Conditional Pass")
    
    def test_grade_quiz_fail_low_correct(self):
        """Verificar 'Fail' cuando hay menos de 5 correctas"""
        self.assertEqual(wb.grade_quiz(4, 2), "Fail")
    
    def test_grade_quiz_fail_high_incorrect(self):
        """Verificar 'Fail' cuando hay mas de 3 incorrectas aunque tenga buenas correctas"""
        self.assertEqual(wb.grade_quiz(7, 4), "Fail")
    
    # ------ Ejercicio 20 ------
    # Verificar autenticacion de usuarios: admin, user regular o invalido
    
    def test_authenticate_user_admin(self):
        """Verificar que credenciales de administrador son aceptadas"""
        self.assertEqual(wb.authenticate_user("admin", "admin123"), "Admin")
    
    def test_authenticate_user_regular_user(self):
        """Verificar que usuario regular con credenciales validas es aceptado"""
        self.assertEqual(wb.authenticate_user("username", "password12"), "User")
    
    def test_authenticate_user_invalid_short_username(self):
        """Verificar que username muy corto resulta en 'Invalid'"""
        self.assertEqual(wb.authenticate_user("user", "password12"), "Invalid")
    
    def test_authenticate_user_invalid_short_password(self):
        """Verificar que password muy corto resulta en 'Invalid'"""
        self.assertEqual(wb.authenticate_user("username", "pass"), "Invalid")
    
    def test_authenticate_user_invalid_both(self):
        """Verificar que ambos campos incorrectos resultan en 'Invalid'"""
        self.assertEqual(wb.authenticate_user("user", "pass"), "Invalid")
    
    # ------ Ejercicio 21 ------
    # Verificar recomendaciones climaticas segun temperatura y humedad
    
    def test_weather_advisory_high_temp_high_humidity(self):
        """Verificar advertencia de hidratacion cuando hace calor y hay humedad"""
        self.assertEqual(
            wb.get_weather_advisory(35, 80),
            "High Temperature and Humidity. Stay Hydrated."
        )
    
    def test_weather_advisory_low_temp(self):
        """Verificar advertencia de abrigarse cuando la temperatura es baja"""
        self.assertEqual(
            wb.get_weather_advisory(-5, 50),
            "Low Temperature. Bundle Up!"
        )
    
    def test_weather_advisory_no_specific(self):
        """Verificar que no hay advertencia especifica en condiciones normales"""
        self.assertEqual(
            wb.get_weather_advisory(20, 50),
            "No Specific Advisory"
        )

# ------ Ejercicio 22 ------
# verificamos el funcionamiento de la maquina expendedora con estados "Ready" y "Dispensing"

class TestVendingMachine(unittest.TestCase):
    """Pruebas unitarias para el ejercicio 22 - Vending Machine"""

    def setUp(self):
        """Configurar una maquina expendedora nueva antes de cada prueba"""
        self.vm = wb.VendingMachine()

    def test_initial_state_ready(self):
        """Verificar que el estado inicial es 'Ready'"""
        self.assertEqual(self.vm.state, "Ready")

    def test_insert_coin_when_ready(self):
        """Verificar que insertar moneda en estado Ready cambia a Dispensing"""
        result = self.vm.insert_coin()
        self.assertEqual(result, "Coin Inserted. Select your drink.")
        self.assertEqual(self.vm.state, "Dispensing")

    def test_insert_coin_when_dispensing(self):
        """Verificar que insertar moneda en estado Dispensing es invalido"""
        self.vm.insert_coin()  # Cambiar a Dispensing
        result = self.vm.insert_coin()
        self.assertEqual(result, "Invalid operation in current state.")
        self.assertEqual(self.vm.state, "Dispensing")  # Estado no cambia

    def test_select_drink_when_dispensing(self):
        """Verificar que seleccionar bebida en estado Dispensing cambia a Ready"""
        self.vm.insert_coin()  # Cambiar a Dispensing
        result = self.vm.select_drink()
        self.assertEqual(result, "Drink Dispensed. Thank you!")
        self.assertEqual(self.vm.state, "Ready")

    def test_select_drink_when_ready(self):
        """Verificar que seleccionar bebida en estado Ready es invalido"""
        result = self.vm.select_drink()
        self.assertEqual(result, "Invalid operation in current state.")
        self.assertEqual(self.vm.state, "Ready")  # Estado no cambia

    def test_full_cycle(self):
        """Verificar el ciclo completo de operacion: insertar moneda y seleccionar bebida"""
        result1 = self.vm.insert_coin()
        self.assertEqual(result1, "Coin Inserted. Select your drink.")
        self.assertEqual(self.vm.state, "Dispensing")

        result2 = self.vm.select_drink()
        self.assertEqual(result2, "Drink Dispensed. Thank you!")
        self.assertEqual(self.vm.state, "Ready")


# ------ Ejercicio 23 ------
# Verificamos que el funcionamiento del semaforo con estados "Red", "Green", "Yellow"

class TestTrafficLight(unittest.TestCase):
    """Pruebas unitarias para el ejercicio 23 - Traffic Light"""

    def setUp(self):
        """Configurar un semaforo nuevo antes de cada prueba"""
        self.tl = wb.TrafficLight()

    def test_initial_state_red(self):
        """Verificar que el estado inicial es 'Red'"""
        self.assertEqual(self.tl.get_current_state(), "Red")

    def test_change_from_red_to_green(self):
        """Verificar que desde Red cambia a Green"""
        self.tl.change_state()
        self.assertEqual(self.tl.get_current_state(), "Green")

    def test_change_from_green_to_yellow(self):
        """Verificar que desde Green cambia a Yellow"""
        self.tl.change_state()  # Red -> Green
        self.tl.change_state()  # Green -> Yellow
        self.assertEqual(self.tl.get_current_state(), "Yellow")

    def test_change_from_yellow_to_red(self):
        """Verificar que desde Yellow cambia a Red"""
        self.tl.change_state()  # Red -> Green
        self.tl.change_state()  # Green -> Yellow
        self.tl.change_state()  # Yellow -> Red
        self.assertEqual(self.tl.get_current_state(), "Red")

    def test_full_cycle(self):
        """Verificar el ciclo completo: Red -> Green -> Yellow -> Red"""
        states = []
        for _ in range(4):
            states.append(self.tl.get_current_state())
            self.tl.change_state()

        # Verificar la secuencia completa
        self.assertEqual(states, ["Red", "Green", "Yellow", "Red"])


# ------ Ejercicio 24 ------
# Verificar el sistema de autenticacion con estados "Logged Out" y "Logged In"

class TestUserAuthentication(unittest.TestCase):
    """Pruebas unitarias para el ejercicio 24 - User Authentication"""

    def setUp(self):
        """Configurar un sistema de autenticacion nuevo antes de cada prueba"""
        self.auth = wb.UserAuthentication()

    def test_initial_state_logged_out(self):
        """Verificar que el estado inicial es 'Logged Out'"""
        self.assertEqual(self.auth.state, "Logged Out")

    def test_login_when_logged_out(self):
        """Verificar que login desde estado Logged Out es exitoso"""
        result = self.auth.login()
        self.assertEqual(result, "Login successful")
        self.assertEqual(self.auth.state, "Logged In")

    def test_login_when_logged_in(self):
        """Verificar que login desde estado Logged In es invalido"""
        self.auth.login()  # Cambiar a Logged In
        result = self.auth.login()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.auth.state, "Logged In")  # Estado no cambia

    def test_logout_when_logged_in(self):
        """Verificar que logout desde estado Logged In es exitoso"""
        self.auth.login()  # Cambiar a Logged In
        result = self.auth.logout()
        self.assertEqual(result, "Logout successful")
        self.assertEqual(self.auth.state, "Logged Out")

    def test_logout_when_logged_out(self):
        """Verificar que logout desde estado Logged Out es invalido"""
        result = self.auth.logout()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.auth.state, "Logged Out")  # Estado no cambia

    def test_full_cycle(self):
        """Verificar el ciclo completo: login y logout"""
        result1 = self.auth.login()
        self.assertEqual(result1, "Login successful")
        self.assertEqual(self.auth.state, "Logged In")

        result2 = self.auth.logout()
        self.assertEqual(result2, "Logout successful")
        self.assertEqual(self.auth.state, "Logged Out")


# ------ Ejercicio 25 ------
# comprobamos el sistema de edicion de documentos con estados "Editing" y "Saved"

class TestDocumentEditingSystem(unittest.TestCase):
    """Pruebas unitarias para el ejercicio 25 - Document Editing System"""

    def setUp(self):
        """Configurar un sistema de edicion nuevo antes de cada prueba"""
        self.doc = wb.DocumentEditingSystem()

    def test_initial_state_editing(self):
        """Verificar que el estado inicial es 'Editing'"""
        self.assertEqual(self.doc.state, "Editing")

    def test_save_when_editing(self):
        """Verificar que guardar desde estado Editing es exitoso"""
        result = self.doc.save_document()
        self.assertEqual(result, "Document saved successfully")
        self.assertEqual(self.doc.state, "Saved")

    def test_save_when_saved(self):
        """Verificar que guardar desde estado Saved es invalido"""
        self.doc.save_document()  # Cambiar a Saved
        result = self.doc.save_document()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.doc.state, "Saved")  # Estado no cambia

    def test_edit_when_saved(self):
        """Verificar que editar desde estado Saved es exitoso"""
        self.doc.save_document()  # Cambiar a Saved
        result = self.doc.edit_document()
        self.assertEqual(result, "Editing resumed")
        self.assertEqual(self.doc.state, "Editing")

    def test_edit_when_editing(self):
        """Verificar que editar desde estado Editing es invalido"""
        result = self.doc.edit_document()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.doc.state, "Editing")  # Estado no cambia

    def test_full_cycle(self):
        """Verificar el ciclo completo: guardar y editar"""
        result1 = self.doc.save_document()
        self.assertEqual(result1, "Document saved successfully")
        self.assertEqual(self.doc.state, "Saved")

        result2 = self.doc.edit_document()
        self.assertEqual(result2, "Editing resumed")
        self.assertEqual(self.doc.state, "Editing")


# ------ Ejercicio 26 ------
# comprobamos el sistema de ascensor con estados "Idle", "Moving Up", "Moving Down"

class TestElevatorSystem(unittest.TestCase):
    """Pruebas unitarias para el ejercicio 26 - Elevator System"""

    def setUp(self):
        """Configurar un sistema de ascensor nuevo antes de cada prueba"""
        self.elevator = wb.ElevatorSystem()

    def test_initial_state_idle(self):
        """Verificar que el estado inicial es 'Idle'"""
        self.assertEqual(self.elevator.state, "Idle")

    def test_move_up_when_idle(self):
        """Verificar que mover arriba desde estado Idle es exitoso"""
        result = self.elevator.move_up()
        self.assertEqual(result, "Elevator moving up")
        self.assertEqual(self.elevator.state, "Moving Up")

    def test_move_up_when_moving_up(self):
        """Verificar que mover arriba desde estado Moving Up es invalido"""
        self.elevator.move_up()  # Cambiar a Moving Up
        result = self.elevator.move_up()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Moving Up")  # Estado no cambia

    def test_move_up_when_moving_down(self):
        """Verificar que mover arriba desde estado Moving Down es invalido"""
        self.elevator.move_down()  # Cambiar a Moving Down
        result = self.elevator.move_up()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Moving Down")  # Estado no cambia

    def test_move_down_when_idle(self):
        """Verificar que mover abajo desde estado Idle es exitoso"""
        result = self.elevator.move_down()
        self.assertEqual(result, "Elevator moving down")
        self.assertEqual(self.elevator.state, "Moving Down")

    def test_move_down_when_moving_down(self):
        """Verificar que mover abajo desde estado Moving Down es invalido"""
        self.elevator.move_down()  # Cambiar a Moving Down
        result = self.elevator.move_down()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Moving Down")  # Estado no cambia

    def test_move_down_when_moving_up(self):
        """Verificar que mover abajo desde estado Moving Up es invalido"""
        self.elevator.move_up()  # Cambiar a Moving Up
        result = self.elevator.move_down()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Moving Up")  # Estado no cambia

    def test_stop_when_moving_up(self):
        """Verificar que detener desde estado Moving Up es exitoso"""
        self.elevator.move_up()  # Cambiar a Moving Up
        result = self.elevator.stop()
        self.assertEqual(result, "Elevator stopped")
        self.assertEqual(self.elevator.state, "Idle")

    def test_stop_when_moving_down(self):
        """Verificar que detener desde estado Moving Down es exitoso"""
        self.elevator.move_down()  # Cambiar a Moving Down
        result = self.elevator.stop()
        self.assertEqual(result, "Elevator stopped")
        self.assertEqual(self.elevator.state, "Idle")

    def test_stop_when_idle(self):
        """Verificar que detener desde estado Idle es invalido"""
        result = self.elevator.stop()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Idle")  # Estado no cambia

    def test_full_cycle_up(self):
        """Verificar el ciclo completo: idle -> moving up -> stop"""
        result1 = self.elevator.move_up()
        self.assertEqual(result1, "Elevator moving up")
        self.assertEqual(self.elevator.state, "Moving Up")

        result2 = self.elevator.stop()
        self.assertEqual(result2, "Elevator stopped")
        self.assertEqual(self.elevator.state, "Idle")

    def test_full_cycle_down(self):
        """Verificar el ciclo completo: idle -> moving down -> stop"""
        result1 = self.elevator.move_down()
        self.assertEqual(result1, "Elevator moving down")
        self.assertEqual(self.elevator.state, "Moving Down")

        result2 = self.elevator.stop()
        self.assertEqual(result2, "Elevator stopped")
        self.assertEqual(self.elevator.state, "Idle")

if __name__ == '__main__':
    unittest.main()