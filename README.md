# Run locally
## Create this first in the cloned repository directory
```shell
$ mkdir entrypoints
$ cd entrypoints 
$ echo -e "export database_password='user'\nuvicorn main:app --reload" > run_local.sh
$ cd ..
```

## Now run this to install the required libraries 
```shell
$ pip install -r requirements.txt

```

## Finally run this to start the app
```shell
$ entrypoints/run_local.sh

```
