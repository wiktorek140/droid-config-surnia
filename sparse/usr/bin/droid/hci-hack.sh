#!/bin/sh

# try to enforce reboot bluetooth service just after it launched and turn on hci0 device

/bin/systemctl restart bluetooth
sleep 3
/usr/sbin/hciconfig hci0 up
