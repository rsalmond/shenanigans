#!/bin/bash

curl "https://api.hipchat.com/v1/rooms/message?format=json&auth_token=$HC_TOKEN&message=$1&room_id=$HC_ROOM&from=Shenanigans"
