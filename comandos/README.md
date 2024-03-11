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

```
# Tudo isso é feito na memória
python manage.py shell
from contact.models import Contact
Contact
<class 'contact.models.Contact'>
c = Contact(first_name='Gustavo') 
c
<Contact: Gustavo >
c.save

c.last_name = 'Silva'
c.save()
c.phone = '543675'
c.save()
c.delete()

# lembrando que isso está na memória se eu der c.save() ele salva um novo contato com todas essas informações que estão na memória
```