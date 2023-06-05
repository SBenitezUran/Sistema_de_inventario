from pydantic import BaseModel, Field
from typing import Optional 

class Supplier(BaseModel):
        id: Optional[int] = None
        Name: str = Field(max_length=15,min_length=3)
        Address: int = Field(ge=1)
        Phone: int = Field(ge=1)
        Email : str  = Field(max_length=15,min_length=3)
        

        class Config:
            schema_extra = {
                "example":{
                    'id': 1,
                    'Name': 'Any',
                    'Address': 41-83,
                    'Phone':3104098026,
                    'Email':"santiagobenite467@gmail.com",
                    
                }
            }
