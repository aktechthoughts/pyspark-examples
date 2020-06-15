#!/bin/bash

if [ "A$1"  == "A" ];
then
docker run --name pyspark-examples_master_1 \
      -p 8080:8080 \
      -v /home/abhishek/PycharmProjects/pyspark-examples/app:/app \
      -v /home/abhishek/PycharmProjects/pyspark-examples/config:/app/config \
      -d -t aktechthoughts/pyspark_app:latest
else
docker exec pyspark-examples_master_1 \
      python3 $1
fi




