# coding=utf-8

from users.models import User


class EmailAuthBackend(object):
    """
    Email Authentication Backend

    Allows a user to sign in using an email/password pair, then check
    a username/password pair if email failed
    """
    def authenticate(self, username=None, password=None, **kwargs):
        """ Authenticate a user based on email address as the user name. """
        try:
            user = User.objects.get(email=username)
            if getattr(user, 'is_active') and user.check_password(password):
                return user
        except User.DoesNotExist:
            try:
                user = User.objects.get(username=username)
                if getattr(user, 'is_active') and \
                        user.check_password(password):
                    return user
            except User.DoesNotExist:
                return None

    def get_user(self, user_id):
        """ Get a User object from the user_id. """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
