from fastapi import APIRouter
from fastapi import status, HTTPException
from config.db import conn
from models.user import users
from schemas.users import User
from typing import List
from cryptography.fernet import Fernet



# create instance for user
user = APIRouter()
#Generator for key 
SECURE_KEY = Fernet.generate_key()
CRYPH = Fernet(SECURE_KEY)


@user.post(path="/users/singup",
          status_code= status.HTTP_201_CREATED,
          response_model=User,
          summary="register a user",
          tags=["users"])
def create_user(user:User):
    """**_summary_** <br>
    > This path operation, create a new user, Encrypt password for stored in the database

    **Args:** <br>
    > **user**: User -> Body Request
    - id -> Optional[str] because is primary Key into database.
    - name str
    - email EmailStr, Email validated
    - password str, min legth is 8  character
        
    **Returns:**<br>
    > Cursor: select to database with dates only password its encrypt
    """
    user = user.dict()
    password = user["password"] 
    user["password"] = CRYPH.encrypt(password.encode("utf_8"))
    result = conn.execute(users.insert().values(user))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()

@user.post(path="/users/login",
          status_code=status.HTTP_200_OK,
          summary="login a user",
          tags=["users"],
          deprecated=True)
def login_a_user():
    """_summary_

    Returns:
        _type_: _description_
    """
    return "login user"




@user.get(path="/users/",
          status_code=status.HTTP_200_OK,
          response_model=List[User],
          summary="Show all users",
          tags=["users"])
def get_users():
    """_summary_:</br> </br> This path operation, get all users

    Args:
        _Args_: </br> </br>None, Only Select Table database and response
    
    Returns:
        _type_: </br> </br> List all Users
    """
    return conn.execute(users.select()).fetchall()


@user.get(path="/users/{user_id}",
          status_code=status.HTTP_200_OK,
          summary="Show a user",
          tags=["users"])
def show_a_users():
    """_summary_

    Returns:
        _type_: _description_
    """
    return "show a user"


@user.put(path="/users/{user_id}/update",
          status_code=status.HTTP_200_OK,
          summary="Update a user",
          tags=["users"])
def update_a_users():
    """_summary_

    Returns:
        _type_: _description_
    """
    return "update a user"


@user.delete(path="/users/{user_id}/delete",
          summary="Delete a user",
          tags=["users"])
def delete_a_users():
    """_summary_

    Returns:
        _type_: _description_
    """
    return "delete a user"