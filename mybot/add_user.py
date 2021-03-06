from db import db_session
from models import User

user = User(name = 'Вася', salary = 30000, email = 'vasya@mail.ru')
db_session.add(user)
db_session.commit()