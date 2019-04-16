#!/bin/bash
#
# Script to build cryptography and/or related python packages for lambda.
#
# Requires two arguments: package and version.
#
# You can use it to build inside an Amazon Linux AMI (default) or with docker
# with --docker (you need docker installed and network access to reach lambci's
# docker-lambda image).
#
# Defaults to building python2.7, python3.6 and python 3.7 packages. If you only want
# one of them use --py2.7-only or --py3.6-only or --py3.7-only.
#
set -e

DOCKER=0
PY27=1
PY36=1
PY37=1
SUDO=sudo

while [[ $# -gt 2 ]]
do
key="$1"

case $key in
    --docker)
        DOCKER=1
        SUDO=""
        shift
        ;;
    --py2.7-only)
        PY27=1
        PY36=0
        PY37=0
        shift
        ;;
    --py3.6-only)
        PY27=0
        PY36=1
        PY37=0
        shift
        ;;
    --py3.7-only)
        PY27=0
        PY36=0
        PY37=1
        shift
        ;;
    *)
        shift
        ;;
esac
done

PACKAGE=${1}
VERSION=${2}

echo DOCKER          = "${DOCKER}"
echo PY27            = "${PY27}"
echo PY36            = "${PY36}"
echo PY37            = "${PY37}"
echo PACKAGE         = "${PACKAGE}"
echo VERSION         = "${VERSION}"

function build_package {
    PACKAGE=${1}
    VERSION=${2}
    PYTHON=${3}
    PIP=${4}
    VIRTUALENV=${5}

    TMP_DIR="${PYTHON}_${PACKAGE}_${VERSION}"

    mkdir ${TMP_DIR}
    cd  ${TMP_DIR}

    echo "install dependencies"
    ${SUDO} yum install -y yum-plugin-ovl
    ${SUDO} yum update -y
    ${SUDO} yum groupinstall -y "Development Tools"
    ${SUDO} yum install -y libffi libffi-devel openssl openssl-devel
    if [ "${VIRTUALENV}" == "virtualenv" ]; then
        ${SUDO} ${PIP} install virtualenv
    fi

    echo `${PYTHON} --version`
    
    echo "make virtualenv"
    ENV="env-${PYTHON}-${PACKAGE}-${VERSION}"
    echo ${VIRTUALENV} "${ENV}"
    ${VIRTUALENV} "${ENV}"

    echo "activate env in `pwd`"
    echo source "${ENV}/bin/activate"
    source "${ENV}/bin/activate"

    # https://github.com/pypa/pip/issues/3056
    echo '[install]' > ./setup.cfg
    echo 'install-purelib=$base/lib64/python' >> ./setup.cfg

    echo "install pips"
    TARGET_DIR=${ENV}/packaged
    echo ${PIP} install --verbose --no-dependencies --target ${TARGET_DIR} "${PACKAGE}==${VERSION}"
    ${PIP} install --verbose --no-dependencies --target ${TARGET_DIR} "${PACKAGE}==${VERSION}"
    deactivate

    TARGET_DIR=${ENV}/packaged
    cd ${TARGET_DIR} && tar -zcvf ../../../${PYTHON}-${PACKAGE}-${VERSION}.tar.gz * && cd ../../..
    rm -r ${TMP_DIR}
}

if [ ${PY27} == 1 ]; then
    build_package ${PACKAGE} ${VERSION} python2.7 pip virtualenv
fi

if [ ${PY36} == 1 ]; then
    build_package ${PACKAGE} ${VERSION} python3.6 pip3.6 "python3.6 -m venv "
fi

if [ ${PY37} == 1 ]; then
    build_package ${PACKAGE} ${VERSION} python3.7 pip3.7 "python3.7 -m venv "
fi
