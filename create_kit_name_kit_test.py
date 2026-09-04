#Este archivo contiene dos partes principales: funciones auxiliares(que hacen el trabajo repetitivo) y los
#casos de prueba(los que verifican que la API funcione según los requerimientos)

import sender_stand_request
import data

# 1. Función auxiliar para modificar el nombre del kit

# Toma la plantilla de datos data.kit_body (en data.py) y hace una copia para no alterar la variable original
def get_kit_body(name):
    current_body =data.kit_body.copy()
    # Reemplaza "name" por el texto o valor que se vaya a probar (ej: "a")
    current_body["name"] = name
    return current_body

# 2. Función auxiliar para pruebas exitosas (assertss positivos)
def positive_assert(name):
    #Paso A: Crear el usuario para obtener su token
    # Llama a post_new_user para registrar un usuario de prueba en la API y extrae su "authToken"
    response_user = sender_stand_request.post_new_user(data.user_body)
    auth_token = response_user.json()["authToken"]


    #Paso B: Generar el cuerpo de la petición con el nombre del kit
    #Llama a la función anterior get_kit_body(name) para preparar los datos del kit con ell nombre a evaluar
    kit_body = get_kit_body(name)

    #Paso C: Enviar la petición POST  para crear el kit
    #Llama a la función pos_new_client_kit enviando los datos del kit y el token para creae el kit e el servidor
    response_kit = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    #Paso D: Comprobaciones (Asserts)
    #Valida que la respuesta del servidor devuelva el código HTTP 201 Created y que el nombre en el JSON retornado
    #coincida exactamente con el parámetro "name" que le pasamos
    assert response_kit.status_code == 201
    assert response_kit.json()["name"] == name

# 3. Función auxiliar para casos que deben devolver error 400
def negative_assert_code_400(name):
    response_user = sender_stand_request.post_new_user(data.user_body)
    auth_token = response_user.json()["authToken"]

    kit_body = get_kit_body(name)
    response_kit = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    #Comprobar que el código de estado sea 400
    assert response_kit.status_code == 400


#  Función de prueban (Test Case 1)
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

#  Función de prueba (Test Case 2)
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

#  Función de prueba (Test Case 3)
def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_code_400("") #FAILED: resultado esperado [400], resultado actual [201]

# Función de prueba (Test Case 4)
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
                             #FAILED: resultado esperado [400], resultado actual [201]
# Función de prueba (Test Case 5)
def test_create_kit_has_special_characters_in_name_get_success_response():
    positive_assert('"№%@,"')

# Función de prueba (Test Case 6)
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert("A Aaa")

# Función de prueba (Test Case 7)
def test_create_kit_has_number_in_name_get_succes_response():
    positive_assert("123")

# Función de prueba (Test Case 8)
def test_create_kit_no_name_in_body_get_error_response():
    response_kit = sender_stand_request.post_new_user(data.user_body)
    auth_token = response_kit.json()["authToken"]
    #Enviar el cuerpo vacío (sin el campo "name")
    kit_body = {}
    response_kit = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response_kit.status_code == 400 #FAILED: resultado esperado [400], resultado actual [500]

# Función de prueba (Test Case 9)
def test_create_kit_has_number_type_in_body_get_error_response():
    negative_assert_code_400(123) #FAILED: resultado esperado [400], resultado actual [201]