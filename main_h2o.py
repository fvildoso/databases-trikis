import os

import h2o
from dotenv import load_dotenv

from h2o.estimators import H2OGradientBoostingEstimator

# take environment variables from .env.
load_dotenv()

if __name__ == '__main__':
    # nos conectamos el 'cluster' de h2o, y decimos donde está el driver de mariadb
    h2o.init(extra_classpath=["drivers/mariadb-java-client-3.0.5.jar"])

    # mostramos el estado del cluster
    h2o.cluster().show_status()

    # datos de conexión
    conn_url = os.getenv('H2O_MARIADB_URL')
    username = os.getenv('H2O_MARIADB_USER')
    password = os.getenv('H2O_MARIADB_PASS')

    # podemos leer los datos de una tabla directamente usando su nombre
    table = "cars_20mpg"
    mariaDBTable = h2o.import_sql_table(conn_url, table, username, password)
    print(mariaDBTable)

    # también podemos usar datos de una query
    select_query = "SELECT * from cars_20mpg"
    mariaDBQuery = h2o.import_sql_select(conn_url, select_query, username, password)
    print(mariaDBQuery)

    # ༼ つ ◕_◕ ༽つ
    # el resto del código ya es específico sobre h2o

    # transformamos la columna economy_20mpg a categórica
    mariaDBQuery["economy_20mpg"] = mariaDBQuery["economy_20mpg"].asfactor()

    # set the predictor names and the response column name
    predictors = ["displacement", "power", "weight", "acceleration", "year"]
    response = "economy_20mpg"

    # split into train and validation sets
    train, valid = mariaDBQuery.split_frame(ratios=[.8], seed=1234)

    # try using the `y` parameter:
    # first initialize your estimator
    cars_gbm = H2OGradientBoostingEstimator(seed=1234)

    # then train your model, where you specify your 'x' predictors, your 'y' the response column
    # training_frame and validation_frame
    cars_gbm.train(x=predictors, y=response, training_frame=train, validation_frame=valid)

    # print the auc for the validation data
    auc = cars_gbm.auc(valid=True)
    print('AUC=' + str(auc))
