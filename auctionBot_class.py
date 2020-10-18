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
                print('error')
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
            print(request.status_code)
        except Exception as e:
            print(e)
            return None
        else:
            # assuming the response's structure is
            # {"access_token": ""}
            return request.json()['access_token']

    async def greet(self, ctx):
        author = str(ctx.author).split('#')[0]
        await ctx.send(f'Greetings {author}')

    async def current_server(self, ctx):
        server_name = self.server['name']
        await ctx.send(f'The server is set to {server_name}')
    
    async def set_server(self, ctx, new_server):
        headers = { 'content-type': 'application/json;charset=UTF-8','Authorization' : f'Bearer {self.access_token}'}
        response = requests.get(f'https://us.api.blizzard.com/data/wow/search/connected-realm?namespace=dynamic-us&realms.name.en_US={new_server}', headers = headers)
        realm = [r for r in response.json()['results'][0]['data']['realms'] if r['name']['en_US'].find(new_server) != -1]
        if response.status_code == 200:
            if len(realm) == 0:
                await ctx.send('Realm not found. Check spelling and capitalization and try again.')
            else:
                self.server['name'] = realm[0]['name']['en_US']
                self.server['id'] = realm[0]['id'] 
                await ctx.send(f'Server set to {self.server["name"]}')
        else:
            await ctx.send(f'Error {response.status_code}')

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