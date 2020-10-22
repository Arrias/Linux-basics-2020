#!/bin/bash
path=$1
commit=$(cat $path)
if [[ "$commit" =~ "^issue-[0-9]{1,} *" ]];then
  echo OK
  exit 0
else
  echo fail
  exit 1
fi