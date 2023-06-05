from models.product import Product as ProductModel
from schemas.product import Product


class ProductService():

    def __init__(self,db) -> None:
        self.db = db

    def get_product(self):
        result = self.db.query(ProductModel).all()
        return result

    def get_product(self,id:int):
        result = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        return result

    def get_product_by_release_contry(self,release_contry:str):
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
        Available_Quantiry = product.Available_Quantiry
        )
        self.db.add(new_product)
        self.db.commit()
        return 

    def update_product(self,id:int, data:Product):
        product = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        product.Name = data.Name
        product.Brand = data.Brand
        product.Description = data.Description
        product.Price = data.Price
        product.Entry_Date = data.Entry_Date
        product.availability = data.availability
        product.Available_Quantiry = data.Available_Quantiry 
        self.db.commit()
        return


    def delete_product(self, id: int):
       self.db.query(ProductModel).filter(ProductModel.id == id).delete()
       self.db.commit()
       return


