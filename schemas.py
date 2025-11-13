from pydantic import BaseModel
from typing import Optional



class SignUpModel(BaseModel):
    id: Optional[int]
    username: str
    email: str
    password: str
    is_staff: Optional[bool] = False
    is_active: Optional[bool] = True


    class Config:
        orm_mode = True
        schema_extra = {
            'example':{
                "username":"latif",
                "email":"example@email.com",
                "password":"password",
                "is_staff":False,
                "is_active":True
            }
        }


class Setting(BaseModel):
    authjwt_secret_key:str='02b283c3e65f6a8aada2d5853d963c516b36fd94997064d74c362fec8860b0f3'


class LoginModel(BaseModel):
    username:str
    password:str



class OrderModel(BaseModel):
    id: Optional[int]
    quantity: int
    order_status: Optional[str] = "PENDING"
    pizza_size:Optional[str] = "SMALL"
    flavour: str = "PEPPERONI"
    user_id:Optional[int]

    class config:              
        orm_model = True
        schema_extra={
            "example":{
                "quantity":2,
                "pizza_size":"LARGE",
                "flavour":"PEPPERONI"
            }
        }

class OrderStatusModel(BaseModel):
    order_status:Optional[str]="PENDING"

    class Config:
        orm_mode = True
        schema_extra = {
            "example":{
                "order_status":"PENDING"
            }
        }