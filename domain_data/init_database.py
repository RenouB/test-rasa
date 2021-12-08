from sqlalchemy import create_engine
from alembic.models import Gemuese
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://renou:password@localhost:5432/testrasa')
Session = sessionmaker(bind=engine)
session = Session()

gemuese = [
    {"veg_type":"Moehren", "variety":"gelb", "length":4, "price":2.99},
    {"veg_type":"Moehren", "variety":"orange", "length":15, "price":1.99},
    {"veg_type":"Moehren", "variety":"schwarz", "length":10, "price":3.99}
]

for gemuese_ in gemuese:
    g = Gemuese(**gemuese_)
    session.add(g)
session.commit()

