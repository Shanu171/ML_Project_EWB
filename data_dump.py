 
import  pymongo
import pandas as pd
import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import csv
client = pymongo.MongoClient("mongodb+srv://shanusinghruhela171:ShanuR%40171@cluster0.yuvoign.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db = client.test

    
DATA_FILE_PATH = (r'C:\Users\prana\Music\resume_based_project\ML_Project_EWB\insurance.csv')
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"


if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and column: {df.shape}")
    df.reset_index(drop = True,inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)


