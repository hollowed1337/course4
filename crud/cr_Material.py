from sqlalchemy.orm import Session

from models import BaseModel
from schemas import schem_Material

def create_material(db: Session, material: schem_Material.MaterialCreate):
    
    db_material = BaseModel.Material(name=material.name)
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material


def get_material(db: Session, material_id: int):

    return db.query(BaseModel.Material).filter(BaseModel.Material.id == material_id).first()

def get_material_by_name(db: Session, name: str):

    return db.query(BaseModel.Material).filter(BaseModel.Material.name == name).first()

def read_materials(db: Session, skip: int, limit: int):
    return db.query(BaseModel.Material).limit(limit).offset(skip).all()


def delete_material(db: Session, material_id: int):

    del_material = db.query(BaseModel.Material).filter(BaseModel.Material.id == material_id).first()
    db.delete(del_material)
    db.commit()
    return del_material