from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/user/<name>', methods=['GET', 'POST'])
def user(name):
    if request.method == 'GET':
        return name
    else:
        return "created " + name
    # return '<div style="background-color: red">byebye</div>'


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
