#!/bin/bash

PACKAGE=${1}
VERSION=${2}
TMP_DIR="${PACKAGE}_${VERSION}"

mkdir ${TMP_DIR}
cd  ${TMP_DIR}
echo "Packaging ${PACKAGE}"

echo "do update"
sudo yum update -y

sudo yum groupinstall -y "Development Tools"

echo "do dependency install"

sudo yum install -y gcc libffi-devel python-devel

ENV="env-${PACKAGE}-${VERSION}"

echo "make ${ENV}"
virtualenv "${ENV}"

echo "activate env in `pwd`"
source "${ENV}/bin/activate"

# https://github.com/pypa/pip/issues/3056
echo '[install]' > ./setup.cfg
echo 'install-purelib=$base/lib64/python' >> ./setup.cfg


TARGET_DIR=${ENV}/packaged
echo "install pips"
pip install --verbose --no-dependencies --target ${TARGET_DIR} "${PACKAGE}==${VERSION}"
deactivate

cd ${TARGET_DIR} && tar -zcvf ../../../${PACKAGE}-${VERSION}.tar.gz * && cd ../../..
rm -rf ${TMP_DIR}




