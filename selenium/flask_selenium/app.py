from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
    db = client["web_page"]
    return db

@app.route('/')
def ping_server():
    return "Welcome to the world of webs."

@app.route('/webs')
def get_stored_animals():
    db=""
    try:
        db = get_db()
        _products = db.clients.find()
        products = [{"producto": animal["producto"], "precio": animal["precio"], "url": animal["url"]} for animal in _products]
        return jsonify({"products": products})
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
