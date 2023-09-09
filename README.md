# discord_bot_for_minecraft

***For this to work, you will need to have already set up a minecraft server.***

1. Have minecraft server set up
2. copy these three files into your base directory for your server. Same directory as minecraft_server_1.20.1.jar, server.properties, etc
3. set up a discord server with at least 2 channels, one for up/down requests and one for server status
4. create a discord bot with read/send permissions
5. replace all [put_..._here] with proper values
6. Make an alias: `alias minecraftUp='java -Xms1024M -Xmx5G -jar minecraft_server_1.20.1.jar nogui'`
7. start server in a screen session, ie `screen -S minecraft` then `minecraftUp`. exit screen session with Ctrl+A+D
   (can use different screen name, but will need to edit up.sh and down.sh accordingly)
9. start bot in a screen session, ie `screen -S server_bot` then `python3 bot.py`. exit screen session with Ctrl+A+D
10. should now be able to bring up and down server with `/down` and `/up` being sent in the requests channel
