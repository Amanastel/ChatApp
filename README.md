# Chat App
Group chat app built with Django, django-channels, and rest_framework 

## Table Of Contents

- [Chat App](#chat-app)
  - [Table Of Contents](#table-of-contents)
    - [Installation](#installation)
    - [Setup](#setup)
    - [Features](#features)
   

### Installation
- Clone this repository https://github.com/amanastel/ChatApp
```sh
git clone https://github.com/amanastel/ChatApp
cd chat-app
```
- Activate the local environment
```sh
virtualenv env
source env/bin/activate
```
- Install the requirements
```sh
pip3 install -r requirements.txt
```
- Migrate the database
```sh
./manage.py makemigrations
./manage.py migrate
```

### Setup 
Go to app/settings.py to set your Redis url
```py
CHANNEL_LAYERS = {
        "default":{
            "BACKEND":"channels_redis.core.RedisChannelLayer",
            "CONFIG":{
                "hosts":[('localhost', 6379)],
            }
        },
}
```
You can run the server by using command
```sh
./manage.py runserver
```

Create your bot!
```
./manage.py create_bot

Username for your bot : ganteng
File name to generate : bot_ganteng.py
Bot Description : Test
Message Handler (e.g : /hello,/fush,/foo) : /hello,/world
File created /home/vvvv/project/app/bots/bot_ganteng.py
User for bot created!

```
The command will automatically create a user for the bot, and save a file to execute bot commands


You can customize the response bot in the file that was created
```python

async def execute_command(argument, group_room_code):
    return "Change this response!"
    
```

Activate your bot in room settings!

### Features
- Login and Register
- Any logged in user can create a room
- Authenticated user can generate new room code, and delete their own room
- Basic Bot feature
- Messages saved to database
- Messages from not logged in user will no saved to database

### Screenshots
Chat Section  

Chat template i got from https://github.com/amanastel/ChatApp (thx a lot for this guy)
