#!/usr/bin/env bash

# surfaceflinger needs to run for a bit, in order for sailfish graphics to work
# very weird, proper solution needed
rm /tmp/start_surfaceflinger
/system/bin/surfaceflinger &
PID=$!
sleep 5
kill -9 $PID
sleep 5
touch /tmp/start_surfaceflinger
killall minisfservice

