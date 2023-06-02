from sqlalchemy import Column, Integer, String

from config.database import Base


class Product(Base):

    __tablename__ ="product"

    id = Column(Integer, primary_key=True)
    Name = Column(String)