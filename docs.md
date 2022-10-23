heroku run python
from app import db
db.create_all()

heroku run bash
$ flask db stamp head
$ flask db migrate
$ flask db upgrade