# Django RESTframework-api key - Allow by key names

Decorator working with `djangorestframework-api-key` allowing to restrict access to a method according to the key 
presented.

# Usage

Use `@allow_only_apikey()` with a list of key names as the first parameter :

    class TelegramMemberCheck(APIView):
        permission_classes = [HasAPIKey]
    
        @allow_only_apikey(['TelegramBot'])
        def get(self, request, format=None):
            pass

If the key does not match, an `AuthenticationFailed` is returned.
