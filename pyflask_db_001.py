from math import *
from datetime import timedelta, datetime
from flask import  (
    Flask,
    render_template,
    request
)
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask import jsonify

###Ket noi database mongoDB
import pymongo 
from pymongo import MongoClient 

MONGO_URI = 'mongodb+srv://admin:12345@nicolast-fqfxo.gcp.mongodb.net/test?retryWrites=true&w=majority'
cluster = MongoClient(MONGO_URI)
db = cluster["ATN_Toys"]


app = Flask(__name__)
#db_connect = create_engine('sqlite:///dsNhanVien.db')

@app.route('/')
def  index():
    return "<h1> Flask DB 001 - Connecting !!! </h1>"

@app.route('/login', methods=['GET', 'POST'])
def  login():
    query_parameters = request.args
    vusername= query_parameters.get("username")
    vusername= query_parameters.get("password")

    ###Check account username va pass
    collection= db["Staff"]
    results = collection.find({"username":"Thanh", "password": "1234"}) 

    if len(results) == 1:
        logined_flag = True
        return render_template("home.html")
    else:
        return render_template("login.html")

@app.route('/profile')
def  profile():
    return render_template("profile.html")

@app.route('/params', methods=['GET'])
def api_filter():
    query_parameters = request.args
    return jsonify(query_parameters)


@app.route('/giaiptb1', methods=['GET'])
def giaiptb1():
    query_parameters = request.args
    a = query_parameters.get("a")
    b = query_parameters.get("b")

    a = int(a)
    b = int(b)

    str = "khong co nghiem"
    
    kq = { "tt" : str }

    if a == 0 and b == 0:
        str = "VSN"
        kq = { "tt" : str }
    elif a != 0:
        x =  -b/a
        str = "co 1 nghiem"
        kq = { "tt" : str , "x" : x}
    else:
        str = "KoCoN"
        kq = { "tt" : str }
    return jsonify(kq)


@app.route('/giaiptb2', methods=['GET'])
def giaiptb2():
    query_parameters = request.args
    a = query_parameters.get("a")
    b = query_parameters.get("b")
    c = query_parameters.get("c")

    a = int(a)
    b = int(b)
    c = int(c)

    d=(b*b)-(4*a*c)

    str = "khong co nghiem"
    
    kq = { "tt" : str }

    if d==0:
        x= -b/(2*a)
        str = "co nghiem kep"
        kq = { "tt" : str, "x":x }
    elif d > 0:
        x=(-b+(sqrt(d))/(2*a))
        str = "co 2 nghiem"
        kq = { "tt" : str , "x1": x,"x2":x}
    else:
        str = "Ko co nghiem"
        kq = { "tt" : str }
    return jsonify(kq)

@app.route('/tamgiac', methods=['GET'])
def tamgiac():
    query_parameters = request.args
    a = query_parameters.get("a")
    b = query_parameters.get("b")
    c = query_parameters.get("c")

    a = int(a)
    b = int(b)
    c = int(c)

    str = "khong co nghiem"
    
    kq = { "tt" : str }

    if(a==b and b==c):
        kq= "Tam giac deu"
        if (a*a==b*b+c*c):
            kq= "Tam giac vuong"
        elif (a==b | b==c | a==c):
            kq= "Tam giac can"
        elif (a+b>c and a+c>b and b+c>a):
            kq= "Tam giac thuong"
    else: 
        kq= "Khong phai tam giac"
    return jsonify(kq)

@app.route('/ngayke', methods=['GET'])
def ngayke():
    query_parameters = request.args
    a = query_parameters.get("ngay")
    b = query_parameters.get("thang")
    c = query_parameters.get("nam")

    a = int(a)
    b = int(b)
    c = int(c)
   # s = a,b,c
    s = "20/3/2000"
   # day, month, year = map(int, date.split('-'))
    
   # date += datetime.timedelta(days=1)
    date = datetime.strptime(s, "%d/%m/%Y")
    modified_date = date + timedelta(days=1)
    datetime.strftime(modified_date, "%d/%m/%Y")
    

class Parameters(Resource):
    def get(self, firstParam):
        return "Day la tam so " + firstParam

api = Api(app)
api.add_resource(Parameters, '/parameters/<firstParam>') # Route_1
