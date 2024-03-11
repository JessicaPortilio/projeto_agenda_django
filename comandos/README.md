Ambiente Virtual
```
python -m venv venv

venv\Scripts\activate
```

Installando django e criando o ínicio do proje

```
pip install django

django-admin startproject project .

```

Subindo o serve para ver se está funcionando

```
python manage.py runserver
```

Criando o projeto 

```
python manage.py startapp contact
```

Migrando a base de dados do Django
```
python manage.py makemigrations
python manage.py migrate
```

Criando e modificando a senha de um super usuário Django
```
python manage.py createsuperuser
python manage.py changepassword USERNAME
```