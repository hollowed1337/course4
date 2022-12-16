from sqlalchemy.orm import Session
from datetime import  datetime
from models import BaseModel
from schemas import schem_Order

def create_order(db: Session, order: schem_Order.OrderCreate):

    order_date = datetime.now()
    db_order = BaseModel.Order(**order.dict(), date=order_date)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, order_id: int):

    return db.query(BaseModel.Order).filter(BaseModel.Order.id == order_id).first()

def get_orders_by_user(db: Session, user_id: int):

    return db.query(BaseModel.User).filter(BaseModel.User.id == user_id).all()

def get_orders_by_product(db: Session, product_id: int):

    return db.query(BaseModel.Product).filter(BaseModel.Product.id == product_id).all()

def get_order_by_order_num(db: Session, order_num: int):

    return db.query(BaseModel.Order).filter(BaseModel.Order.order_num == order_num).first()

def read_orders(db: Session, skip: int = 0, limit: int = 100):

    return db.query(BaseModel.Order).limit(limit).offset(skip).all()


def delete_order(db: Session, order_id: int):

   db_order =  db.query(BaseModel.Order).filter(BaseModel.Order.id == order_id).first()
   db.delete(db_order)
   db.commit()
   return db_order


def edit_order(db: Session,  order_id: int, order: schem_Order.OrderUpdate):

    db.query(BaseModel.Order).filter(BaseModel.Order.id == order_id).update(
        {BaseModel.Order.name: order.name,
        BaseModel.Order.order_num: order.order_num,
        BaseModel.Order.price: order.price,
        BaseModel.Order.order_status: order.order_status}, synchronize_session="fetch"
    )
    db.commit()
    #db.refresh(db_order)
    return db.query(BaseModel.Order).filter(BaseModel.Order.id == order_id).first()
