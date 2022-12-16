from sqlalchemy.orm import Session
from datetime import  datetime
from models import BaseModel
from schemas import schem_Product


def create_product(db: Session, product: schem_Product.ProductCreate, image_id: int, material_id:int, prodtype_id: int):

    db_product = BaseModel.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_product(db: Session, product_id: int):

    return db.query(BaseModel.Product).filter(BaseModel.Product.id == product_id).first()

def get_products_by_material(db: Session, material_id: int):

    return db.query(BaseModel.Product).filter(BaseModel.Material.id == material_id).all()

def get_products_by_prodtype(db: Session, prodtype_id: int):

    return db.query(BaseModel.Product).filter(BaseModel.ProdType.id == prodtype_id).all()

def get_products_by_img(db: Session, img_id: int):

    return db.query(BaseModel.Product).filter(BaseModel.Image.id == img_id).all()

def read_products(db: Session, skip: int = 0, limit = 100):

    return db.query(BaseModel.Product).offset(skip).limit(limit).all()

def delete_product(db: Session, product_id: int):

   db_product =  db.query(BaseModel.Product).filter(BaseModel.Product.id == product_id).first()
   db.delete(db_product)
   db.commit()
   return db_product