#!/bin/bash

echo it starts

i=1
while [ $i -le 5 ]; do
    echo "i is $i"
    i=$(( i + 1 ))
done