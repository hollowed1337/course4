from sqlalchemy.orm import Session
from datetime import  datetime
from models import BaseModel
from schemas import schem_User

def create_user(db: Session, user: schem_User.UserCreate, role_id: int):

    reg_date = datetime.now()
    db_user = BaseModel.User(**user.dict(), reg_date=reg_date)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def edit_user(db: Session,  user_id: int, user: schem_User.UserUpdate):

    db.query(BaseModel.User).filter(BaseModel.User.id == user_id).update(
        {BaseModel.User.name: user.name,
        BaseModel.User.login: user.login,
        BaseModel.User.email: user.email,
        BaseModel.User.password: user.password,
        BaseModel.User.payment: user.payment,
        BaseModel.User.role_id: user.role_id, }, synchronize_session="fetch"
    )
    db.commit()
    #db.refresh(db_order)
    return db.query(BaseModel.User).filter(BaseModel.User.id == user_id).first()

def get_user(db: Session, user_id: int):

    return db.query(BaseModel.User).filter(BaseModel.User.id == user_id).first()

def read_users(db: Session, skip: int = 0, limit: int = 100):
    
    return db.query(BaseModel.User).offset(skip).limit(limit).all()

def get_user_by_email(db: Session, email: str):

    return db.query(BaseModel.User).filter(BaseModel.User.email == email).first()

def get_user_by_login(db: Session, login: str):

    return db.query(BaseModel.User).filter(BaseModel.User.login == login).first()

def get_users_by_role_id(db: Session, role_id: int):
    
    return db.query(BaseModel.Role).filter(role_id == BaseModel.Role.id).all()

def delete_user(db: Session, user_id: int):

    user = db.query(BaseModel.User).filter(BaseModel.User.id == user_id).first()
    db.delete(user)
    db.commit()
    return user


