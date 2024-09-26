import sender_stand_request
import data
from data import user_body


# esta función cambia los valores en el parámetro "firstName"
def get_user_body(first_name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data"
    #   (datos) para conservar los datos del diccionario de origen
    current_body = data.user_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["firstName"] = first_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body

# Función de prueba positiva
def positive_assert(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)

    assert user_response.status_code == 201, f"Codigo de respuesta es {user_response.status_code}, se esperaba 201"

    assert user_response.json()["authToken"] != "", "El token de autenticación no se ha recibido"

    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1, "El usuario no se ha creado"

# Usuario o usuaria creada con éxito. El parámetro firstName contiene 2 caracteres
def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert('Aa')

# Usuario o usuaria creada con éxito. El parámetro firstName contiene 15 caracteres
def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert('Aaaaaaaaaaaaaaa')

# Usuario o usuaria creada con éxito. El parámetro firstName contiene caracteres latinos
def test_create_english_letter_in_first_name_get_success_response():
    positive_assert('Fredy')


# Función de prueba negativa
def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)
    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400, f"Codigo de respuesta es {response.status_code}, se esperaba 400"

    assert response.json()["code"] == 400, "El código de respuesta no es 400"

    expected_message = 'Has introducido un nombre de usuario no válido. El nombre solo puede contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres.'
    assert response.json()["message"] == expected_message, f"El mensaje de respuesta no es {expected_message}"


# El parámetro "firstName" contiene solo una caracter
def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol('A')

# El parámetro "firstName" contiene más de 15 caracteres
def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol('Aaaaaaaaaaaaaaaa')

# El parámetro "firstName" contiene un espacio
#def test_create_user_has_space_in_first_name_get_error_response():
#    negative_assert_symbol('A Aaa')

# El parámetro "firstName" contiene un string de caracteres especiales
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol('№%@')

# El parámetro "firstName" contienen un string de digitos
def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol('123')


def negative_assert_no_firt_name(user_body):
    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400, f"Codigo de respuesta es {response.status_code}, se esperaba 400"

    assert response.json()["code"] == 400, "El código de respuesta no es 400"

    expected_message = 'No se han aprobado todos los parámetros requeridos'
    assert response.json()["message"] == expected_message, f"El mensaje de respuesta no es {expected_message}"

# La solicitud no contiene el parámetro "firstName"
def test_create_user_no_first_name_get_error_response():
    user_body = data.user_body.copy()
    user_body.pop('firstName')

    negative_assert_no_firt_name(user_body)

# El parámetro "firstName" contiene un string vacío
def test_create_user_empty_first_name_get_error_response():
    user_body = get_user_body('')

    negative_assert_no_firt_name(user_body)

# El tipo del parámetro "firstName" es un número
def test_create_user_number_type_first_name_get_error_response():
    # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_body = get_user_body(12)
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable response
    response = sender_stand_request.post_new_user(user_body)

    assert response.status_code == 400