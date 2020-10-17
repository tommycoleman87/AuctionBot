import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

WOW_CLIENT = os.getenv('WOW_CLIENT')
WOW_SECRET = os.getenv('WOW_SECRET')
class AuctionBot():


    def __init__(self):
        # the function that is executed when
        # an instance of the class is created
        self.host = 'https://us.battle.net/oauth/token'
        self.access_token = None
        self.expiration = None
        self.server = {'name': 'Stormrage', 'id': 60}
        try:
            self.access_token = self.getAccessToken()
            if self.access_token is None:
                raise Exception("Request for access token failed.")
        except Exception as e:
            print(e)
        else:
            self.expiration = time.time() + 86300

    def getAccessToken(self):
        # the function that is 
        # used to request the JWT
        try:
            # build the JWT and store
            # in the variable `token_body`
            data = { 'grant_type': 'client_credentials' }
            # request an access token
            request = requests.post(self.host, data=data, auth=(WOW_CLIENT, WOW_SECRET))

            # optional: raise exception for status code
            request.raise_for_status()
        except Exception as e:
            print(e)
            return None
        else:
            # assuming the response's structure is
            # {"access_token": ""}
            return request.json()['access_token']

    async def greet(self, message):
        author = message.author.split('#')[0]
        await message.send(f'Greetings {author}')

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