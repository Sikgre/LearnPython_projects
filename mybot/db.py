from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgres://pdqngskc:zIgbbTBbaqaLZw4ncHpu_pqqZ8GqeImZ@hattie.db.elephantsql.com:5432/pdqngskc")
db_session = scoped_session(sessionmaker(bind = engine))

base = declarative_base()
base.query = db_session.query_property()