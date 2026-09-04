# Proyecto Urban Grocers 
Este proyecto contiene la suite de pruebas automatizadas para la API de creación de kits de usuario en la aplicación **Urban Grocers**, utilizando **Python**, **Requests** y **Pytest**.

## Descripción del Proyecto

Las pruebas verifican las reglas de negocio para el parámetro `name` al crear un kit de cliente mediante el endpoint `/api/v1/kits`. Se evalúan casos positivos (caracteres permitidos, longitudes límite de 1 y 511 caracteres) y casos negativos (cadena vacía, 512 caracteres, tipos de datos no válidos y cuerpo sin el parámetro).

*Nota: Algunos casos negativos devuelven un resultado `FAILED` debido a discrepancias conocidas entre la respuesta actual de la API y la documentación de requisitos.*
### Documentación de Referencia
* **Fuente de Documentación:** Se utilizó la documentación del proyecto alojada en **apiDoc** de Urban Grocers para definir los endpoints, encabezados, cuerpos de solicitud y respuestas esperadas (códigos HTTP y esquemas JSON).

### Tecnologías y Técnicas Utilizadas
* **Lenguaje y Librerías:** Python 3.10+, librería `requests` para peticiones HTTP y `pytest` como framework de ejecución de pruebas.
* **Técnicas de Prueba:** Diseño de casos mediante **Clases de Equivalencia** y **Análisis de Valores Límite** (longitudes de 1, 511 y 512 caracteres), pruebas funcionales de API REST, y aserciones automatizadas para códigos de estado HTTP (`201 Created`, `400 Bad Request`) y cuerpos de respuesta.
> 💡 **Nota sobre los comentarios en el código:**  
> Al ser un proyecto de carácter estudiantil y en proceso de aprendizaje, todo el código fuente incluye comentarios explicativos detallados paso a paso. Estos sirven como guía didáctica para facilitar la comprensión de la estructura, la lógica de las peticiones HTTP y las comprobaciones (`asserts`) a cualquier persona que no esté completamente familiarizada con el código.
---

## Archivos del Proyecto

* `configuration.py`: Contiene las URLs base y rutas relativas de los endpoints.
* `data.py`: Contiene las plantillas de datos para el cuerpo del usuario y del kit.
* `sender_stand_request.py`: Contiene las funciones para enviar peticiones HTTP (POST para usuarios y kits).
* `create_kit_name_kit_test.py`: Contiene la lógica de las pruebas y las funciones de aserción (`positive_assert` y `negative_assert_code_400`).
* `.gitignore`: Configuración para ignorar archivos temporales del entorno.
* `README.md`: Descripción e instrucciones del proyecto.

---

## Requisitos Previos

* Python 3.10+
* Administrador de paquetes `pip`

## Instalación y Configuración

1. Clonar el repositorio:
   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd qa-project-Urban-Grocers-app-es
2. Crear y activar un entorno virtual:

   ```bash
   python -m venv .venv
   # En Windows:
   .venv\Scripts\activate
3. Instalar las dependencias necesarias:

   ```bash
   pip install requests pytest
   
## Instrucciones para Ejecutar las Pruebas

1. Asegúrate de actualizar la URL base del servidor activo en el archivo **configuration.py**.

2. Ejecuta la suite completa de pruebas desde la terminal:

   ```bash
   pytest create_kit_name_kit_test.py
  
2. Para ver el detalle completo de la consola durante la ejecución:

   ```bash
   pytest create_kit_name_kit_test.py -v -s