from sqlalchemy import Column, ForeignKey, Integer

from config.database import Base


class Supplies(Base):

    __tablename__ ="supplies"

    id = Column(Integer, primary_key=True)
    Produc_ID = Column(Integer, ForeignKey("Product.ID"))
    Supplies_ID = Column(Integer, ForeignKey("Supplies_ID"))
    Purchase_Price = Column(Integer)