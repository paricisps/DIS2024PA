
from app import app
from flask import render_template


#@app.route('/')  # default route
#def default():
    #return '<h2>Hello</h2>'

@app.route('/')
@app.route('/index')  # index route
def index():
    user = {'username': 'Fred'}
    return '''
    <html>
        <head>
            <title>Homepage - Microblog</title>
        </head>
        <body>
            <h1> Hello, ''' + user['username'] + '''!</h1>
        </body>
    </html>'''