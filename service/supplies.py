from models.supplies import Supplies as SuppliesModel
from schemas.supplies import Supplies 

class SuppliesService():
    def __init__(self, db):
        self.db = db
        
    def get_supplies(self):
        result = self.db.query(SuppliesModel).all()
        return result
    
    def  create_supplies(self,supplies:SuppliesModel):
        new_supplies = SuppliesModel(
            Supplier_ID = supplies.Supplier_ID,
            Product_ID = supplies.Product_ID,
            Purchase_Price = supplies.Purchase_Price,
            
        )
        self.db.add(new_supplies)
        self.db.commit()
        return
    
    def get_for_id(self,id:int):
        result = self.db.query(SuppliesModel).filter(SuppliesModel.id == id). first()
        return result
    
    def update_supplies(self,data):
        supplies = self.db.query(SuppliesModel).filter(SuppliesModel.id == data.id). first()
        supplies.Supplier_Id = data.Supplier_ID
        supplies.Product_ID = data.Product_ID
        supplies.Purchase_Price = data.Purchase_Price 
        self.db.commit()
        return
    
    def delete_supplies(self,id:int):
        self.db.query(SuppliesModel).filter(SuppliesModel.id == id).delete()
        self.db.commit()
        return
    