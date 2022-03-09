from fastapi import APIRouter
from fastapi import status, HTTPException
from config.db import conn
from models.user import users
from schemas.users import User

# create instance for user
user = APIRouter()


@user.post(path="/users/singup",
          status_code=status.HTTP_201_CREATED,
          summary="register a user",
          tags=["users"])
def create_user(user:User):
    """_summary_

    Returns:
        _type_: _description_
    """
    return user.dict()

@user.post(path="/users/login",
          status_code=status.HTTP_200_OK,
          summary="login a user",
          tags=["users"])
def login_a_user():
    """_summary_

    Returns:
        _type_: _description_
    """
    return "login user"




@user.get(path="/users/",
          status_code=status.HTTP_200_OK,
          summary="Show all users",
          tags=["users"])
def get_users():
    """_summary_

    Returns:
        _type_: _description_
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