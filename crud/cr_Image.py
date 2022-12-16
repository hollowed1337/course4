from sqlalchemy.orm import Session

from models import BaseModel
from schemas import schem_Image

def create_image(db: Session, image: schem_Image.ImageCreate):
    
    db_image = BaseModel.Image(img_url=image.img_url)
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image


def get_image(db: Session, image_id: int):

    return db.query(BaseModel.Image).filter(BaseModel.Image.id == image_id).first()

def get_image_by_url(db: Session, url: int):

    return db.query(BaseModel.Image).filter(BaseModel.Image.img_url == url).firts()

def read_images(db: Session, skip: int, limit: int):
    return db.query(BaseModel.Image).limit(limit).offset(skip).all()

def delete_img(db: Session, image_id: int):

    img = db.query(BaseModel.Image).filter(BaseModel.Image.id == image_id).first()
    db.delete(img)
    db.commit()
    return img