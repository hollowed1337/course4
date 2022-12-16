from sqlalchemy.orm import Session

from models import BaseModel
from schemas import schem_ProdType

def create_prodtype(db: Session, prodtype: schem_ProdType.ProdTypeCreate):
    
    db_prodtype = BaseModel.ProdType(name=prodtype.name)
    db.add( db_prodtype)
    db.commit()
    db.refresh( db_prodtype)
    return  db_prodtype


def get_prodtype(db: Session, prodtype_id: int):

    return db.query(BaseModel.ProdType).filter(BaseModel.ProdType.id == prodtype_id).first()

def get_prodtype_by_name(db: Session, name: str):

    return db.query(BaseModel.ProdType).filter(BaseModel.ProdType.name == name).first()

def read_prodtypes(db: Session, skip: int, limit: int):
    return db.query(BaseModel.ProdType).limit(limit).offset(skip).all()


def del_prodtype(db: Session, prodtype_id: int):

    del_prodtype = db.query(BaseModel.ProdType).filter(BaseModel.ProdType.id == prodtype_id).first()
    db.delete(del_prodtype)
    db.commit()
    return del_prodtype