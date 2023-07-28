from urllib.response import addclosehook
from flask import Flask, render_template,jsonify,request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin 

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_DB"] = "system"
mysql = MySQL(app)

#Esto esta obteniendo tipos de datos GET | busqueda de cliente
@app.route("/api/customers/<int:id>") 
@cross_origin()
async def getCustomer(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, first_name,last_name,email,phone,address FROM customers WHERE id=" + str(id))
    data = cur.fetchall()
    content = {}
    for row in data:
        content = { 
                    "id":row[0], 
                    "first_name":row[1], 
                    "last_name":row[2], 
                    "email":row[3], 
                    "phone":row[4],
                    "address":row[5] 
                    }
    return jsonify(content)

#Esto esta obteniendo tipos de datos GET | Mostrar todos los clientes
@app.route("/api/customers") 
@cross_origin()
async def getAllCustomers():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, first_name,last_name,email,phone,address FROM customers;")
    data = cur.fetchall()
    result = []
    for row in data:
        content = { 
                    "id":row[0], 
                    "frist_name":row[1], 
                    "last_name":row[2], 
                    "email":row[3], 
                    "phone":row[4],
                    "address":row[5] 
                    }
        result.append(content)
    return jsonify(result)

#Esto esta obteniendo tipos de datos POST, Creacion de clientes
@app.route("/api/customers", methods=["POST"]) 
@cross_origin()
async def AddCustomer():
    if "id" in request.json:
        modifyCustomer()
        return {"message":"Customer modified"}
    else:
        addCustomer()
        return {"message":"Customer created"}

#Esto esta obteniendo tipos de datos POST, nuevas entidades
@app.route("/api/customers", methods=["POST"]) 
@cross_origin()
async def addCustomer():
   cur = mysql.connection.cursor()
   cur.execute("INSERT INTO `customers` (`id`, `first_name`, `Last_name`, `email`, `phone`, `address`) VALUES (NULL, %s, %s, %s, %s, %s);", 
                (request.json["first_name"], request.json["last_name"], request.json["email"], request.json["phone"], request.json["address"]))
   mysql.connection.commit()
   return "Added customers"

#Esto esta obteniendo tipos de datos PUT, actualizacion de entidades
@app.route("/api/customers", methods=["PUT"]) 
@cross_origin()
async def modifyCustomer():
   cur = mysql.connection.cursor()
   cur.execute("UPDATE `customers` SET `first_name` = %s, `Last_name` = %s, `email` = %s, `phone` = %s, `address` = %s WHERE `customers`.`id` = %s;", 
                (request.json["first_name"], request.json["last_name"], request.json["email"], request.json["phone"], request.json["address"], request.json["id"]))
   mysql.connection.commit()
   return "Modified customers"

#Esto esta obteniendo tipos de datos POST
@app.route("/api/customers/<int:id>", methods=["DELETE"]) 
@cross_origin()
async def removeCustomer(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM `customers` WHERE `customers`.`id` = " + str(id) + ";")
    mysql.connection.commit()
    return "Deleted customers"


@app.route("/")
@cross_origin()
async def index():
    return render_template("index.html") 

if __name__ =="__main__":
    app.run(None, 3000, True)
if __name__ =="__main__":
    app.run(debbuger=True)