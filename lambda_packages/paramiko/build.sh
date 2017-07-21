#!/bin/bash

PACKAGE=${1}
VERSION=${2}
TMP_DIR="${PACKAGE}_${VERSION}"

mkdir ${TMP_DIR}
cd  ${TMP_DIR}
echo "Packaging ${PACKAGE} ${VERSION} ..."

yum update -y

yum groupinstall -y "Development Tools"

echo "do dependcy install"
yum install libffi-devel openssl-devel

ENV="env-${PACKAGE}-${VERSION}"
echo "make ${ENV}"
virtualenv "${ENV}"
source "${ENV}/bin/activate"

# https://github.com/pypa/pip/issues/3056
echo '[install]' > ./setup.cfg
echo 'install-purelib=$base/lib64/python' >> ./setup.cfg

TARGET_DIR=${ENV}/packaged
echo "install pips"
pip install --verbose --use-wheel --no-dependencies --target ${TARGET_DIR} "${PACKAGE}==${VERSION}"
deactivate

cd ${TARGET_DIR} && tar -zcvf ../../../${PACKAGE}-${VERSION}.tar.gz * && cd ../../..
rm -rf ${TMP_DIR}
rm -rf ${ENV}
