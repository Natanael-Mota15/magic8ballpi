from flask import Flask, render_template, request
import picamera
import datetime
import time
import glob
from sense_hat import SenseHat
import random
sense=SenseHat()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')   

@app.route('/Qs', methods=['POST', 'GET'])
def Question(): 
    if request.method == 'POST':
            
        name = request.form['name']    
        num = (random.randrange(1,18))
        reponse = {
            1:("It is certain."),
            2:("It is decidedly so."),
            3:("Without a doubt."),
            4:("Yes - definitely."),
            5:("You may rely on it."),
            6:("As I see it, yes."),
            7:("Outlook good."),
            8:("Most likely."),
            9:("Yes."),
            10:("Signs point to yes."),
            11:("Reply hazy, try again another time."),
            12:("Ask again later."),
            13:("Better not tell you now."),
            14:("Cannot predict now."),
            15:("Concentrate and ask again another time."),
            16:("Don't count on it."),
            17:("My reply is no."),
            18:("My sources say no.")
            }
        display = f'{name},{reponse[num]}'
        sense.show_message((display),text_colour=(0,0,255),scroll_speed=0.05)
    return render_template('Qs.html')

@app.route('/future')
def future():
    num = (random.randrange(1,18))
    reponse2 = {
        1: ("I will put a curse on you, and you shall not pass."),
        2:("Outlook not so good."),
        3: ("You shall have a happy life"),
        4:("You shall have a rich life"),
        5:("You shall die"),
        6:("IDK you future"),
        7: ("You shall have a happy restuarant"),
        8: ("You shall have a pool house"),
        9:"You shall be buried in california",
        10: "you slow",
        11: "You will marry a good woman",
        12:"You shall have a pizza life",
        13:"No sleep to Boston",
        14:"You go to Harvard",
        15: "You shall have a sad but ok life",
        16:"You shall have a poor life",
        17:"You shall die a painful death",
        18:"IDK you future but you look nice(wink wink)",    
        }
    sense.show_message((reponse2[num]),text_colour=(0,0,255),scroll_speed=0.05)
    return render_template('future.html')   
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

    

