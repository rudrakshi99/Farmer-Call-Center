from flask import Flask, redirect, url_for, render_template, request, flash
from twilio import twiml
from twilio.rest import Client
from flaskext.mysql import MySQL
import pymysql



app = Flask(__name__)
app.secret_key = "Geeks_On_FIre"
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'geeks_on_fire'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# Index
@app.route('/', methods=['POST','GET'])
def index ():
    
    return render_template ('index.html')

# Send sms
@app.route('/find_response', methods=['POST','GET'])
def find_response ():
    
    if request.method == 'POST':
    
        phone_number= request.form['number']
        message_body = request.form['message']
      
    try:    
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT content FROM topics WHERE topic_title=%s",(message_body,))
        data = cursor.fetchone()
        conn.close()  
        data = list(data.values())
        
        response = data[0]
        
        print(response)

    except:
        if data == None:
            flash("Not found.")
            return redirect(url_for('index'))

    def sms_response(response, phone_number):
            
        ## Twilio account
        account_sid = "AC06e69898844aa7fb0f8790830b8fde17"
        auth_token = "352f7b01b9d0aa47b3276114f8a13f60"
        ##

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body = response,
            from_ = "+18159576078", 
            to = phone_number
        )

    sms_response(response, phone_number)
    flash("A message whit the answer was sent to your phone.")
    return redirect(url_for('index'))
        

if __name__ == '__main__':
    app.run(debug=True)
