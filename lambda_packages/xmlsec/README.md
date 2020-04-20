## Build

```
./build.sh xmlsec 1.0.9
```

### Docker

```bash
docker build --tag xmlsec:latest .
# Do whatever to make the container exist
docker run -it --name xmlsecbuild xmlsec:latest /bin/bash
docker container cp xmlsecbuild:/workon/python3.8-xmlsec-1.3.3.tar.gz .
```
