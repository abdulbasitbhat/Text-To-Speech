from gtts import gTTS
import os
from flask import Flask, render_template,request,redirect,url_for
import time

app = Flask(__name__)

def move_to_static(name_of_file):
    main_file = open(name_of_file, "rb").read()
    dest_file = open('static/speech.mp3', 'wb+')
    dest_file.write(main_file)
    dest_file.close()
    os.remove('speech.mp3')

def text_to_speech(text):
    speech = gTTS(text)
    speech.save('speech.mp3')

@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        text = request.form['text1']
        #Attempt to synchronize but cant
        while(os.path.exists('speech.mp3')):
            continue
        text_to_speech(text)
        move_to_static('speech.mp3')
        return redirect(url_for('output'))  
    else:  
        return render_template("index.html")


@app.route("/output")
def output():
    return render_template("output.html")
 
if __name__ == "__main__":
    app.run()   
