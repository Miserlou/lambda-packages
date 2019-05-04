#!/bin/bash

PILVER=3.4.2

set -ex
set -o pipefail

prefix="pillow-build"
bucket="<YOUR BUCKET>"
region="<YOUR REGION>"

echo "do update"
sudo yum update -y

echo "do dependency install"
sudo yum install -y \
	gcc \
	libtiff-devel \
	libzip-devel \
	libjpeg-devel \
	freetype-devel \
	lcms2-devel \
	libwebp-devel \
	tcl-devel \
	tk-devel

echo "copy webp deps"
cd /usr/lib64/ 
find . -name "*webp*" | cpio -pdm ~/env/lib64/python2.7/site-packages/
cd ~/
chmod 755 -R env/lib64/python2.7/site-packages/

echo "make env"
/usr/bin/virtualenv \
	--python /usr/bin/python env \
	--always-copy

echo "activate env in `pwd`"
source env/bin/activate

echo "install pips"
pip install --verbose Pillow==${PILVER}
deactivate

echo "tar lib and lib64"
mkdir Pillow-${PILVER}
cp -a env/lib64/python2.7/site-packages/PIL Pillow-${PILVER}/
cp -a env/lib64/python2.7/site-packages/libwebp* Pillow-${PILVER}/
strip -x Pillow-${PILVER}/PIL/*.so
cd Pillow-${PILVER}/ && tar -zcvf ../Pillow-${PILVER}.tar.gz * && cd ..

#make lambda test
cd Pillow-${PILVER}/
wget https://raw.githubusercontent.com/Miserlou/lambda-packages/master/lambda_packages/Pillow/test/test.jpg
wget https://raw.githubusercontent.com/Miserlou/lambda-packages/master/lambda_packages/Pillow/test/test.py
zip -r9 ../test.zip * && cd ..

if [ "$bucket" != "<YOUR BUCKET>" ] && [ "$region" != "<YOUR REGION>" ]
	then
		echo "uploading to $bucket in $region"
		aws s3 cp test.zip s3://$bucket/$dir/test.zip --region $region
		aws s3 cp Pillow-${PILVER}.tar.gz s3://$bucket/$dir/Pillow-${PILVER}.tar.gz --region $region
fi
