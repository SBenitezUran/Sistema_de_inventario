from sqlalchemy import Column, ForeignKey, Integer

from config.database import Base


class Supplies(Base):

    __tablename__ ="supplies"

    id = Column(Integer, primary_key=True)
    Product_ID = Column(str, ForeignKey("Product.ID"))
    Supplier_ID = Column(Integer, ForeignKey("Supplier_ID"))
    Purchase_Price = Column(Integer)