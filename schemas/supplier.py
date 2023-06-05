from pydantic import BaseModel, Field
from typing import Optional 

class Supplier(BaseModel):
        id: Optional[int] = None
        Name: str = Field(max_length=40,min_length=3)
        Address: str = Field(max_length=300,min_length=3)
        Phone: int = Field(ge=1)
        Email : str  = Field(max_length=300,min_length=3)
        

        class Config:
            schema_extra = {
                "example":{
                    'id': 1,
                    'Name': 'Any',
                    'Address':"Medellin",
                    'Phone':3104098026,
                    'Email':"santiagobenite467@gmail.com",
                    
                }
            }
