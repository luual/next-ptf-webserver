# Dependencies

* flask
* flask-sock
* flask-cors


# Install

```
python -m venv venv
```

## Activate 

On windows

```
./venv/Script/Activate.ps1
```

on Mac

```
source ./bin/activate
```

then install dependancies with

```
pip install -r requirements.txt
```


Start with 
```
flask run --host=0.0.0.0

# flask run --debug --host=0.0.0.0
```

## Tests

```
python -m pytest tests
```