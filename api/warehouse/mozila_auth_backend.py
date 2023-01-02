from mozilla_django_oidc.auth import OIDCAuthenticationBackend
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenVerifySerializer

from core.models import User
from rest_framework import HTTP_HEADER_ENCODING, exceptions

# def get_authorization_header(request):
#     auth = request.META.get("HTTP_AUTHORIZATION", "")
#     return auth


def get_authorization_header(request):
    """
    Return request's 'Authorization:' header, as a bytestring.
    Hide some test client ickyness where the header can be unicode.
    """
    auth = request.META.get('HTTP_AUTHORIZATION', b'')
    if isinstance(auth, str):
        # Work around django test client oddness
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth


class MyOIDCAB(OIDCAuthenticationBackend):

    def authenticate(self, request, **kwargs):
        # auth = get_authorization_header(request)
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        data = {'token': token}

        try:
            valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
            # valid_data = TokenVerifySerializer().validate(data)
            email = valid_data['email']

            profile = User.objects.get(email=email)
            # return [profile.user]
            request.user = profile
        except ValidationError as v:
            print("validation error", v)

        # return super().authenticate(request, **kwargs)
        return (request.user, None)

    # def filter_users_by_claims(self, claims):
    #     email = claims.get('email')
    #     if not email:
    #         return self.UserModel.objects.none()
    #
    #     try:
    #         profile = User.objects.get(email=email)
    #         return [profile.user]
    #
    #     except User.DoesNotExist:
    #         return self.UserModel.objects.none()
