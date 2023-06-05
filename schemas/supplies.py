from pydantic import BaseModel, Field

from typing import Optional

class  Supplies(BaseModel):
   id : Optional[int] = None
   Supplier_ID :int = Field(ge=1, description="ForeignKey Supplier")
   Product_ID :int= Field(ge=1, description="ForeingKey Product")
   Purchase_Price : int = Field(ge=1,le=50000)

   class Config:
        schemas_extra = {
            "example":{
                "Supplier_ID":0,
                "Product_ID":0,
                "Purchase_Price":40
                
            }
        }