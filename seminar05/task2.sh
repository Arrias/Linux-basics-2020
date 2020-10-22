#!/bin/bash
left=$1
right=$2
git log --pretty=format:"%s" > log.txt

touch "releases_notes.md"
online=0

while read -r LINE;
   do
    if [[ $LINE == "$left" ]]; then
        online=1
    fi
    if [[ "$online" == "1" ]]; then
        echo $LINE >> "release_notes.md"
    fi
    if [[ $LINE == "$right" ]]; then
        break
    fi
   done < "log.txt"

