# Pre-setup

## Create a virtual environment

```
python3 -m venv venv
```

## Activate the virtual environment

```
source venv/bin/activate
```

## Install dependencies

```
pip install -r requirements.txt
```

## Apply the migrations

```
python manage.py migrate
```

## Run the project

```
python3 manage.py runserver
```

# Usage

### Home page

```
http://127.0.0.1:8000/
```

### Register a user

```
http://127.0.0.1:8000/users/register/
```

### Login

```
http://127.0.0.1:8000/users/login/
```

### List of all topics

```
http://127.0.0.1:8000/topics/
```

### Detail of the each topic

```
http://127.0.0.1:8000/topics/topic_id/
```

Where ```topic_id``` is the unique primary key for each topic.

Here you also can see all entries according to this topic.

### Add a new entry to the topic

```
http://127.0.0.1:8000/new_entry/topic_id/
```

### Edit the entry

```
http://127.0.0.1:8000/edit_entry/topic_id/
```
