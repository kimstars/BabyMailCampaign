from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db')

with engine.connect() as conn:
    pass