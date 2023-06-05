from sqlalchemy import Column, ForeignKey, Integer

from config.database import Base


class Supplies(Base):

    __tablename__ ="supplies"

    id = Column(Integer, primary_key=True)
    Supplier_ID = Column(Integer, ForeignKey("supplier.id"))
    Product_ID = Column(Integer, ForeignKey("product.id"))
    Purchase_Price = Column(Integer)
    
     