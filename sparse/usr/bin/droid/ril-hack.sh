#!/bin/sh

# check if exist ril1 device

if [ -e /dev/socket/rild2 ] ; then
   echo "[ril_1]" >> ril_subscription.conf
   echo "socket=/dev/socket/rild2" >> ril_subscription.conf
fi
