#En data.py definimos el encabezado (headers) y la estructura(body) de los datos que se enviarán a la aPI.
#Headers: indican el tipo de contenido (ej: content-type: application/json) y el token de autorizacion si aplica.
#Body: son los datos que se envían al servidor en dormato de diccionario de python

#Headers le indica a la API que los datos enviados están formateados como JSON
headers = {
    "Content-Type": "application/json"
}

#user_body incluye los datos minimos necesarios para registrar un usuario de prueba: nombre, telefono y diección
user_body = {
    "firstName": "Andrea",
    "phone": "+10005553535",
    "address": "123 Calle Principal"
}

#kit_body es la estructura básica que se usará para probar la creación de kits, enviando el campo "name".
kit_body = {
    "name": "Mi Kit"
}