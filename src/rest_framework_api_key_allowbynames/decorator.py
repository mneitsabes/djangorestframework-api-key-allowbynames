from functools import wraps

from rest_framework_api_key.models import APIKey
from rest_framework.exceptions import AuthenticationFailed


def allow_only_apikey(key_names):
    """
    Allow access only by the API key named with the provided name.

    :param key_names: the keys's name authorized
    :type key_names: [str]
    """

    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            request = args[1]

            success = False

            try:
                key = request.META["HTTP_AUTHORIZATION"].split()[1]
                api_key = APIKey.objects.get_from_key(key)

                for k in key_names:
                    if api_key.name == k:
                        success = True
                        break

                if success:
                    request.META["API_KEY_NAME"] = api_key.name
            except ValueError:
                pass

            if not success:
                raise AuthenticationFailed()

            return f(*args, **kwargs)

        return wrapped

    return wrapper
