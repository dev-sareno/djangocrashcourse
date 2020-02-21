from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from django.http import HttpRequest
from django.contrib.auth.hashers import check_password


class Authentication(authentication.BaseAuthentication):
    def authenticate(self, request: HttpRequest):
        skey = request.POST.get('skey')
        if not skey:
            raise exceptions.AuthenticationFailed('skey not found')

        username = request.POST.get('username')
        password2 = request.POST.get('password2')
        if not password2:
            raise exceptions.AuthenticationFailed('password2 not found')

        try:
            user: User = User.objects.get(username=username)  # get the user
            user_pw = user.password

            if not check_password(password2, user_pw):
                raise exceptions.AuthenticationFailed('invalid password2')
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')  # raise exception if user does not exist

        return (user, None)  # authentication successful
