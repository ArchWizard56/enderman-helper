# Enderman Server Bot
This bot automates interaction with my minecraft server hosted on enviromc. This bot uses a combination of the discordconsole plugin and the pterodactyl .7 api

## Using on your server

### Install requirements
```
$ pip install -r requirements.txt
```

### Update configuration file
Copy `config-default.ini` to `config/config.ini` and update the values in the file.

### Start the server
```
$ python main.py
```

### Or run with Docker
```
$ docker build --tag endermanhelper:v1 .
$ docker run --rm -v $PWD/config:/app/config endermanhelper:v1
```