#!/bin/bash

# Script to bring up the server

# check if server is already up
if [[ $(ps aux | grep minecraft_server_1.20.1 | grep -v grep) ]]; then
	echo "server is already up"
else
	echo "bringing server up"
	# I have the following alias for minecraftUp
	# alias minecraftUp='java -Xms1024M -Xmx5G -jar minecraft_server_1.20.1.jar nogui'
	# the ^M represents hitting return and running the command
	screen -S minecraft -p 0 -X stuff "minecraftUp^M"
	# wait for server to be up
	while [[ -z $(ps aux | grep minecraft_server_1.20.1 | grep -v grep) ]]
	do
		# as long as the server is not up, wait 3 seconds and try again
		sleep 3
	done
	echo "server is up :arrow_up:"
fi
