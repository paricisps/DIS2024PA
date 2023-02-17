from flask import Flask  # importing the Flask class from the flask library

app = Flask(__name__)  # creating an instance of this class

@app.route('/')  # default route

def hello_form():    return "<h1>Hello, this is a form!</h1>"

#if __name__ == '__main__':
    #app.run(debug=True)
