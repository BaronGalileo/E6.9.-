import os
from datetime import datetime

import django
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from .models import UserPage

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'messanger.settings')
django.setup()

import jwt
from django.conf import settings
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware

from django.db import close_old_connections

ALGORITHM = "HS256"


@database_sync_to_async
def get_user(token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=ALGORITHM)
    except:
        print('no payload')


    token_exp = datetime.fromtimestamp(payload['exp'])
    if token_exp < datetime.utcnow():
        print("no date-time")


    try:
        user = UserPage.objects.get(user_profile_id=payload['user_profile_id'])

    except UserPage.DoesNotExist:
        print('no user')



    return user


class TokenAuthMiddleware(BaseMiddleware):

    async def __call__(self, scope, receive, send):
        close_old_connections()

        try:
            token_key = (dict((x.split('=') for x in scope['query_string'].decode().split("&")))).get('token', None)
        except ValueError:
            token_key = None


        scope['user'] = await get_user(token_key)
        return await super().__call__(scope, receive, send)


def JwtAuthMiddlewareStack(inner):
    return TokenAuthMiddleware(inner)

