#!/bin/bash
touch /tmp/valid
while true; do
    ln -sfn /home/user/level10/token /tmp/link
    ln -sfn /tmp/valid /tmp/link
done