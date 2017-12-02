#!/bin/bash

# Require sudo
if [[ $UID != 0 ]]; then
    echo "Please run this script with sudo."
    exit 1
fi

umount /media/mount
umount /media/bitlocker
