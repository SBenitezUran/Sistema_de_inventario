from pydantic import BaseModel, Field
from typing import Optional 

class Movie(BaseModel):
        id: Optional[int] = None
        Name: str = Field(max_length=15,min_length=3)
        Brand: str = Field(max_length=15,min_length=3)
        Description: str = Field(max_length=40,min_length=10)
        Price: int = Field(ge=1)
        Entry_Date : int  = Field(ge=1)
        availability: str = Field(max_length=15,min_length=3)
        Available_Quantity: str = Field(max_length=15,min_length=3)

        class Config:
            schema_extra = {
                "example":{
                    'id': 1,
                    'Name': 'Any',
                    'Brand': "Mattelsa",
                    'Description':"In this clothing store you can find your favorite clothes...",
                    'Price': 80.000,
                    'Entry_Date':5/6/2023,
                    'availability':'available',
                    "Available_Quantity" : 100,
                }
            }

