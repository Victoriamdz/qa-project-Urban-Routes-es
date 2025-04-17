# Urban Routes

## Descripción del Proyecto

El proyecto tiene como objetivo automatizar pruebas para la plataforma de viajes **Urban Routes**.

El proyecto implementa **Selenium** para interactuar con la interfaz web.

## Tecnologías y Técnicas Utilizadas

- **Python**: Lenguaje de programación para la automatización de las pruebas.
- **Selenium WebDriver**: Herramienta para la automatización de las interacciones
- **Pytest**: Framework para escribir y ejecutar pruebas.  
- **ChromeDriver**: Utilizado en conjunto con Selenium para controlar el navegador Chrome y ejecutar las pruebas.

## Instrucciones para Ejecutar las Pruebas

1. **Clona el repositorio**:
   ```bash
   git clone [git@github.com:Victoriamdz/qa-project-Urban-Routes-es.git]
   
###  **Instalar dependencias**

pip install -r requirements.txt


###  **Configurar datos en el archivo data.py:**


urban_routes_url = ''
address_from = 'East 2nd Street, 601'
address_to = '1300 1st St'
phone_number = '+1 123 123 12 12'
card_number, card_code = '1234 5678 9100', '111'
message_for_driver = 'Muéstrame el camino al museo'

###  **Ejecutar pruebas**
pytest

