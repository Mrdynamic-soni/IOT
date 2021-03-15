from flask import Flask,request,render_template,jsonify
import sqlite3
import time
import json

app = Flask(__name__)

# DATA =[];

#recieving data from node MCU and logging into database
@app.route("/",methods =["GET","POST"])
def node():
    
    #feth data from node MCU
    data = request.data
    
    #printing that data in  terminal
    print(data) 
    
    # decoding incoming data form node MCU 
    #DATA = DATA.append(data)
    
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
        conn.executemany("insert into database values(?,?,?);",(data))
        #conn.execute("insert into database(sensor_name,temperature,humidity)  values('dht11',34.6,23.8)")
        print("data appended successfully")
    #commiting changes
        conn.commit()
        conn.close()

    return "json posted"
    
#running api
if __name__ == '__main__':
    app.run(host="0.0.0.0",port = 2777)