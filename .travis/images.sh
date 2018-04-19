#!/bin/bash
for i in ubuntu-molecule:18.04 ubuntu-molecule:16.04
do 
    docker pull paulfantom/$i &
done

wait
