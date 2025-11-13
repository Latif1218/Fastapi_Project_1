from fastapi import APIRouter,Depends, status
from fastapi.exceptions import HTTPException
from fastapi_jwt_auth import AuthJWT
from models import User, Order
from schemas import OrderModel, OrderStatusModel
from database import Session, engine
from fastapi.encoders import jsonable_encoder

order_router = APIRouter(
    prefix="/orders",
    tags=['orders']
)

session=Session(bind=engine)

@order_router.get('/')
async def hello(Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Tnvalid Token"
        )
    return {"massage" : "hello world"}


@order_router.post('/order',status_code=status.HTTP_201_CREATED)
async def place_an_order(order:OrderModel,Authorize:AuthJWT=Depends()):

    try:
        Authorize.jwt_required()

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    curent_user = Authorize.get_jwt_subject()

    user=session.query(User).filter(User.username==curent_user).first()

    new_order = Order(
        pizza_size = order.pizza_size,
        quantity = order.quantity
    )

    new_order.user = user

    session.add(new_order)

    session.commit()


    response = {
        "pizza_size":new_order.pizza_size,
        "quantity":new_order.quantity,
        "id":new_order.id,
        "order_status":new_order.order_status,
        "flavour":new_order.flavour
    }

    return jsonable_encoder(response)





@order_router.get('/orders')
async def list_all_orders(Authorize:AuthJWT=Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    
    current_user=Authorize.get_jwt_subject()

    user = session.query(User).filter(User.username==current_user).first()

    if user.is_staff:
        orders=session.query(Order).all()

        return jsonable_encoder(orders)
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="you are not a superuser"
    )