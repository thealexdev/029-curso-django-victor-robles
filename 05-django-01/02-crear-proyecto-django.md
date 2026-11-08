### Crear un nuevo proyecto de Django

```bash
django-admin startproject <nombre_proyecto>
```

### Crear la base de datos con los modelos definidos (ORM)

```bash
python manage.py migrate
```

### Crear aplicaciones de Django

```bash
python manage.py startapp <nombre_app>
```

- Esta aplicación creada debe agregarse en los settings del core del proyecto.
