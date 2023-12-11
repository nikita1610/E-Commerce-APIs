from dotenv import dotenv_values
import jwt
from fastapi import (FastAPI, Depends, HTTPException, status)

from models import *
from passlib.context import CryptContext


config_credentials = dict(dotenv_values(".env"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)