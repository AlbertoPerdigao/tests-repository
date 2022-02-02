**Installation commands**
```
pip install virtualenv    
virtualenv venv --python=python3
OR 
python -m virtualenv venv --python=python3
```

**Activate environment**
```
(Win) (Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser)
venv/Scripts/activate

(Linux/Mac)
source venv/Scripts/activate
```

**Execution File**
```
python my_app.py
```