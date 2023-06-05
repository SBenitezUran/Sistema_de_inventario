from pydantic import BaseModel, Field
from typing import Optional 

class Product(BaseModel):
        id: Optional[int] = None
        Name: str = Field(max_length=15,min_length=3)
        Brand: str = Field(max_length=15,min_length=3)
        Description: str = Field(max_length=400,min_length=3)
        Price: int = Field(ge=1)
        Entry_Date : str = Field(max_length=15,min_length=3)
        availability: str = Field(max_length=15,min_length=3)
        Available_Quantity: int = Field(ge=1)

        class Config:
            schema_extra = {
                "example":{
                    'id': 1,
                    'Name': 'Any',
                    'Brand': "Mattelsa",
                    'Description':"In this clothing store you can find your favorite clothes...",
                    'Price': 80000,
                    'Entry_Date':"20/02/2023",
                    'availability':'available',
                    "Available_Quantity" : 100,
                }
            }

