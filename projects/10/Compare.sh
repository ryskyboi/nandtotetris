#!/bin/bash

dir=$1

for file in $(comm -12 <(ls -1 $dir | sort) <(ls -1 $dir/MyXml | sort))
do
  "../../tools/TextComparer.sh" "$dir/$file" "$dir/MyXml/$file"
done