from django.contrib.auth.backends import BaseBackend, ModelBackend


class MyBackend(ModelBackend):

    def get_user(self, user_id):
        print('!!!!!')
        return super().get_user(user_id)

    def authenticate(self, request, username=None, password=None, **kwargs):
        print('!!!!!')
        return super().authenticate(request, username, password, **kwargs)

    # def authenticate(self, request, **kwargs):
    #     # Check the token and return a user.
    #     print('!!!!!')
    #     return None
