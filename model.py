from pydantic import BaseModel

class product(BaseModel):
    name:str
    price:int
    quantity:int
    reviews:int

