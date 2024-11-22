from gtts import gTTS
import os

from flask import Flask, render_template,request,redirect,url_for
import time

app = Flask(__name__)

def move_to_static(name_of_file):
    main_file = open("speech.mp3", "rb").read()
    dest_file = open('/home/lonewolfTech/mysite/static/speech.mp3', 'wb+')
    dest_file.write(main_file)
    dest_file.close()
    #os.remove('speech.mp3')

def text_to_speech(text):
    speech = gTTS(text)
    speech.save('speech.mp3')

@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        text = request.form['text1']
        text_to_speech(text)
        move_to_static('speech.mp3')
        return redirect(url_for('output'))
    else:
        return render_template("index.html")


@app.route("/output")
def output():
    return render_template("output.html")
"""
@app.route('/')
def home():
    return render_template("index.html")
"""
if __name__ == "__main__":
    app.run()
