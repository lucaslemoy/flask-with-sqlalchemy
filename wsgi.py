from flask import Flask, jsonify
from config import Config
app = Flask(__name__)
app.config.from_object(Config)

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow # Order is important here!
db = SQLAlchemy(app)
ma = Marshmallow(app)

from models import Product
from schemas import products_schema

@app.route('/hello')
def hello():
    return "Hello World!"

@app.route('/products')
def products():
    products = db.session.query(Product).all() # SQLAlchemy request => 'SELECT * FROM products'
    return products_schema.jsonify(products)

@app.route('/products/<int:id_product>')
def products_id(id_product):
    products = db.session.query(Product).get(id_product) # SQLAlchemy request => 'SELECT * FROM products'
    mon_dico = {'id':products.id,'name':products.name}
    return jsonify(mon_dico)

@app.route('/products/add')
def products_add():
    new_product=Product(name='Lucas',description='toto')
    db.session.add(new_product)
    #products = db.session.query(Product).get(id_product)
    #return jsonify(mon_dico)
    return '',204
