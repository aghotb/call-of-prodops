from flask import Flask
from flask import request
import sqlite3
from flask import g
DATABASE = 'stupid.db'

app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def init_db():
    with app.app_context():
        db = get_db()
        db.executescript('CREATE TABLE users(user_id int, username varchar(255));')
        db.commit()


@app.route('/user/<name>', methods=['GET', 'POST'])
def user(name):
    if request.method == 'GET':
        u = query_db('select * from users where username = ?', [name], one=True)
        if u is None:
            return 'No such user'
        else:
            return u
    # u = query_db('insert into users(username) values(?)', [name])
    return "created " + str(u)
    # return '<div style="background-color: red">byebye</div>'


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    init_db()
    app.run()
