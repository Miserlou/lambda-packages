# pylibmc

Built based on https://github.com/bxm156/pylibmc-manylinux/blob/master/.travis.yml

## On an machine with Amazon Linux:

`./build.sh pylibmc 1.5.2`

On a machine with docker and access to lambci images:

```
docker run --rm -v `pwd`:/app -d lambci/lambda:build-python2.7 bash -c "cd /app && /app/build.sh --docker --py2-only pylibmc 1.5.2"
```

```
docker run --rm -v `pwd`:/app -d lambci/lambda:build-python3.6 bash -c "cd /app && /app/build.sh --docker --py3-only pylibmc 1.5.2"
```
