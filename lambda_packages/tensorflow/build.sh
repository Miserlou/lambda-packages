#!/bin/bash

if [ -z "${1}" ]
then
    echo "usage: build.sh version"
    exit 1;
fi

VERSION=${1}
TMP_DIR="tensorflow_${VERSION}"

mkdir ${TMP_DIR}
cd  ${TMP_DIR}
echo "Packaging ${PACKAGE}"

echo "do update"
sudo yum update -y

sudo yum groupinstall -y "Development Tools"

echo "do dependency install"

# JDK 8: https://medium.com/@mertcal/easily-install-oracle-jdk8-on-your-ec2-instance-9317644a42fa
sudo wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-cookie" "https://download.oracle.com/otn-pub/java/jdk/8u51-b16/jdk-8u51-linux-x64.rpm"
sudo rpm -ivh jdk-8u51-linux-x64.rpm

# Bazel
wget https://github.com/bazelbuild/bazel/releases/download/0.4.5/bazel-0.4.5-installer-linux-x86_64.sh
sudo bash bazel-0.4.5-installer-linux-x86_64.sh

# Python dependencies
sudo yum install python27-devel -y
sudo pip install numpy wheel

# Clone the repo
git clone https://github.com/tensorflow/tensorflow
cd tensorflow
git checkout r${1}

# Build TensorFlow. This takes about 26 minutes
PYTHON_BIN_PATH=/usr/bin/python CC_OPT_FLAGS="-march=native" \
TF_NEED_JEMALLOC=1 TF_NEED_GCP=0 TF_NEED_HDFS=0 TF_ENABLE_XLA=0 \
TF_NEED_OPENCL=0 TF_NEED_CUDA=0 PYTHON_LIB_PATH="/usr/local/lib64/python2.7/site-packages" ./configure
JAVA_HOME=/usr/java/latest bazel build -c opt //tensorflow/tools/pip_package:build_pip_package

# Install into a new directory
bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg/
sudo pip install --upgrade pip
mkdir package
/usr/local/bin/pip install --no-dependencies --target package/ /tmp/tensorflow_pkg/*.whl

# Make it smaller
cd package
rm -rf external
rm -rf tensorflow/examples
rm -rf tensorflow/tools
rm -rf tensorflow/tensorboard
for f in $(find . | grep '.so$')
do
    strip -x $f
done

# Archive it
tar cvzf ~/tensorflow-${1}.tar.gz * && cd ~/
