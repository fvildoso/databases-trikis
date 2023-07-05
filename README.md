# databases-trikis

Este proyecto "databases-trikis" es una aplicación que utiliza SQLAlchemy, Redis y H2O. A continuación, se detallan los
requerimientos para ejecutar el proyecto.

## Requerimientos

- MariaDB/MySQL
- Python 3.10
- Java 11
- H2O
- Redis

## Instalación

1. Clonar el repositorio de "databases-trikis":

```
git clone https://github.com/fvildoso/databases-trikis
```
2. Accede al directorio del proyecto:
```
cd databases-trikis
```
3. Crear un entorno virtual con alguna de las siguientes opciones: 
   - Se recomienda hacerlo en PyCharm, ya que el proceso es automático.
   - Manual
      1. Crear el entorno virtual.
      ```
      python -m venv venv
      ```
    
      2. Activar el entorno virtual:
         - En Windows:
         ```
         venv\\Scripts\\activate
         ```
         - En Linux/macOS:
         ```
         - source venv/bin/activate
         ```

4. Instala las dependencias requeridas:
```
pip install -r requirements.txt
```
## Configuración
Antes de ejecutar la aplicación, asegúrate de configurar correctamente los siguientes parámetros:
    
- SQLAlchemy: Actualiza la URL de conexión a tu base de datos en el archivo de configuración correspondiente.
- Redis: Verifica la configuración de conexión a Redis en el archivo de configuración correspondiente.
- H2O: Asegúrate de tener H2O correctamente instalado y configurado según tus necesidades.

## Uso
Para ejecutar el proyecto "databases-trikis", sigue estos pasos:

1. Activa el entorno virtual (si no lo has hecho ya):

    - En Windows:
        ```
        venv\\Scripts\\activate
        ```
    - En Linux/macOS:
        ```
        source venv/bin/activate
        ```

2. Ejecuta el archivo principal de la aplicación:
```
python main_sqlalchemy.py
```
```
python main_h2o.py
```
```
python main_redis.py
```
 
¡Listo! Ahora puedes utilizar el proyecto "databases-trikis" con SQLAlchemy, Redis y H2O.

## Contribución
Si deseas contribuir a este proyecto, siéntete libre de realizar un fork y enviar tus pull requests. Serán revisados y considerados.

## Licencia
Este proyecto está bajo la licencia MIT. Puedes consultar el archivo `LICENSE` para más detalles.

<img src="random/img.png" alt="random">