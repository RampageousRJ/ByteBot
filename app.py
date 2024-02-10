from flask import Flask,request,make_response,jsonify
from resources import *
import os

app = Flask(__name__)
app.config['SECRET_KEY']=os.getenv('CHATBOT_SECRET_KEY')

@app.route('/',methods=['POST'])
def api():
    payload = request.get_json(force=True)
    # print(payload)
    
    if payload['queryResult']['intent']['displayName']=='resource-intent':    
        return resource_provision(payload)
    
    if payload['queryResult']['intent']['displayName']=='subject-list-intent':    
        return subject_list(payload)

if __name__=='__main__':
    app.run(debug=1)
    
    
    