# 1️⃣ AuctionBot

1️⃣ You can find the deployed project at [AuctionBot](https://discord.com/api/oauth2/authorize?client_id=763900890917634059&permissions=2048&scope=bot).

## 4️⃣ Contributors


|                                       [Tommy Coleman](https://github.com/tommycoleman87)                                        | 
| :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: |
|                      [<img src="https://avatars1.githubusercontent.com/u/50923422?s=400&u=817cd183508a4da9c048210dcd1962de16298b2b&v=4" width = "200" />](https://github.com/tommycoleman87)                                        |
|                 [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/tommycoleman87)        
| [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/tommy-coleman-028151a4/) |
<br>
<br>


## Project Overview

AuctionBot is a discord bot used to find and report auction prices of specific items from World of Warcraft to a discord channel.

### 4️⃣ Key Features

-    Ability to switch the World of Warcraft server to one of your choosing use the command !server your_server_here
-    Ability to grab the buyout price of an item from the server the bot is set to using the command !price item_name_here
-    Ability to report the price of a World of Warcraft game token but typing the command !token
-    Ability to check the current server by typing the command !servercheck
-    feature five

## 1️⃣ Tech Stack

AuctionBot was built using python3, discord.py library, python_dotenv library, and requests library.



# APIs

## 2️⃣ OAuth 2.0

OAuth 2.0 is the industry-standard protocol for authorization. OAuth 2.0 focuses on client developer simplicity while providing specific authorization flows for web applications, desktop applications, mobile phones, and living room devices

## 2️⃣ Blizzard Entertainments World of Warcraft API

The World of Warcraft API requires OAuth 2.0 authentication. It provides an assortment of Game data and profile account data. AuctionBot mainly makes use of the server, items, and auction house endpoints.

## 3️⃣ Discord API

Discord API is used to connect the bot to discord. It gives the bot the permissions it needs to post messages in the discord channels. Discord also uses Oauth 2.0 for authentication.


# 3️⃣ Environment Variables

In order for the app to function correctly, the user must set up their own environment variables. There should be a .env file containing the following:



    *  BLIZZARD_CLIENT_ID - this is the client ID given to you by the Blizzard Developer Portal, this is necessary to access Blizzards API
    *  BLIZZARD_CLIENT_SECRET - this is the secret given to you by the Blizzard Developer Portal, this is necessary to access Blizzards API
    *  DISCORD_GUILD - This is the name of the Discord Server you want to connect the bot to
    *  DISCORD_TOKEN - The token generated by Discord to give you access to their API
    

## Bot Commands



    * !servercheck - reports the current World of Warcraft server the bot is set to
    * !server <server name> - will set the bot to the specific server
    * !token - will report the current price of a World of Warcraft game token
    * !hello - the bot will greet the user
    * !price <item name> - will report the current price of the item on the current World of Warcraft server

# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please note we have a [code of conduct](./CODE_OF_CONDUCT.md). Please follow it in all your interactions with the project.

## Issue/Bug Request
   
 **If you are having an issue with the existing project code, please submit a bug report under the following guidelines:**
 - Check first to see if your issue has already been reported.
 - Check to see if the issue has recently been fixed by attempting to reproduce the issue using the latest master branch in the repository.
 - Create a live example of the problem.
 - Submit a detailed bug report including your environment & browser, steps to reproduce the issue, actual and expected outcomes,  where you believe the issue is originating from, and any potential solutions you have considered.

### Feature Requests

We would love to hear from you about new features which would improve this app and further the aims of our project. Please provide as much detail and information as possible to show us why you think your new feature should be implemented.

### Pull Requests

If you have developed a patch, bug fix, or new feature that would improve this app, please submit a pull request. It is best to communicate your ideas with the developers first before investing a great deal of time into a pull request to ensure that it will mesh smoothly with the project.

Remember that this project is licensed under the MIT license, and by submitting a pull request, you agree that your work will be, too.

#### Pull Request Guidelines

- Ensure any install or build dependencies are removed before the end of the layer when doing a build.
- Update the README.md with details of changes to the interface, including new plist variables, exposed ports, useful file locations and container parameters.
- Ensure that your code conforms to our existing code conventions and test coverage.
- Include the relevant issue number, if applicable.
- You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

### Attribution

These contribution guidelines have been adapted from [this good-Contributing.md-template](https://gist.github.com/PurpleBooth/b24679402957c63ec426).


