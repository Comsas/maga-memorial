## How to configure the projet

1. Create a virtual environment and activate  
```
virtualenv -p python3 /path/to/env
source /path/to/env/bin/activate
```

2. Install requirements  
```
pip install -r requirements.txt
```

3. Run migrations and startserver  
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
