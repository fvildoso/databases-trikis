import logging

import coloredlogs
import pymongo
from dotenv import load_dotenv

# create logger
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')

# take environment variables from .env.
load_dotenv()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    mydict = {"name": "John", "address": "Highway 37"}

    x = mycol.insert_one(mydict)
