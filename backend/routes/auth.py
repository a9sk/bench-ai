from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import mysql.connector
import bcrypt
import logging

router = APIRouter()

# database configuration to move somwhere else
DB_CONFIG = {
    "host": "mysql",
    "user": "root",
    "password": "root",
    "database": "benchai"
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@router.post("/register")
async def register(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    confirm_password: str = Form(...)
):
    # debug logging
    print(f"Password: {password}")
    print(f"Confirm password: {confirm_password}")
    print(f"Passwords match: {password == confirm_password}")
    
    # check if passwords match
    if password != confirm_password:
        raise HTTPException(status_code=400, detail="Passwords do not match")

    conn = get_db_connection()
    cursor = conn.cursor()

    # hash password
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    try:
        cursor.execute(
            "INSERT INTO users (username, email, hashed_password) VALUES (%s, %s, %s)",
            (username, email, hashed_password.decode())
        )
        conn.commit()
    except mysql.connector.errors.IntegrityError:
        raise HTTPException(status_code=400, detail="Username or email already exists")
    finally:
        cursor.close()
        conn.close()

    return RedirectResponse(url="/", status_code=303)

@router.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()
        
        if not user or not bcrypt.checkpw(password.encode(), user['hashed_password'].encode()):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        return RedirectResponse(url="/", status_code=303)
    finally:
        cursor.close()
        conn.close()

@router.get("/logout")
async def logout():
    return RedirectResponse(url="/login", status_code=303)
