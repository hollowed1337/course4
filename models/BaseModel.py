from sqlalchemy import ForeignKey, Column,  Integer, String, Date, DateTime
from sqlalchemy.orm import  declarative_base, relationship

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    def __repr__(self):
        return f"<{type(self).__name__}(id={self.id})>"

class Crate(BaseModel):
    __tablename__ = "crates"

    count = Column(Integer)
    summ = Column(Integer)
    status = Column(String)
    product_id = Column(Integer, ForeignKey("products.id"))
    order_id = Column(Integer, ForeignKey("orders.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="crate")
    product = relationship("Product", back_populates="crate")
    order = relationship("Order", back_populates="crate")


class Image(BaseModel):
    __tablename__ = "images"

    img_url = Column(String)
    
    product = relationship("Product", back_populates="img")


class Log(BaseModel):
    __tablename__ = "logs"

    input_time = Column(DateTime)
    output_time = Column(DateTime)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="log")

class Material(BaseModel):
    __tablename__ = "materials"

    name = Column(String, unique=True, index=True)

    product = relationship("Product", back_populates="material")

class Order(BaseModel):
    __tablename__ = "orders"

    name = Column(String)
    order_num = Column(Integer, unique=True, index=True)
    price = Column(Integer)
    date = Column(DateTime)
    order_status = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    crate = relationship("Crate", back_populates="order")
    user = relationship("User", back_populates="order")
    product = relationship("Product", back_populates="order")

class ProdType(BaseModel):
    __tablename__ = "products_type"

    name = Column(String, unique=True, index=True)

    product = relationship("Product", back_populates="prodtype")


class Product(BaseModel):
    __tablename__ = "products"

    name = Column(String)
    desc = Column(String)
    stock = Column(Integer)
    sale = Column(Integer)
    price = Column(Integer)
    weight = Column(Integer)
    prodtype_id = Column(Integer, ForeignKey("products_type.id"))
    material_id = Column(Integer, ForeignKey("materials.id"))
    image_id = Column(Integer, ForeignKey("images.id"))

    order = relationship("Order", back_populates="product")
    crate = relationship("Crate", back_populates="product")
    material = relationship("Material", back_populates="product")
    prodtype = relationship("ProdType", back_populates="product")
    img = relationship("Image", back_populates="product")

class Role(BaseModel):
    __tablename__ = "roles"

    name = Column(String, unique=True, index=True)

    user = relationship("User", back_populates="role")

class User(BaseModel):
    __tablename__ = "users"

    name = Column(String)
    login = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    payment = Column(Integer)
    reg_date = Column(Date)
    role_id = Column(Integer, ForeignKey("roles.id"))

    role = relationship("Role", back_populates="user")
    log = relationship("Log", back_populates="user")
    order = relationship("Order", back_populates="user")
    crate = relationship("Crate", back_populates="user")