from sqlalchemy.orm import Session

from models import BaseModel
from schemas import schem_Crate

def create_crate(db: Session, crate: schem_Crate.CrateCreate, product_id: int, order_id: int, user_id: int):

    db_crate = BaseModel.Crate(**crate.dict())
    db.add(db_crate)
    db.commit()
    db.refresh(db_crate)
    return db_crate


def get_crate(db: Session, crate_id: int):

    return db.query(BaseModel.Crate).filter(BaseModel.Crate.id == crate_id).first()

def get_crates_by_user_id(db: Session, user_id: int):

    return db.query(BaseModel.User).filter(BaseModel.User.id == user_id).all()

def get_crates_by_order_id(db: Session, order_id: int):

    return db.query(BaseModel.Order).filter(BaseModel.Order.id == order_id).all()

def get_crates_by_product_id(db: Session, product_id: int):

    return db.query(BaseModel.Product).filter(BaseModel.Product.id == product_id).all()

def read_crates(db: Session, limit: int = 100, skip: int = 0):

    return db.query(BaseModel.Crate).limit(limit).offset(skip).all()

def delete_crate(db: Session, crate_id: int):

    crate = db.query(BaseModel.Crate).filter(BaseModel.Crate.id == crate_id).first()
    db.delete(crate)
    db.commit()
    return crate