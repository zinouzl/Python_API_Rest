# import micro freamwork flask to bluid the rest api
from flask import Flask ,g
import os
import markdown
import shelve
from  flask_restful import reqparse, Resource,Api


# Creating the instance of flask
app = Flask(__name__)

api = Api(app)

# database functionalities
def get_db():
     db = getattr(g,'_database',None)
     if db is None:
         db = g._database = shelve.open("employee.db")
     return db
@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g,'_database',None)
    if db is not None:
        db.close()


# localhost:5000\
@app.route("/")
def index():

    #opening the README file.
    with open(os.path.dirname(app.root_path)+ '/README.md', 'r') as readmeFile:

        content = readmeFile.read()
        # markdown the readme file and send it to the client
        return markdown.markdown(content)
    
    
class Employees(Resource):
    # the GET methode for retriving all employees
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())


        employees = []

        for key in keys:
            employees.append(shelf[key])

        return {'message': 'Success' , 'data':employees},200


    # POST methode for adding new employee
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('id',required=True)
        parser.add_argument('firstName',required=True)
        parser.add_argument('lastName',required=True)
        parser.add_argument('age',required=True)
        parser.add_argument('yearsInService',required=True)

        args = parser.parse_args()

        shelf = get_db()
        shelf[args['id']] = args

        return {'message' : 'Employee registered', 'data': args}, 201


class Employee(Resource):
    def get(self,id):
        shelf = get_db()

        # see if the key does not exist in the database return 404 error
        if (not id in shelf):
            return {'message':'Employee not found','data':{}}, 404
        return {'message':'Employee found','data':shelf[id]}, 200

    def delete(self,id):
        shelf = get_db()
        # see if the key does not exist in the database return 404 error
        if (not id in shelf):
            return {'message':'Employee not found','data':{}}, 404

        del shelf[id]
        return '', 204
        
    
api.add_resource(Employees,'/employees')
api.add_resource(Employee,'/employees/<string:id>')





'''
@app.route("/login")
def login():
    auth = request.authorization
    if auth != None:

        if auth.password == 'password':
            return jsonify("hello ussser!")
        else: 
            return make_response(" password not correct",401,{'WWW-Authenticate':'Basic realm="login Required"'})

    return make_response("verify",401,{'WWW-Authenticate':'Basic realm="login Required"'})

'''

