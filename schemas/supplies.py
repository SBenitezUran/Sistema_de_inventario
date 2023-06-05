from pydantic import BaseModel, Field

from typing import Optional

class  Supplies(BaseModel):
   id : Optional[int] = None
   Supplier_ID :int = Field(ge=1, description="ForeignKey Supplier")
   Product_ID :int= Field(ge=1, description="ForeingKey Product")
   Purchase_Price : int = Field(ge=1)

   class Config:
        schemas_extra = {
            "example":{
                "Supplier_ID":2,
                "ProducT_ID":3,
                "Purchase_Price":4
                
            }
        }