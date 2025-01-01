from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__, static_folder='static')
app.config['JSON_AS_ASCII'] = False

cors = CORS(app, resource={
    r"/*":{
        "origin":"*"
    }
})



@app.route("/")
def home():    
    return ({"message": "Hello World!"})



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
