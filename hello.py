from flask import Flask
app = Flask(__name__)
@app.route("/")#URL leading to method
def hello(): # Name of the method
 return("Hello World!") #indent this line
if __name__ == "__main__":
 app.run(host='20.123.82.3', port='8080') # indent this line
