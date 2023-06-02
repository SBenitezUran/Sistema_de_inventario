from sqlalchemy import Column, Integer, String

from config.database import Base


class Supplier(Base):

    __tablename__ ="supplies"

    id = Column(Integer, primary_key=True)
    Name = Column(String)
    Address = Column(Integer)
    Phone = Column(Integer)
    Email = Column(String)
   