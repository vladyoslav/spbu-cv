import shutil
from datetime import datetime
from pathlib import Path

import sqlalchemy as sa
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

from config import DATABASE_FOLDER, SQLITE_DATABASE_NAME, SQLITE_DATABASE_BACKUP_NAME

import pytz

db = SQLAlchemy()


class Comment(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(64), nullable=False)
    text = sa.Column(sa.String(512), nullable=False)
    created_at = sa.Column(sa.DateTime(), default=datetime.now().astimezone(pytz.timezone('Europe/Moscow')))


comments = [
    {'name': 'Амогус', 'text': 'Это тестовый текст тестового комментария для тестирования тестов'},
]

def init_db(app, reset=False):
    # Check if db file already exists. If so, backup it
    db_file = Path(f'{DATABASE_FOLDER}/{SQLITE_DATABASE_NAME}')

    if db_file.is_file():
        if reset:
            shutil.copyfile(f'{DATABASE_FOLDER}/{SQLITE_DATABASE_NAME}', f'{DATABASE_FOLDER}/{SQLITE_DATABASE_BACKUP_NAME}')
        else:
            return

    with app.app_context():
        # Init DB
        db.session.commit()
        db.drop_all()
        db.create_all()

        # Create default comments
        print("Create default comments")
        for c in comments:
            print(c)
            comment = Comment(name=c['name'], text=c['text'])
            db.session.add(comment)
            db.session.commit()
