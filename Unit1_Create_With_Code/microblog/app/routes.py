
from app import app
from flask import render_template


#@app.route('/')  # default route
#def default():
    #return '<h2>Hello</h2>'

@app.route('/')
@app.route('/index')  # index route
def index():
    user = {'username': 'Peyton'}
    posts = [
        {
            'author': {'username': 'Fred'},
            'body': 'Beautiful day in Brisbane!'
         },
        {
            'author': {'username': 'Wilma'},
            'body': 'Basketball is the best sport!'
        },
        {
            'author': {'username': 'person'},
            'body': 'Basketball is the worst'
        }
    ]
    return render_template('index.html', title=user['username'], user=user,posts=posts)