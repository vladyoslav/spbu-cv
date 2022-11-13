import sys

from flask import Flask, render_template, request

from config import SQLALCHEMY_DATABASE_URI, PORT
from models import Comment, db, init_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db.init_app(app)
init_db(app)


@app.route('/')
def index():
    comments = Comment.query.all()

    return render_template('index.html', comments=comments[::-1])


@app.post('/comment')
def comment():
    comment = Comment(
        name=request.form['name'],
        text=request.form['text']
    )

    db.session.add(comment)
    db.session.commit()

    return 'OK'


if __name__ == '__main__':

    if len(sys.argv) > 1:
        if sys.argv[1] == 'init':
            init_db(app, reset=True)
    else:
        app.run(port=PORT)
