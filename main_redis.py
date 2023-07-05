import json
import logging
import os

import coloredlogs
import redis
from dotenv import load_dotenv

# create logger
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')

# take environment variables from .env.
load_dotenv()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # hacemos la conexion a redis
    r = redis.Redis(
        host=os.getenv('REDIS_HOST'),
        port=int(os.getenv('REDIS_PORT')),
        password=os.getenv('REDIS_PASSWORD'),
        db=0
    )

    # agregamos una variable 'foo' con valor 'bar'
    r.set('nombre_variable', 'valor_variable')

    # leemos la variable 'foo' y la dejamos en la variable 'test' de Python
    test = r.get('nombre_variable')
    logger.info(test)

    # hacemos un diccionario
    some_dict = {'nombre': 'Nezuko', 'edad': 32}

    # pasamos el diccionario a json
    json_object = json.dumps(some_dict, indent=4)

    # guardamos el diccionario
    r.set('json_object', json_object)

    # leemos el json y lo pasamos a diccionario
    get_json = json.loads(r.get('json_object'))

    # printiamos la edad
    logger.info(get_json['nombre'])
    logger.info(get_json['edad'])
