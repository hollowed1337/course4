from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from models import BaseModel
from crud import cr_Crate, cr_Image, cr_Material, cr_Order, cr_ProdType, cr_Product, cr_Role, cr_User
from schemas import schem_Crate, schem_Image, schem_Material, schem_Order, schem_ProdType, schem_Product, schem_Role,schem_User
from database.database import SessionLocal, engine

BaseModel.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.post("/crate", response_model= schem_Crate.Crate)
# def create_crate(crate: schem_Crate.CrateCreate,db: Session = Depends(get_db)):
    
#     db_crate_user = cr_Crate.get_crates_by_user_id(db, user_id=crate.user_id)
#     db_crate_product = cr_Crate.get_crates_by_product_id(db, product_id=crate.product_id)
#     db_crate_order = cr_Crate.get_crates_by_order_id(db, order_id=crate.order_id)

#     if not db_crate_user:
#         raise HTTPException(status_code=404, detail="Пользователь не найден")
#     if not db_crate_product:
#         raise HTTPException(status_code=404, detail="Изделие не найдено")
#     if not db_crate_order:
#         raise HTTPException(status_code=404, detail="Заказ не найден")

#     return cr_Crate.create_crate(db=db, crate=crate, product_id=crate.product_id, order_id=crate.order_id, user_id=crate.user_id)

# @app.get("/crate/{crate_id}", response_model=schem_Crate.Crate)
# def get_crate(crate_id: int, db: Session = Depends(get_db)):
    
#     db_crate = cr_Crate.get_crate(db, crate_id=crate_id)
#     if  not db_crate:
#         raise HTTPException(status_code=228, detail="Корзины не существует")
#     return db_crate

# @app.get("/crates", response_model=list[schem_Crate.Crate])
# def read_crates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

#     crates = cr_Crate.read_crates(db, skip=skip, limit=limit)
#     return crates

# @app.get("/crates/user/{user_id}", response_model=list[schem_Crate.Crate])
# def read_crates_by_user_id(user_id: int, db: Session = Depends(get_db)):

#     crates = cr_Crate.get_crates_by_user_id(db, user_id=user_id)
#     if not crates:
#         raise HTTPException(status_code=404, detail="Пользователь не найден")
#     return crates

# @app.delete("/crate/{crate_id}", response_model=schem_Crate.Crate)
# def delete_crate(crate_id: int, db: Session = Depends(get_db)):
    
#     db_crate = cr_Crate.get_crate(db, crate_id=crate_id)
#     if  not db_crate:
#         raise HTTPException(status_code=228, detail="Корзины не существует")
#     return cr_Crate.delete_crate(db, crate_id=crate_id)


# @app.post("/image", response_model= schem_Image.Image)
# def create_img(img: schem_Image.ImageCreate, db: Session = Depends(get_db)):

#     return cr_Image.create_image(db=db, image=img)

# @app.get("/image/{img_id}", response_model=schem_Image.Image)
# def get_img(img_id: int, db: Session = Depends(get_db)):
    
#     db_img = cr_Image.get_image(db, image_id=img_id)
#     if not db_img:
#         raise HTTPException(status_code=400, detail="Изображения нет")
#     return db_img

# @app.get("/images", response_model=list[schem_Image.Image])
# def read_images(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

#     return cr_Image.read_images(db=db, limit=limit, skip=skip)

# @app.delete("/image/{img_id}", response_model=schem_Image.Image)
# def delete_img(img_id: int, db: Session = Depends(get_db)):
    
#     db_img = cr_Image.get_image(db, image_id=img_id)
#     if not db_img:
#         raise HTTPException(status_code=400, detail="Изображения нет")

#     return cr_Image.delete_img(db, image_id=img_id)


@app.post("/user", response_model=schem_User.User)
def create_user(user: schem_User.UserCreate, db: Session = Depends(get_db)):

    db_email = cr_User.get_user_by_email(db, email=user.email)
    db_login = cr_User.get_user_by_login(db, login=user.login)
    if db_email: 
        raise HTTPException(status_code=400, detail="Email используется")
    if db_login: 
        raise HTTPException(status_code=400, detail="Пользователь с данным логином уже существует")
    
    db_user_role = cr_User.get_users_by_role_id(db, role_id=user.role_id)
    if not db_user_role:
        raise HTTPException(status_code=400, detail="Роли с данным ID нет")
        
    return cr_User.create_user(db=db, user=user, role_id=user.role_id)

@app.get("/user/{user_id}",  response_model=schem_User.User)
def get_user(user_id: int, db: Session = Depends(get_db)):

    db_user =  cr_User.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return db_user

