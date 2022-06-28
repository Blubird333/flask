from flask import Flask
from flask import request

app = Flask("Job site")

items = ["Good day","Hide n seek","bourbon","Parle-G"]

@app.route("/")                       #decorater(mainly used to make this python file as a flask file.)
def hello():
    l = ", ".join(items)
    return f"List of items is : {l}"

@app.route("/add")
def add_item():                       #after opening the webpage, adding '/add' to the link will take me to another page which will function as the following method.
#    items.append("Dark fantasy")     #And by reloading this page, this method will be executed again resulting in addition of the item 'Dark fantasy' to the list 'lis' for everyreload
#    lis = ", ".join(items)           #After reloading many times, the appended items can be viewed in the main page(by removing '/add' from the link).
#    return f"New item is added : 'Dark fantasy'|||List of items : {lis}|||Number of items : {len(items)}"

    #http://127.0.0.1/add?item=x            #When is types a item '"x"' is added into the list 'items'.The type of x should be plain text.
    new_item = request.args.get("item")
    items.append(new_item)
    return f"No. of items in the list : {len(items)}"



#Steps to run this for flask:
#save this file.
#type 'export FLASK_APP=main' and hit enter in the terminal.
#type 'flask run' and hit enter in the terminal.


#Type the following 2 lines in the command line to close the application running through port 5000:
# netstat -ltnp       # list the running ports
# kill -9 <num>       #this is to kill the application.The 'num' can be found in the PID/Program name section, after using the first command.



# kill specific port in my case for django 8000. kill using PID
