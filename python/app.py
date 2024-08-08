from flask import Flask
from flask import request
from flask_cors import  CORS
from db import insert_message_details
app = Flask(__name__)
app.config['DEBUG'] = True
CORS(app)

@app.route("/queue",methods=['POST'])
def get_messages():
    data = request.get_json()
    print(data)
    message = data.get("message","").strip()
    destination = data.get("destination","").strip()
    origin = data.get("origin","").strip()
    response = insert_message_details(message,destination,origin)
    return response




if __name__ == '__main__':
    app.run(debug=True)