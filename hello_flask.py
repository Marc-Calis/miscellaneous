# http://flask.pocoo.org
# https://realpython.com/flask-by-example-part-1-project-setup/

# $ pip3 install Flask
# $ FLASK_APP=hello.py flask run
#  * Running on http://localhost:5000/

# terminal: python3 hello_flask.py

#!/usr/bin/env python3
# coding=utf-8

import os.path
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.debug('A value for debugging')
    #app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/hello')
def hello_bis():
    return 'Hello, World'

# http://flask.pocoo.org/docs/1.0/quickstart/#debug-mode

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

# File Uploads
# https://github.com/arendst/Sonoff-Tasmota/wiki/Python-HTTP-OTA-Server
# https://github.com/arendst/Sonoff-Tasmota/blob/development/tools/fw_server/fw-server.py


if __name__ == '__main__':
    app.run(
        host="192.168.201.3", 
        #port="5000"
        )