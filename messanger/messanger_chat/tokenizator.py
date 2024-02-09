import jwt
from datetime import datetime, timedelta

from messanger import settings

ALGORITHM = "HS256"
access_token_jwt_subject = "access"


def create_token(user_profile_id: int) -> dict:
    access_token_expires = timedelta(minutes=120)
    return {
        "access_token": create_access_token(
            data={"user_profile_id": user_profile_id}, expires_delta=access_token_expires
        ),
        "token_type": "Token",
    }


def create_access_token(data: dict, expires_delta: timedelta = None):
    """Создание токена"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=120)
    to_encode.update({"exp": expire, "sub": access_token_jwt_subject})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

"""создание токена на 2 часа. Ввести нужно id профиля пользователя (он такой же как и user)"""
token = create_token(2)
print(token)