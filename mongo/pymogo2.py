#from bson import json_util
import json
import pymongo
from flask import Flask,request,render_template
#from bson import BSON

app = Flask(__name__)

#connecting to mongodb database
client = pymongo.MongoClient("mongodb://localhost:27017/new_database")

#creating databse
data = client['new_database']

#creating list
coll = data['new_collection']

#getting json data nand sending to mongodb database
@app.route("/", methods=['POST'])
def insert_document():
    req_data = json.dumps(request.get_json())
    print(req_data)
   
    coll.insert_one(request.get_json())
    print("data aded successfully")
    return "json posted"


    
#running api
if __name__ == '__main__':
    app.run(host="0.0.0.0",port = 2555)