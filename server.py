import json
import mysql.connector
from flask import Flask, request
import os
from db_to_jsonl import export_table_to_jsonl

app = Flask(__name__)

@app.route('/9moisacroquer/UpdateCollection/', methods=['GET'])
update_collection():
    table_name = request.args.get('table_name')
    try:
        export_table_to_jsonl(table_name)
        return json.dumps({"Success": "Table updated"})
    except:
        return json.dumps({"Error": "Table doesn't exist"})

if __name__ == '__main__':
    app.run(debug=True) 

