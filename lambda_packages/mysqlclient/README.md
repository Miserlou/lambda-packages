## Build

On an machine with Amazon Linux:

`./build.sh mysqlclient 1.3.14`

On a machine with docker and access to lambci images:

`docker run --rm -v `pwd`:/app lambci/lambda:build-python2.7 bash -c "cd /app && /app/build.sh --docker --py2-only mysqlclient 1.3.14"`

`docker run --rm -v `pwd`:/app lambci/lambda:build-python3.6 bash -c "cd /app && /app/build.sh --docker --py3-only mysqlclient 1.3.14"`
