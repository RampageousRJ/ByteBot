from flask import Flask,request,make_response,jsonify
import os

app = Flask(__name__)
app.config['SECRET_KEY']=os.getenv('CHATBOT_SECRET_KEY')

@app.route('/',methods=['POST'])
def api():
    payload = request.get_json()
    print(payload)
    return make_response(jsonify({'fulfillmentText':'https://github.com/RampageousRJ/CCE-AP-Lab'}))

if __name__=='__main__':
    app.run(debug=1)