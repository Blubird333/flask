#https://flask.palletsprojects.com/en/2.0.x/

from flask import Flask

app = Flask("Job site")

@app.route("/")                       #decorater(mainly used to make this python file as a flask file.)
def hello():
    return "Hi! I'm here!\n"


#Steps to run this for flask:
#save this file.
#type 'export FLASK_APP=main' and hit enter in the terminal.
#type 'flask run' and hit enter in the terminal.
