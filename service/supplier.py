from models.supplier import Supplier as SupplierModel
from schemas.supplier import Supplier


class SupplierService():

    def __init__(self,db) -> None:
        self.db = db

    def get_supplier(self):
        result = self.db.query(SupplierModel).all()
        return result

    def get_supplier(self,id:int):
        result = self.db.query(SupplierModel).filter(SupplierModel.id == id).first()
        return result

    def get_supplier_by_release_contry(self,release_contry:str):
        result = self.db.query(SupplierModel).filter(SupplierModel.release_contry == release_contry).all()
        return result        

    def create_supplier(self, supplier:Supplier):
        new_supplier = SupplierModel(
        Name = supplier.Name,
        Address = supplier.Address,
        Phone = supplier.Phone,
        Email = supplier.Email,

        )
        self.db.add(new_supplier)
        self.db.commit()
        return 

    def update_supplier(self,id:int, data:Supplier):
        supplier = self.db.query(SupplierModel).filter(SupplierModel.id == id).first()
        supplier.Name = data.Name
        supplier.Address = data.Address
        supplier.Phone = data.Phone
        supplier.Email = data.Email
        self.db.commit()
        return


    def delete_supplier(self, id: int):
       self.db.query(SupplierModel).filter(SupplierModel.id == id).delete()
       self.db.commit()
       return


