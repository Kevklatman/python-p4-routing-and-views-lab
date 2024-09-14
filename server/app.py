#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:route>')
def print_string(route):
    print(route)
    return route

@app.route('/count/<int:number>')
def count(number):
    count = '\n'
    for n in range(number):
        count += f'{n}\n'
    return count.rstrip('\n')

@app.route('/math/<int:n1>/<string:operation>/<int:n2>')
def math(n1, operation, n2):
    if operation == '+':
        return str(n1 + n2)
    
    elif operation == '-':
        return str(n1 - n2)

    elif operation == '*':
        return str(n1 * n2)

    elif operation == 'div':
        return str(n1 / n2)

    elif operation == '%':
        return str(n1 % n2)

    return 'Operation not recognized. Please use one of the following: + - * div %'


if __name__ == '__main__':
    app.run(port=5555, debug=True)