#!/bin/bash

# Script to bring down server

# check if server is up (running processes that contain "minecraft_server_1.20.1" and don't contain "grep" (this command))
if [[ $(ps aux | grep minecraft_server_1.20.1 | grep -v grep) ]]; then
    # check if anyone else currently has an established connection to the server
    if [[ $(lsof -iTCP:[put_your_port_here] -sTCP:ESTABLISHED) ]]; then
        echo "Players still in sever, leaving server up for them"
    else
        echo "bringing server down"
        screen -S minecraft -p 0 -X stuff "stop^M"
        # wait for server to be down
        while [[ $(ps aux | grep minecraft_server_1.20.1 | grep -v grep) ]]
        do
            # as long as the server is still up, wait 3 seconds and check again
            sleep 3
        done
        echo "server is down :arrow_down:"
    fi
else
    echo "server is already down"
fi
