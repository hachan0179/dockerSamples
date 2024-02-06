#!/bin/bash

#CONF
LOCAL_PORT=8080
APP_PORT=8080

#NAME
THIS_NAME='run.sh'
IMAGE_NAME='bottle-app'
CONTAINER_NAME='bottle-container'

#FUNCTION
while (( $# > 0 ))
do
  case $1 in
    -b | --build)
      echo ">> docker build -t $IMAGE_NAME ."
      docker build -t $IMAGE_NAME .
      exit 0
      ;;
    -r | --run)
      echo ">> docker run -it -d --rm -p $LOCAL_PORT:$APP_PORT --name $CONTAINER_NAME $IMAGE_NAME"
      docker run -it -d --rm -p $LOCAL_PORT:$APP_PORT --name $CONTAINER_NAME $IMAGE_NAME 
      exit 0
      ;;
    -s | --stop)
      echo ">> docker stop $CONTAINER_NAME"
      docker stop $CONTAINER_NAME
      exit 0
      ;;
    -c | --clear)
      echo ">> docker image rm $IMAGE_NAME"
      docker image rm $IMAGE_NAME
      exit 0
      ;;
    -e | --exec)
      echo ">> docker exec -it $CONTAINER_NAME bash" 
      docker exec -it $CONTAINER_NAME bash
      exit 0
      ;;
    -* | --*)
      echo "Invailed option"
      ;;
  esac
  shift
done

echo "Usage : ./$THIS_NAME [AN OPTION]"
echo "Options:"
echo "  -b  --build     Build the docker image"
echo "  -r  --run       Run the docker image"
echo "  -s  --stop      Stop the docker container"
echo "  -e  --exec      Execute bash in runnig contaicer"
echo "  -c  --clear     Delete the docker image"
