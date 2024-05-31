# Comprensor de comunicaciones 

## Descripción
El Compresor de Comunicaciones es una herramienta diseñada para optimizar la transmisión de datos 
al reducir el tamaño de los archivos sin comprometer la integridad de la información. 
Utilizando algoritmos avanzados de compresión, este proyecto busca facilitar la 
transferencia de datos en entornos donde el ancho de banda es limitado o costoso..

## Características
Enumera las características principales de tu proyecto. Por ejemplo:
- Compresión de datos utilizando algoritmos.
- Interfaz fácil de usar para comprimir y descomprimir archivos.
- Soporte para múltiples tipos de archivos y formatos de datos.

## Instalación

# Instalación de Kivy en Windows

Kivy es un framework de código abierto para desarrollar aplicaciones multitáctiles que se pueden ejecutar en múltiples plataformas incluyendo Windows. A continuación, se detallan los pasos para instalar Kivy en un sistema Windows.

## Requisitos Previos

Asegúrate de tener Python instalado. Puedes descargarlo desde [python.org](https://www.python.org/).

## Pasos para la Instalación

### 1. Actualiza pip y herramientas asociadas
Abre la terminal de comandos como administrador y ejecuta:
```bash
python -m pip install --upgrade pip wheel setuptools
```
### Paso 2: Instalar las dependencias de Kivy

Para asegurar que Kivy funcione correctamente en tu sistema, necesitas instalar algunas dependencias específicas. Abre la terminal de comandos como administrador y ejecuta el siguiente comando para instalar estas dependencias esenciales:

```bash
python -m pip install docutils pygments pypiwin32 kivy_deps.sdl2 kivy_deps.glew kivy_deps.gstreamer
```
### Paso 3: Instalar Kivy

Una vez que hayas instalado todas las dependencias necesarias, puedes proceder a instalar Kivy. Kivy es un framework poderoso que permite el desarrollo de aplicaciones multitáctiles y multiplataforma. Para instalar Kivy, abre tu terminal de comandos como administrador y ejecuta el siguiente comando:
```bash
pip install kivy
```
### paso 4: instalar pandas 

```bash
pip install pandas 
```
### paso 5: instalar psycopg2

```bash
pip install psycopg2
```
# instrucciones para ejecutar el programa 

Proporciona instrucciones claras sobre cómo instalar y configurar el proyecto. Por ejemplo:
1. Clona el repositorio a tu máquina local:
   ```
   git clone https://github.com/jorgebls/compresor_de_comunicaciones
   ```
2. Navega al directorio del proyecto:
   ```
   cd compresor_de_comunicaciones/
   ```
3. Ejecutar el programa en consola :
   ```
   python src/console/console.py
   ```
4. Ejecutar el programa en la interfaz:
   ```
   python src/Gui/interfaz.py

   ```
5. Ejecutar la base de datos por consola:
   ```
   python src/view/consoledb.py
   ```

## Base de Datos del Sistema de Compresión de Textos

### Descripción de la Base de Datos

El sistema utiliza una base de datos **PostgreSQL** hospedada en **Neon** para gestionar eficientemente los datos de los usuarios y sus operaciones de compresión y descompresión de textos. La base de datos permite realizar inserciones, actualizaciones, eliminaciones y consultas de manera segura y eficaz.

### Estructura y Variables Almacenadas

La tabla `Usuarios` en la base de datos almacena los siguientes datos:

- **Cédula (BIGINT)**: Identificador único para cada usuario.
- **Nombre (VARCHAR)**: Nombre del usuario.
- **Teléfono (BIGINT)**: Número de teléfono del usuario.
- **CorreoElectronico (VARCHAR)**: Correo electrónico del usuario.
- **TipoEvento (VARCHAR)**: Indica si la operación fue de compresión o descompresión.
- **TextoOriginal (TEXT)**: Texto original proporcionado por el usuario.
- **TextoProcesado (TEXT)**: Resultado del texto después de la compresión o descompresión.
- **FechaHora (TIMESTAMP)**: Marca de tiempo del evento guardada automáticamente.

### Funcionalidades Clave

- **Creación Automática de Tabla**: Al iniciar el sistema, se verifica y crea la tabla de usuarios si no existe.
- **Manejo de Excepciones**: Se gestionan las excepciones para prevenir errores comunes como duplicaciones de entradas o búsquedas de registros inexistentes, manteniendo la integridad de la base de datos.

Esta base de datos PostgreSQL proporciona una plataforma robusta para el almacenamiento y gestión de datos dentro del sistema de compresión de textos, asegurando un funcionamiento eficiente y seguro del mismo.

   
# instrucciones para ejecutar los casos de prueba

Proporciona instrucciones claras sobre cómo instalar y configurar el proyecto. Por ejemplo:
1. Clona el repositorio a tu máquina local:
   ```
   git clone https://github.com/jorgebls/compresor_de_comunicaciones
   ```
2. Navega al directorio del proyecto:
   ```
   cd compresor_de_comunicaciones/
   ```
3. Ejecutar casos de prueba:
   ```
   python test/testcaseregular.py
   ```
   ```
   python test/testcasesextraordinary.py
   ```
   ```
   python test/testcaseerror.py
   ```
4. Ejecutar pruebas de base de datos:
   ```
   python test/testdb.py  
   

## Ejecución
Explica cómo utilizar tu proyecto. Por ejemplo:

Se abrirá una interfaz de usuario donde puedes seleccionar los archivos que deseas comprimir o descomprimir.


## Ejemplos
Se proporciona un pedazo de código de que como funciona para comprimir o descomprimir un archivo. Por ejemplo:

```python
# Ejemplo de cómo comprimir o descomprimir un texto por consola

#comprimir

(base) jorge@jorge-IdeaPad:~/Música/compresor_de_comunicaciones$ /bin/python3 /home/jorge/Música/compresor_de_comunicaciones/src/console/console.py
Bienvenido a la aplicación de compresión/descompresión de texto.
Por favor, ingrese el texto: hola mundo 
¿Desea comprimir o descomprimir el texto? (comprimir/descomprimir): comprimir
Texto comprimido (en bytes): 789ccbc8cf4954c82dcd4bc957000019460408

#descomprimir

(base) jorge@jorge-IdeaPad:~/Música/compresor_de_comunicaciones$ /bin/python3 /home/jorge/Música/compresor_de_comunicaciones/src/console/console.py
Bienvenido a la aplicación de compresión/descompresión de texto.
Por favor, ingrese el texto: 789ccbc8cf4954c82dcd4bc957000019460408
¿Desea comprimir o descomprimir el texto? (comprimir/descomprimir): descomprimir
Texto descomprimido: hola mundo 

```

## Licencia MIT

Copyright (c) 2024  

Autores: NEHIR RODRIGUEZ, JORGE BEDOYA

Colaboradores: ANA SOFIA LONDOÑO, ALEJANDRO RIVERA

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia
de este software y los archivos de documentación asociados (el "Software"), para tratar
en el Software sin restricciones, incluidos, entre otros, los derechos
utilizar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar y / o vender
copias del Software, y permitir a las personas a quienes se les proporcione el Software lo hagan
lo mismo, sujeto a las siguientes condiciones:

El aviso de derechos de autor anterior y este aviso de permiso se incluirán en todos
copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O
IMPLÍCITO, INCLUYENDO PERO NO LIMITADO A LAS GARANTÍAS DE COMERCIABILIDAD,
ADECUACIÓN PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO
LOS AUTORES O TITULARES DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES DE NINGÚN RECLAMO, DAÑO U OTRO
RESPONSABILIDAD, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O DE OTRO MODO, DERIVADO DE,
FUERA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTROS NEGOCIOS EN EL
EL SOFTWARE.
