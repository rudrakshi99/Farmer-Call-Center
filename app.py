from flask import Flask, jsonify
from flask_mysqldb import MySQL
from twilio.rest import Client

import utils

from config import config

app = Flask(__name__)

conexion = MySQL(app)


#The thelephone number associated whit the twilio account is: 
# --------> +240222139113
# The titles of the topics stored in the database are:
    # Nutrition
    # Fertilizers
    # Cultivation
    # Harvest

    

@app.route('/find_response/<phone_number>/<message_body>', methods=['GET','POST'])
def find_response(phone_number,message_body):
    try:
        cursor=conexion.connection.cursor()
        sql="SELECT content FROM topics WHERE topic_title = '{0}'".format(message_body)
        cursor.execute(sql)
        data=cursor.fetchone()
        if data != None:
            response = data
            
            
            def sms_response(phone_number,response):
                account_sid = "AC06e69898844aa7fb0f8790830b8fde17"
                auth_token = "352f7b01b9d0aa47b3276114f8a13f60"

                
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                    body = response,
                    from_ = "+18159576078", 
                    to = phone_number
                )
            try:
                sms_response(phone_number, response)
            except Exception as ex:
                return jsonify({'message':"Check your internet conection."})
            
            return jsonify({'topic':response, 'message':"Topic found."})
        else:    
            return jsonify({'message':"Topic not found."})
    except Exception as ex:
        return jsonify({'message':"Error"})
    


def page_not_found(error):
    return "<h1> Page not found ...", 404
      

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, page_not_found)
    app.run()
    
    
    