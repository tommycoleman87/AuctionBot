import time
import requests
class AuctionBot():
    host = None
    key = None
    secret = None
    access_token = None
    access_token_expiration = None

    def __init__(self,host,key,secret):
        # the function that is executed when
        # an instance of the class is created
        self.host = host
        self.key = key
        self.secret = secret

        try:
            self.access_token = self.getAccessToken()
            if self.access_token is None:
                raise Exception("Request for access token failed.")
        except Exception as e:
            print(e)
        else:
            self.access_token_expiration = time.time() + 3500

    def getAccessToken(self):
        # the function that is 
        # used to request the JWT
        try:
            # build the JWT and store
            # in the variable `token_body`

            # request an access token
            request = requests.post(self.host)

            # optional: raise exception for status code
            request.raise_for_status()
        except Exception as e:
            print(e)
            return None
        else:
            # assuming the response's structure is
            # {"access_token": ""}
            return request.json()['access_token']

    class Decorators():
        @staticmethod
        def refreshToken(decorated):
            # the function that is used to check
            # the JWT and refresh if necessary
            def wrapper(api,*args,**kwargs):
                if time.time() > api.access_token_expiration:
                    api.getAccessToken()
                return decorated(api,*args,**kwargs)

            return wrapper

    # @Decorators.refreshToken
    # def someRequest():
    #     # make our API request
    #     pass