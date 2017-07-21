#!/bin/bash

PACKAGE=${1:-paramiko}
VERSION=${2:-2.2.1}
CONTAINER_NAME="lambda-packages-$PACKAGE"

docker run --name ${CONTAINER_NAME} -v "$PWD":/var/task lambci/lambda:build-python2.7 \
bash build.sh ${PACKAGE} ${VERSION}

docker rm ${CONTAINER_NAME}
mv "${PACKAGE}-${VERSION}.tar.gz" "python2.7-${PACKAGE}-${VERSION}.tar.gz"
