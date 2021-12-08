from sqlalchemy import Column, DateTime, String, Integer, Float, func  
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Gemuese(Base):  
    __tablename__ = 'gemuese'
    id = Column(Integer, primary_key=True)
    veg_type = Column(String)
    variety = Column(String)
    length = Column(Integer)
    price = Column(Integer)

    def __repr__(self):
        return 'id: {}, veg_type: {} variety: {}'.format(self.veg_type, self.variety)

class Events(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    sender_id = Column(String(255), nullable=False)
    type_name = Column(String(255), nullable=False)
    timestamp = Column(Float)
    intent_name = Column(String(255))
    action_name = Column(String(255))
    data = Column(String)

    def __repr__(self):
        return 'id: {}, sender_id {}, intent_name, {}, action_name {}'.format(self.id,
                self.sender_id, self.intent_name, self.action_name)