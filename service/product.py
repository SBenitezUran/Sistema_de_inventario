from models.product import Product as ProductModel
from schemas.product import Product


class ProductService():

    def __init__(self,db) -> None:
        self.db = db

    def get_products(self):
        result = self.db.query(ProductModel).all()
        return result

    def get_for_id(self,id:int):
        result = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        return result

    def get_products_by_release_contry(self,release_contry:str):
        result = self.db.query(ProductModel).filter(ProductModel.release_contry == release_contry).all()
        return result        

    def create_product(self, product:Product):
        new_product = ProductModel(
        Name = product.Name,
        Brand = product.Brand,
        Description = product.Description,
        Price = product.Price,
        Entry_Date = product.Entry_Date,
        availability = product.availability,
        Available_Quantity = product.Available_Quantity
        )
        self.db.add(new_product)
        self.db.commit()
        return 

    def update_product(self, data:Product):
        product = self.db.query(ProductModel).filter(ProductModel.id == data.id).first()
        product.Name = data.Name
        product.Brand = data.Brand
        product.Description = data.Description
        product.Price = data.Price
        product.Entry_Date = data.Entry_Date
        product.availability = data.availability
        product.Available_Quantity = data.Available_Quantity 
        self.db.commit()
        return


    def delete_product(self, id: int):
       self.db.query(ProductModel).filter(ProductModel.id == id).delete()
       self.db.commit()
       return


