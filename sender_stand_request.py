#En este archivo se crean las fuciones que enviarán las peticiones a la API usando la librería "requests"
#Para que lo anterior sea posible, son necesarias dos funciones:
# 1.Crear un nuevo usuario: La API Urban Grocers requiere que un usuario exista primero para obtener un token de autorización(authToken)
# el cual es necesario para crear kits
# 2.Crear un kit: La funcion que enviará la solicitud POST a la ruta de kits incluyendo el token en los encabezados

import configuration
import requests  #esta librería no viene instalada de forma predeterminada, hay que instalarla (install package request)
import data

#Envía una petición POST con la informacion del usuario a la ruta /api/v1/users
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

#Toma los datos del kit y el auth_token del usuario creado, agrega la cabecera "Authorization" y envía la petición POST a /api/v1/kits
def post_new_client_kit(kit_body, auth_token):
    #Copia los encabezados actuales para no modificar la variable original directamente
    current_headers = data.headers.copy()
    #Añade el token de autorización a los encabezados
    current_headers["Authorization"] = "Bearer " + auth_token

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=current_headers)