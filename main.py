# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def hello():
#     return 'Hello, World!'
# Note: Please install following libraries to run the flask API : flask, pymongo, dnspython, flask_cors
# > set FLASK_APP=flaskr
# > set FLASK_ENV=development
# > flask run

from flask import Flask, jsonify, request
from flask_cors import CORS
import pymongo
  
# connection_url = 'mongodb+srv://admin:samplearticle@cluster0-pm5vp.mongodb.net/test?retryWrites=true&w=majority'
connection_url = 'mongodb+srv://ibara1010:admin123@cluster0.4gh6a.mongodb.net/test?retryWrites=true&w=majority'
app = Flask(__name__)
client = pymongo.MongoClient(connection_url)

# Kalau butuh define sendiri :  
Database = client["mydatabase"]
SampleTable = Database["customers"]
# # Database
# Database = client.get_database('Example')
# # Table
# SampleTable = Database.SampleTable

@app.route('/', methods=['GET'])
def index():
  return "Hello World!"

# To insert a single document into the database,
# insert_one() function is used
@app.route('/insert-one/<name>/<id>/', methods=['GET'])
def insertOne(name, id):
    queryObject = {
        'Name': name,
        'ID': id
    }
    query = SampleTable.insert_one(queryObject)
    return "Query inserted...!!!"
  
# To find the first document that matches a defined query,
# find_one function is used and the query to match is passed
# as an argument.
@app.route('/find-one/<argument>/<value>/', methods=['GET'])
def findOne(argument, value):
    queryObject = {argument: value}
    query = SampleTable.find_one(queryObject)
    query.pop('_id')
    return jsonify(query)
  
# To find all the entries/documents in a table/collection,
# find() function is used. If you want to find all the documents
# that matches a certain query, you can pass a queryObject as an
# argument.
@app.route('/find/', methods=['GET'])
def findAll():
    query = SampleTable.find()
    output = {}
    i = 0
    for x in query:
        output[i] = x
        output[i].pop('_id')
        i += 1
    return jsonify(output)
  
  
# To update a document in a collection, update_one()
# function is used. The queryObject to find the document is passed as
# the first argument, the corresponding updateObject is passed as the
# second argument under the '$set' index.
@app.route('/update/<key>/<value>/<element>/<updateValue>/', methods=['GET'])
def update(key, value, element, updateValue):
    queryObject = {key: value}
    updateObject = {element: updateValue}
    query = SampleTable.update_one(queryObject, {'$set': updateObject})
    if query.acknowledged:
        return "Update Successful"
    else:
        return "Update Unsuccessful"
  
  
if __name__ == '__main__':
    # app.run(debug=True)
    app.run( # Starts the site
      host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
      port=5000,  # Randomly select the port the machine hosts on.
      debug=True
    )