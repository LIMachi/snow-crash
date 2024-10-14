#!/bin/bash

files=$(find / -iname "*pass*" -type d 2>&1 | grep -v "denied")

for file in $files; do
    grep --color=always -n "flag01" "$file"
done
