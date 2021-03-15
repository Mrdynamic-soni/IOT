from flask import Flask,request,render_template,jsonify
import sqlite3
import time
import json

app = Flask(__name__)


#recieving data from node MCU and logging into database
@app.route("/",methods =["GET","POST"])
def node():
#     req_json = json.dumps(request.get_json()) #feth data frm node MCU
#     print(req_json) #printing that data in  terminal
    req_json = request.data.decode("utf-8")
    
    #creating database
    conn = None;
    conn = sqlite3.connect("file.db")
    curs = conn.cursor()
    print("datatable created successfully")
  
   
    if(curs.fetchone() == 0):
     #creating table for database
        conn.execute("create table database(sensor_name text,temperature float,humidity float)")
    else:
       #insertng data into databse
        #conn.execute("insert into database values(?,?,?)",req_json)
        curs.execute('insert into database (sensor_name,temperature,humidity) '
                 'values (:SENSOR,:TEMPERATURE,:HUMIDITY)', [req_json])
    
       #commiting changes
        conn.commit()
        conn.close()
   
    return "json posted"


if __name__ == '__main__':
    app.run(host="0.0.0.0",port = 2777)