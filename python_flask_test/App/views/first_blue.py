from flask import Blueprint, render_template

first = Blueprint('first', __name__)

# def url_hello(app):
#     @app.route('/')
#     def hello_world():
#         return 'Hello World!'
#
@first.route('/')
def hih():
    return render_template('index.html', name='任磊')

@first.route('/holle/')
def holle():
    return 'hoole'