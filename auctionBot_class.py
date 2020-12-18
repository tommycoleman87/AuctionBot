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
        self.headers = { 'content-type': 'application/json;charset=UTF-8','Authorization' : f'Bearer {self.access_token}'}
        try:
            self.access_token = self.getAccessToken()
            self.headers['Authorization'] = f'Bearer {self.access_token}'
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
    
    class Decorators():
        @staticmethod
        def refreshToken(decorated):
            # the function that is used to check
            # the JWT and refresh if necessary
            def wrapper(api,*args,**kwargs):
                if time.time() > api.expiration:
                    api.getAccessToken()
                return decorated(api,*args,**kwargs)

            return wrapper

    @Decorators.refreshToken
    async def current_server(self, ctx):
        server_name = self.server['name']
        await ctx.send(f'The server is set to {server_name}')
    
    @Decorators.refreshToken
    async def set_server(self, ctx, new_server):
        response = requests.get(f'https://us.api.blizzard.com/data/wow/search/connected-realm?namespace=dynamic-us&realms.name.en_US={new_server}', headers = self.headers)
        if response.status_code == 200:
            realm = [r for r in response.json()['results'][0]['data']['realms'] if r['name']['en_US'].find(new_server) != -1]
            if len(realm) == 0:
                await ctx.send('Realm not found. Check spelling and capitalization and try again.')
            elif len(realm) > 1:
                await ctx.send('Too many matches, please be more specific.')
            else:
                self.server['name'] = realm[0]['name']['en_US']
                self.server['id'] = response.json()['results'][0]['data']['id']
                await ctx.send(f'Server set to {self.server["name"]}')
        else:
            await ctx.send(f'Error {response.status_code}')

    @Decorators.refreshToken
    async def token(self, ctx):
        response = requests.get(f'https://us.api.blizzard.com/data/wow/token/index?namespace=dynamic-us&locale=en_US', headers = self.headers)
        if response.status_code == 200:
            token_price = str(response.json()['price'])[:-4]
            await ctx.send("The current price of a WoW token is {:,} Gold".format(int(token_price)))
        else:
            await ctx.send(f"Error {response.status_code}")

    @Decorators.refreshToken
    async def price_check(self, ctx, arg):
        item_request = requests.get(f'https://us.api.blizzard.com/data/wow/search/item?namespace=static-us&locale=en_US&name.en_US={arg}&orderby=id', headers = self.headers)
        if item_request.status_code == 200:
            items = item_request.json()['results']
            items_table = {}
            
            for item in items:
                name = item['data']['name']['en_US']
                if name.find(arg) != -1:
                    items_table[item['data']['id']] = { 'name' : name, 'price' : None}
            
            response = requests.get(f'https://us.api.blizzard.com/data/wow/connected-realm/{self.server["id"]}/auctions?namespace=dynamic-us&locale=en_US', headers = self.headers)
            if response.status_code == 200:
                message = ''
                auctions = response.json()['auctions']
                for auction in auctions:
                    item_id = auction['item']['id']
                    if item_id in items_table.keys():
                        if 'buyout' in auction:
                            if items_table[item_id]['price'] is None or items_table[item_id]['price'] > auction['buyout']:
                                items_table[item_id]['price'] = auction['buyout']
                        elif 'unit_price' in auction:
                            if items_table[item_id]['price'] is None or items_table[item_id]['price'] > auction['unit_price']:
                                items_table[item_id]['price'] = auction['unit_price']
                
                for key in items_table.keys():
                    if items_table[key]['price'] is not None:
                        price = self.wow_currency_converter(items_table[key]['price'])
                        if items_table[key]['name'] == arg:
                            await ctx.send(f'{items_table[key]["name"]} is {price}')
                            return
                        else:
                            message += f'{items_table[key]["name"]} is {price} \n'
                if len(message) != 0:
                    await ctx.send(message)
                else:
                    await ctx.send('Item not found in the Auction House')
            else:
                await ctx.send(f'Error {response.status_code}')
        else:
            await ctx.send(f'Error {item_request.status_code}')

    @Decorators.refreshToken
    async def item_search(self, ctx, arg):
        item_request = requests.get(f'https://us.api.blizzard.com/data/wow/search/item?namespace=static-us&locale=en_US&name.en_US={arg}&orderby=id', headers = self.headers)
        if item_request.status_code == 200:
            items = item_request.json()['results']
            for item in items:
                name = item['data']['name']['en_US']
                if name == arg:
                    return_item = {
                        'type' : item['data']['item_subclass']['name']['en_US']
                    }
                    await ctx.send(item)
                    await ctx.send(return_item)
        await ctx.send(item_request.status_code)
   
    def wow_currency_converter(self, currency):
        price = None
        if currency < 100:
            price = str(currency) + ' Copper'
        elif currency < 10000:
            price = str(currency)[:-2] + ' Silver ' + str(currency)[-2:] + ' Copper'
        else:
            price = '{:,}'.format(int(str(currency)[:-4])) + ' Gold ' + str(currency)[-4:-2] + " Silver " + str(currency)[-2:] + ' Copper'
        return price

    
