from fastapi import APIRouter, Depends, HTTPException
from schemas.user import UserBase, CreateUser, User, UpdateUser