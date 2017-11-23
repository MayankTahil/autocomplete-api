from flask import jsonify, Flask, request
from flask_cors import CORS
from dbHelper import dbHelper

app = Flask(__name__)
CORS(app)

@app.route('/api',methods=['GET'])
def autocomplete():
    search = request.args.get('input')
    app.logger.debug(search)
    # Helper utilities to filter the BD based on what's passed into the search
    db = dbHelper()
    db.initConnection()
    products = db.queryDB(filter=search)
    products = db.formatData(products)
    return jsonify(json_list=products)

@app.route('/probe')
def probe():
    return '200 OK'