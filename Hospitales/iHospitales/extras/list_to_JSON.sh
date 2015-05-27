#!/bin/bash
filename="$1"

echo "[" > output.json
while read -r line
do
	l=$line
	echo '"'"$l"'"', >> output.json
done < "$filename"

echo "]" >>output.json
