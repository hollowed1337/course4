from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main.main import app, get_db
from models.BaseModel import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_role():
    response = client.post( 
        "/role",
        json={
            "name": "Мастер"}
        )
    
    assert response.status_code == 200, response.text
    data = response.json() 
    assert data["name"] == "Мастер"

def test_create_user():
    response = client.post( 
        "/user",
        json={
            "email": "ppa@ugrasu.ru",
            "password": "fakepassword123", 
            "name": "Ксения Собчак", 
            "login": "431245", 
            "payment": 412224515151, 
            "role_id": 1}
        )
    
    assert response.status_code == 200, response.text
    data = response.json() 
    assert data["email"] == "ppa@ugrasu.ru"

def test_create_exist_user():
    response = client.post( 
        "/user",
        json={
            "email": "ppa@ugrasu.ru",
            "password": "fakepassword123", 
            "name": "Ксения Собчак", 
            "login": "431245", 
            "payment": 412224515151, 
            "role_id": 1}
        )
    
    assert response.status_code == 400, response.text
    data = response.json() 
    assert data["detail"] == "Email используется"

def test_create_exist_user_login():
    response = client.post( 
        "/user",
        json={
            "email": "црошр@ugrasu.ru",
            "password": "fakepassword123", 
            "name": "Ксения Собчак", 
            "login": "431245", 
            "payment": 412224515151, 
            "role_id": 1}
        )
        
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Пользователь с данным логином уже существует"


def test_create_user_roleId_not_found():
    response = client.post( 
        "/user",
        json={
           "email": "aafffaaf@ugrasu.ru",
            "password": "fakepassword123", 
            "name": "Ксения Собчак", 
            "login": "logutHAha", 
            "payment": 412224515151, 
            "role_id": 2}
        )
        
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Роли с данным ID нет"


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["email"] == "ppa@ugrasu.ru"

def test_read_user_by_id():
    response = client.get(f"/user/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == "ppa@ugrasu.ru"


def test_user_not_found():
    response = client.get(f"/user/41")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Пользователь не найден"