@app.get("/users", response_model=list[schem_User.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    users = cr_User.read_users(db, skip=skip, limit=limit)
    return users

@app.delete("/user/{user_id}",  response_model=schem_User.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):

    db_user =  cr_User.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return cr_User.delete_user(db, user_id=user_id)

@app.put("/user/{user_id}", response_model=schem_User.User)
def edit_order(user: schem_User.UserUpdate, user_id: int, db: Session = Depends(get_db)):

    edit_user = cr_User.get_user(db, user_id=user_id)
    if not edit_user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    return cr_User.edit_user(db, user_id=user_id, user=user)

@app.post("/role", response_model= schem_Role.Role)
def create_role(role: schem_Role.RoleCreate, db: Session = Depends(get_db)):
    
    db_role_name = cr_Role.get_roles_by_name(db, name=role.name)
    if db_role_name:
        raise HTTPException(status_code=400, detail="Ролей с одинаковым названием не должно быть")

    return cr_Role.create_role(db=db, role=role)

# @app.get("/role/{role_id}", response_model=schem_Role.Role)
# def get_role(role_id: int, db: Session = Depends(get_db)):

#     db_role = cr_Role.get_role(db, role_id=role_id)
#     if not db_role:
#         raise HTTPException(status_code=404, detail="Роли не существует")
#     return db_role

# @app.get("/roles", response_model=list[schem_Role.Role])
# def read_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

#     roles = cr_Role.read_roles(db, skip=skip, limit=limit)
#     return roles

# @app.delete("/role/{role_id}", response_model=schem_Role.Role)
# def delete_role(role_id: int, db: Session = Depends(get_db)):

#     db_role = cr_Role.get_role(db, role_id=role_id)
#     if not db_role:
#         raise HTTPException(status_code=404, detail="Роли не существует")
#     return cr_Role.delete_role(db, role_id=role_id)


# @app.post("/prodtype", response_model= schem_ProdType.ProdType)
# def create_prodtype(prodtype: schem_ProdType.ProdTypeCreate, db: Session = Depends(get_db)):

#     db_prodtype = cr_ProdType.get_prodtype_by_name(db, name=prodtype.name)
#     if db_prodtype:
#         raise HTTPException(status_code=400, detail="Тип продукта уже существует")
#     return cr_ProdType.create_prodtype(db=db, prodtype=prodtype)

# @app.get("/prodtype/{prodtype_id}", response_model=schem_ProdType.ProdType)
# def get_prodtype(prodtype_id: int, db: Session = Depends(get_db)):
    
#     db_prodtype = cr_ProdType.get_prodtype(db, prodtype_id=prodtype_id)
#     if not db_prodtype:
#         raise HTTPException(status_code=400, detail="Типа продукта не существует")
#     return db_prodtype

# @app.get("/prodtypes", response_model=list[schem_ProdType.ProdType])
# def read_prodtypes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

#     return cr_ProdType.read_prodtypes(db=db, limit=limit, skip=skip)


# @app.delete("/prodtype/{prodtype_id}", response_model=schem_ProdType.ProdType)
# def delete_prodtype(prodtype_id: int, db: Session = Depends(get_db)):
    
#     db_prodtype = cr_ProdType.get_prodtype(db, prodtype_id=prodtype_id)
#     if not db_prodtype:
#         raise HTTPException(status_code=404, detail="Типа продукта не существует")
#     return cr_ProdType.del_prodtype(db, prodtype_id=prodtype_id)


# @app.post("/material", response_model= schem_Material.Material)
# def create_material( material: schem_Material.MaterialCreate, db: Session = Depends(get_db)):

#     db_material = cr_Material.get_material_by_name(db, name= material.name)
#     if db_material:
#         raise HTTPException(status_code=400, detail="Материал уже существует")
#     return cr_Material.create_material(db=db,  material= material)

# @app.get("/material/{material_id}", response_model=schem_Material.Material)
# def get_material(material_id: int, db: Session = Depends(get_db)):
    
#     db_material = cr_Material.get_material(db,  material_id= material_id)
#     if not db_material:
#         raise HTTPException(status_code=400, detail="Материала нет на складе")
#     return db_material

# @app.get("/materials/", response_model=list[schem_Material.Material])
# def read_materials(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

#     return cr_Material.read_materials(db=db, limit=limit, skip=skip)

# @app.delete("/material/{material_id}", response_model=schem_Material.Material)
# def delete_material(material_id: int, db: Session = Depends(get_db)):
    
#     db_material = cr_Material.get_material(db,  material_id= material_id)
#     if not db_material:
#         raise HTTPException(status_code=400, detail="Материала нет на складе")
#     return cr_Material.delete_material(db,  material_id= material_id)

# @app.post("/product", response_model=schem_Product.Product)
# def create_product(product: schem_Product.ProductCreate, db: Session = Depends(get_db)):

#     db_material= cr_Product.get_products_by_material(db, material_id=product.material_id)
#     db_prodtyp = cr_Product.get_products_by_prodtype(db, prodtype_id=product.prodtype_id)
#     db_img = cr_Product.get_products_by_img(db,img_id=product.image_id)
#     if not db_material: 
#         raise HTTPException(status_code=400, detail="Материала с таким ID не существует")
#     if not db_prodtyp: 
#         raise HTTPException(status_code=400, detail="Типа продукта с таким ID не существует")
#     if not db_img: 
#         raise HTTPException(status_code=400, detail="Изображения с таким ID не существует")
    
#     return cr_Product.create_product(db=db, product=product, image_id=product.image_id, prodtype_id=product.prodtype_id, material_id=product.material_id)

# @app.get("/product/{product_id}",  response_model=schem_Product.Product)
# def get_product(product_id: int, db: Session = Depends(get_db)):
    
#     db_product = cr_Product.get_product(db, product_id=product_id)
#     if not db_product:
#         raise HTTPException(status_code=400, detail= "Продукт не найден")
#     return db_product

# @app.get("/products/", response_model=list[schem_Product.Product])
# def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

#     products = cr_Product.read_products(db, skip=skip, limit=limit)
#     return products

# @app.delete("/product/{product_id}",  response_model=schem_Product.Product)
# def delete_product(product_id: int, db: Session = Depends(get_db)):

#     db_product = cr_Product.get_product(db, product_id=product_id)
#     if not db_product:
#         raise HTTPException(status_code=400, detail="Товар не найден")
        
#     return cr_Product.delete_product(db, product_id=product_id)


# @app.post("/order", response_model=schem_Order.Order)
# def create_order(order: schem_Order.OrderCreate, db: Session = Depends(get_db)):

#     db_order = cr_Order.get_order_by_order_num(db, order_num = order.order_num)
#     db_order_by_user = cr_Order.get_orders_by_user(db, user_id=order.user_id)
#     db_order_by_product = cr_Order.get_orders_by_product(db, product_id=order.product_id)
#     if db_order:
#         raise HTTPException(status_code=400, detail="Заказ с таким номером уже существует")
#     elif not db_order_by_user:
#         raise HTTPException(status_code=400, detail="Пользователь не найден")
#     elif not db_order_by_product:
#         raise HTTPException(status_code=400, detail="Изделие не найдено")
        
#     return cr_Order.create_order(db=db, order=order)


# @app.get("/order/{order_id}", response_model= schem_Order.Order)
# def get_order(order_id: int, db: Session = Depends(get_db)):

#     db_order = cr_Order.get_order(db, order_id=order_id)
#     if not db_order:
#         raise HTTPException(status_code=400, detail="Заказа не найдено")
#     return db_order


# @app.get("/orders", response_model=list[schem_Order.Order])
# def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

#     return cr_Order.read_orders(db, skip=skip, limit=limit)


# @app.delete("/order/{order_id}", response_model= schem_Order.Order)
# def delete_order(order_id: int, db: Session = Depends(get_db)):

#     db_order = cr_Order.get_order(db, order_id=order_id)
#     if not db_order:
#         raise HTTPException(status_code=400, detail="Заказа не найдено")
        
#     return cr_Order.delete_order(db, order_id=order_id)

# @app.put("/order/{order_id}", response_model=schem_Order.Order)
# def edit_order(order: schem_Order.OrderUpdate, order_id: int, db: Session = Depends(get_db)):

#     edit_ord = cr_Order.get_order(db, order_id=order_id)
#     if not edit_ord:
#         raise HTTPException(status_code=404, detail="Заказ не найден")
    
#     db_order_by_user = cr_Order.get_orders_by_user(db, user_id=order.user_id)
#     db_order_by_product = cr_Order.get_orders_by_product(db, product_id=order.product_id)
#     if not db_order_by_user:
#         raise HTTPException(status_code=400, detail="Пользователь не найден")
#     elif not db_order_by_product:
#         raise HTTPException(status_code=400, detail="Изделие не найдено")

#     return cr_Order.edit_order(db, order_id=order_id, order=order)