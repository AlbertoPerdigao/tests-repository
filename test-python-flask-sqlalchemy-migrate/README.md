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

**Environment variables**
```
(Win)
SET FLASK_APP=my_app.py

(Linux)
export FLASK_APP=my_app.py
```