#!/usr/bin/env python3
from flask import Flask, request

app = Flask(__name__)

# Component 1: Routing
@app.route('/')
def index():
    # Component 3: Response Handling
    return '''
    <h1>Welcome to my app!</h1>
    <p>Liverpool FC is the greatest club in the world.</p>
    <p>Cristiano Ronaldo is the G.O.A.T</p>
    '''

# Component 1: Routing
@app.route('/<string:username>')
def user(username):
    # Component 3: Response Handling
    return f'<h1>Profile for {username}</h1>'

if __name__ == '__main__':
    # Component 7: Running the Development Server
    app.run(port=5555, debug=True)
