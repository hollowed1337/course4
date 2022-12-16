from sqlalchemy.orm import Session
from models import BaseModel
from schemas import schem_Role

def create_role(db: Session, role: schem_Role.RoleCreate):

    db_role = BaseModel.Role(name=role.name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


def get_role(db: Session, role_id: int):

    return db.query(BaseModel.Role).filter(BaseModel.Role.id == role_id).first()

def get_roles_by_name(db: Session, name: str):

    return db.query(BaseModel.Role).filter(BaseModel.Role.name == name).all()

def read_roles(db: Session, skip: int = 0, limit: int = 100):

    return db.query(BaseModel.Role).offset(skip).limit(limit).all()

def delete_role(db: Session, role_id: int):

    role =  db.query(BaseModel.Role).filter(BaseModel.Role.id == role_id).first()
    db.delete(role)
    db.commit()
    return role