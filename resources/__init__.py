from flask import make_response,jsonify

semester_subject = {
    3:{'Object Oriented Programming','Data Structures','Principles of Data Communication','Digital Systems and Computer Organisation','Engineering Mathematics-III','Digital Systems Design Lab','Data Structures Lab','Object Oriented Programming Lab'}, 
    4:{'Database Systems','Design and Analysis of Algorithms','Operating Systems','Engineering Mathematics-IV','Computer Network Protocols','Operating Systems Lab','Database Systems Lab','Algorithms Lab'}, 
    5:{'Advanced Programming','Data Mining and Predictive Analysis','Data Mining and Predictive Analysis Lab','Information Security','Network Design and Programming','Network Programming and Advanced Communication Networks','Software Design Technology','Essentials of Management'}, 
    6:{'Wireless Communication and Computing','Embedded Systems Design','Embedded Systems Design Lab','Mobile Application Development Lab','Network Simulation Lab','Engineering Economics and Financial Management'}
}

semester_subject_short = {
    3:{'OOP','DS','PDC','DSCO','EM3','DSD-L','DS-L','OOP-L'}, 
    4:{'DBS','DAA','OS','EM4','CNP','OS-L','DBS-L','AL'}, 
    5:{'AP','DMPA','DMPA-L','IS','NDP','NPACN','SDT','EOM'}, 
    6:{'WCC','ESD','ESD-L','MAD','NS','EEFM'}
}

def resource_provision(payload):  
    subject = payload['queryResult']['parameters']['subjects'] 
    semester = int(payload['queryResult']['outputContexts'][0]['parameters']['semester'])
    if subject in semester_subject_short[semester]:
        if subject =='AP':
            return make_response(jsonify({'fulfillmentText':'Your desired resources can be found here! https://github.com/RampageousRJ/CCE-AP-Lab'}))
        elif subject=='NDP':
            return make_response(jsonify({'fulfillmentText':'Your desired resources can be found here! https://github.com/RampageousRJ/CCE-NDP-Lab'}))
        elif subject=='DMPA-L':
            return make_response(jsonify({'fulfillmentText':'Your desired resources can be found here! https://github.com/RampageousRJ/CCE-DMPA-Lab'}))
        elif subject=='DBS-L':
            return make_response(jsonify({'fulfillmentText':'Your desired resources can be found here! https://github.com/PHOENIX00710/DBS-LAB_Codes-IT_CCE-MIT_Manipal'}))
        elif subject=='OS-L':
            return make_response(jsonify({'fulfillmentText':'Your desired resources can be found here! https://github.com/RampagousRJ/CCE-OS-Lab'}))
        elif subject=='AL':
            return make_response(jsonify({'fulfillmentText':'Your desired resources can be found here! https://github.com/RampagousRJ/CCE-AL-Lab'}))
        elif subject=='DS-L':
            return make_response(jsonify({'fulfillmentText':'Your desired resources can be found here! https://github.com/RampagousRJ/CCE-DS-Lab'}))
        elif subject=='OOP-L':
            return make_response(jsonify({'fulfillmentText':'Your desired resources can be found here! https://github.com/RampagousRJ/CCE-OOP-Lab'}))
        elif subject=='EOM':
            return make_response(jsonify({"fulfillmentText": "Your desired resources can be found here!   http://tinyurl.com/ZippedEOM"}))
        elif subject=='SDT':
            return make_response(jsonify({"fulfillmentText": "Your desired resources can be found here!   http://tinyurl.com/ZippedSDT"}))
        elif subject=='NPACN':
            return make_response(jsonify({"fulfillmentText": "Your desired resources can be found here!   http://tinyurl.com/ZippedNPACN"}))
        elif subject=='IS':
            return make_response(jsonify({"fulfillmentText": "Your desired resources can be found here!   http://tinyurl.com/ZippedIS"}))
        elif subject=='DMPA':
            return make_response(jsonify({"fulfillmentText": "Your desired resources can be found here!   http://tinyurl.com/ZippedDMPA"}))
        elif subject=='CNP':
            return make_response(jsonify({"fulfillmentText": "Your desired resources can be found here!   http://tinyurl.com/ZippedCNP"}))
        elif subject=='DAA':
            return make_response(jsonify({"fulfillmentText": "Your desired resources can be found here!   http://tinyurl.com/ZippedDAA"}))
        elif subject=='EM4':
            return make_response(jsonify({"fulfillmentText": "Your desired resources can be found here!   http://tinyurl.com/ZippedEM4"}))
        elif subject=='DBS':
            return make_response(jsonify({"fulfillmentText": "Your desired resources can be found here!   http://tinyurl.com/ZippedDBS"}))
        elif subject=='OS':
            return make_response(jsonify({"fulfillmentText": "Your desired resources can be found here!   http://tinyurl.com/ZippedOS"}))
    else:
        return make_response(jsonify({'fulfillmentText':'Sorry! The resource does not exist for the given semester...'}))
    return make_response(jsonify({'fulfillmentText':'Sorry! The resource you are looking for is not available!'}))

def subject_list(payload):
    semester = int(payload['queryResult']['outputContexts'][0]['parameters']['semester'])
    print(semester)
    if semester in semester_subject.keys():
        subs = ', '.join(x for x in semester_subject[semester])
        print(subs)
        return make_response(jsonify({'fulfillmentText':f'Subjects available for the SEMESTER {semester} are: {subs}'}))
    return make_response(jsonify({'fulfillmentText':'Sorry! The resources are not available for this semester!'}))