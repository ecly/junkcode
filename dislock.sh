#!/bin/bash

# Create folders if they don't exist
mkdir -p /mnt/bitlocker /mnt/mount

# Mount device to /mnt/bitlocker (prompts for sudo password and BitLocker password
sudo dislocker-fuse -V /dev/sdbX -u -- /mnt/bitlocker
