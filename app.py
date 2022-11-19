from flask import Flask, jsonify, request
# from flask_mysqldb import MySQL
from twilio.rest import Client
from crop_recommendation.corp_prediction import recommend_crop
# import boto3 
# from botocore.client import Config
from crop_recommendation.weather import weather_fetch
# from gtts import gTTS
import os
import utils
import numpy as np
from config import config
from farmers_log.search_user_request import search_log
from farmers_log.summarize_log import xlnet_summarizer
from utils import response_payload
import pickle
from config import config, ACCESS_KEY_ID, ACCESS_SECRET_KEY, BUCKET_NAME


app = Flask(__name__)

# conexion = MySQL(app)


#The thelephone number associated whit the twilio account is: 
# --------> +240222313788
# The titles of the topics stored in the database are:
    # Nutrition
    # Fertilizantes
    # Cultivation
    # Harvest

@app.route("/test", methods = ["GET"])
def test():
    return response_payload(True, "Hello World")

@app.route("/farmers-log", methods = ["POST"])
def farmers_log():
    try:
        data = request.get_json()
    except Exception:
        response_payload(False, msg="Request body could not be found")
    if not data:
        return response_payload(False, msg="No data provided")
    log = data.get("log")
    if not log:
        return response_payload(False, msg="No log provided")
    search_result = search_log(log)
    return response_payload(True,search_result, "Success search")




@app.route('/crop-recommedation', methods = ["POST"])
def crop_recommedation():
    try:
        data = request.get_json()
    except Exception:
        response_payload(False, msg="Request body could not be found")
    if not data:
        return response_payload(False, msg="No data provided")
    
    try:
        N = int(data.get('nitrogen'))
        P = int(data.get('phosphorous'))
        K = int(data.get('pottasium'))
        ph = float(data.get('ph'))
        rainfall = float(data.get('rainfall'))
        city = data.get("city")
        
        
        try:
            city_info = weather_fetch(city)
        except Exception:
            return response_payload(False, msg="Unable to get the city information. Please try again")
         
        if city_info != None:
            temperature, humidity = city_info
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            my_prediction = recommend_crop(data)
            recommendation_result = {
                    "prediction": my_prediction[0]
                }
            return response_payload(True, recommendation_result, "Success search")
        else:
            return response_payload(False, 'Please try again') 
        
        
    except Exception:
        return response_payload(False, msg="Request body is not valid")


# @app.route('/find_response/<phone_number>/<message_body>', methods=['GET','POST'])
# def find_response(phone_number,message_body):
#     try:
#         cursor=conexion.connection.cursor()
#         sql="SELECT content FROM topics WHERE topic_title = '{0}'".format(message_body)
#         cursor.execute(sql)
#         resp=cursor.fetchone()
#         if resp != None:
#             response = resp[0]
            
            
#             # Convert text to audio
#             mytext = response
#             languaje = "es"
#             myobj = gTTS(text=mytext, lang=languaje, slow=False)
#             myobj.save("response.mp3")   
            
#             # Send the audio in to bucket
#             s3 = boto3.resource(
#             's3',
#             aws_access_key_id = ACCESS_KEY_ID,
#             aws_secret_access_key = ACCESS_SECRET_KEY,
#             config=Config(signature_version='s3v4')
#             )
#             data = open('response.mp3', 'rb')
#             s3.Bucket(BUCKET_NAME).put_object(Key='response.mp3', Body=data, ContentType='audio/mp3')      
            
#             s3_url = f"https://{BUCKET_NAME}.s3.{'us-east-1'}.amazonaws.com/{'response.mp3'}"
            
#             # Send sms
#             def sms_response(phone_number,response, s3_url):
#                 account_sid = "ACa14fbcbce98e84a08d6a60bbdebbf18b"
#                 auth_token = "9a9bf0f756d4d38fcbb305e252c27f4a"

                
#                 client = Client(account_sid, auth_token)
#                 message = client.messages.create(
#                     body = response + " " + "Abra el siguiente enlace para escuchar la respuesta " +  s3_url,
#                     from_ = "+19452392171", 
#                     to = phone_number        
#                 )
#             try:
#                 sms_response(phone_number, response, s3_url)
#             except Exception as ex:
#                 return jsonify({'message':"Check your internet conection."})
            
                
#             return jsonify({ 'Abra el siguiente enlace para escuchar la respuesta': s3_url,  'message':response,'topic':"Topic found."})
#         else:    
#             return jsonify({'message':"Topic not found."})
#     except Exception as ex:
#         return jsonify({'message':"Error"})
        


def page_not_found(error):
    return "<h1> Page not found ...", 404
      

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, page_not_found)
    app.run()
    
    
    