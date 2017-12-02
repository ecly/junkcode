#!/bin/bash

# Require sudo
if [[ $UID != 0 ]]; then
    echo "Please run this script with sudo."
    exit 1
fi

# Create folders if they don't exist
mkdir -p /media/bitlocker /media/mount

echo "What is the partition name (can be found with 'lsblk') eg: sdb1"
read partition

# Mount device to /mnt/bitlocker (prompts for sudo password and BitLocker password
dislocker-fuse -V /dev/$partition -u -- /media/bitlocker

# Mount the dislocker file
mount -r -o loop /media/bitlocker/dislocker-file /media/mount

echo "Mounted partition at /media/mount"
