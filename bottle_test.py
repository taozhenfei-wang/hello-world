from bottle import route, run, template
from datetime import datetime

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)
@route('/')
def index(name='time'):
    dt=datetime.now()
    time="{:%Y-%m-%d %H:%M:%S}".format(dt)
    return template('<b>Pi thinks the date/time is: {{t}}</b>',t=time)

@route('/welcome')   
def index():
    return "Welcome !!!"

run(host='localhost', port=8080)