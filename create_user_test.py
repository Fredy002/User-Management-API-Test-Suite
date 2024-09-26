import configuration
import data
from data


# esta función cambia los valores en el parámetro "firstName"
def get_user_body(first_name):
    # el diccionario que contiene el cuerpo de solicitud se copia del archivo "data"
    #   (datos) para conservar los datos del diccionario de origen
    current_body = data.user_body.copy()
    # Se cambia el valor del parámetro firstName
    current_body["firstName"] = first_name
    # Se devuelve un nuevo diccionario con el valor firstName requerido
    return current_body

def test_create_user_2_letter_in_first_name_get_success_response():
    user_body = get_user_body('Aa')
    user_response = sender_stand_request.post_new_user(user_body)
    return