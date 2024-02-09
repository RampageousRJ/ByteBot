from flask import Flask,request,make_response,jsonify
import os

app = Flask(__name__)
app.config['SECRET_KEY']=os.getenv('CHATBOT_SECRET_KEY')

@app.route('/',methods=['POST'])
def api():
    payload = request.get_json()
    print(payload)
    
    if payload['queryResult']['parameters']['subjects']=='AP':
        return make_response(jsonify({'fulfillmentText':'Your desired resources can be found here! https://github.com/RampageousRJ/CCE-AP-Lab'}))
    
    elif payload['queryResult']['parameters']['subjects']=='NDP':
        return make_response(jsonify({'fulfillmentText':'Your desired resources can be found here! https://github.com/RampageousRJ/CCE-NDP-Lab'}))
    
    elif payload['queryResult']['parameters']['subjects']=='DMPA-L':
        return make_response(jsonify({'fulfillmentText':'Your desired resources can be found here! https://github.com/RampageousRJ/CCE-DMPA-Lab'}))
    
    elif payload['queryResult']['parameters']['subjects']=='OS-L':
        return make_response(jsonify({'fulfillmentText':'Your desired resources can be found here! https://github.com/RampageousRJ/CCE-OS-Lab'}))
    
    elif payload['queryResult']['parameters']['subjects']=='EOM':
        return make_response(jsonify({"fulfillmentText": "Your desired resources can be found here!   http://tinyurl.com/ZippedEOM"}))
    
    elif payload['queryResult']['parameters']['subjects']=='SDT':
        return make_response(jsonify({"fulfillmentText": "Your desired resources can be found here!   http://tinyurl.com/ZippedSDT"}))
    
    elif payload['queryResult']['parameters']['subjects']=='NPACN':
        return make_response(jsonify({"fulfillmentText": "Your desired resources can be found here!   http://tinyurl.com/ZippedNPACN"}))
    
    elif payload['queryResult']['parameters']['subjects']=='IS':
        return make_response(jsonify({"fulfillmentText": "Your desired resources can be found here!   http://tinyurl.com/ZippedIS"}))
    
    elif payload['queryResult']['parameters']['subjects']=='DMPA':
        return make_response(jsonify({"fulfillmentText": "Your desired resources can be found here!   http://tinyurl.com/ZippedDMPA"}))
    
    return make_response(jsonify({'fulfillmentText':'Sorry! The resource you are looking for is not available!'}))

if __name__=='__main__':
    app.run(debug=1)