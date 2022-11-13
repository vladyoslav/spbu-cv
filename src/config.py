import os
from datetime import datetime

current_data = datetime.now().isoformat().replace(':', '-')

SQLITE_DATABASE_NAME = os.environ.get('SQLITE_DATABASE_NAME') or 'database.db'
SQLITE_DATABASE_BACKUP_NAME = 'backup_' + current_data + '.db'
SQLALCHEMY_DATABASE_URI = f'sqlite:///{SQLITE_DATABASE_NAME}'
DATABASE_FOLDER = os.environ.get('DATABASE_FOLDER') or 'instance'
PORT = os.environ.get('PORT') or 5000
