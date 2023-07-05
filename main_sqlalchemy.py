import datetime
import json
import logging
import os

import coloredlogs
import randomname
from dotenv import load_dotenv
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import Session

from sqlalchemy_models import ResumenAmigos, metadata

# create logger
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')

# take environment variables from .env.
load_dotenv()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # conexión con la base de datos
    engine = create_engine(os.getenv('SQLALCHEMY_DATABASE'))

    # Crear todas las tablas que no existan en la base de datos, llamando metadata de models.
    metadata.create_all(engine)

    # iniciamos una sesión
    session = Session(engine)

    # obtener último ID de los cazadores
    lastId = session.query(ResumenAmigos).order_by(ResumenAmigos.id.desc()).first()
    if lastId is None:
        lastId = 1
    else:
        lastId = lastId.id
    logger.info("LastID=" + str(lastId))

    print()
    logger.info("Creamos registros...")
    for x in range(10):
        lastId = lastId + 1

        dict_resumen_amigo = {'name': randomname.get_name(), 'datetime': str(datetime.datetime.now())}
        json_resumen_amigo = json.dumps(dict_resumen_amigo, indent=4)

        stmt = insert(ResumenAmigos).values(id=lastId, json=json_resumen_amigo)
        result = session.execute(stmt)
    session.commit()

    print()
    logger.info("Mostramos todos los registros...")
    query = session.query(ResumenAmigos)

    for amigo in query:
        logger.info(amigo.json)

    # cerramos la sesión con la base de datos
    session.close()
