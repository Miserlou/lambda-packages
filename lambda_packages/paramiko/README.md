## Build

`./create-build.sh`

## Test

- Deploys a lambda that imports paramiko and echos paramiko version

```bash
cd lambda;
virtualenv .env; source .env/bin/activate; pip install -r requirements.txt
zappa deploy test; zappa invoke test 'app.test'
```
