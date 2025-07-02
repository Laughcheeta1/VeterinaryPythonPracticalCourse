# Creadores
## Santiago Yepes Mesa
[LinkedIn](https://www.linkedin.com/in/santiago-yepes-mesa-67ab80270)

## Simon Gomez Castro
[LinkedIn](https://www.linkedin.com/in/sgc-9149b4243/)

# Guia de Sistema de Veterinaria Amigos Peludos
## Como iniciar la aplicacion?
### 1. Para iniciar la aplicacion tiene que tener primero instalado python, y ademas instalar las dependencias definidas en el archivo `requirements.txt` ejecutando el siguiente comando:
```bash
pip install -r requirements.txt
```

### 2. Una vez instaladas las dependencias, debe crear una base de datos. Para ello, primero debe crear un archivo  `.env` en la raiz del proyecto y definir las variables de entorno necesarias. Un ejemplo de este archivo es el siguiente:
```env
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=Veterinaria_Python_Practical_Course
DATABASE_USER=<tu usuario>
DATABASE_PASSWORD=<tu contraseña>
DATABASE_HOST=127.0.0.1
DATABASE_PORT=5432
```
`Nota`: Esta configuracion es para una base de datos PostgreSQL, si desea utilizar otro motor de base de datos, debe cambiar la variable `DATABASE_ENGINE` y las demas variables segun corresponda, ademas de instalar la libreria de python correspondiente. En el archivo `requirements.txt` ya se encuentra incluida la libreria para PostgreSQL.

### 3. Crear las tablas necesarias en la base de datos
Para crear las tablas en la base de datos (hacer las migraciones), debe ejecutar los siguientes comandos:
```bash
python manage.py makemigrations
python manage.py migrate

python manage.py makemigrations users pets appointments
python manage.py migrate users
python manage.py migrate pets
python manage.py migrate appointments
```

### 4. Una vez hecho esto, puede iniciar la aplicacion ejecutando el siguiente comando:
```bash
python manage.py runserver
```

## Panel de Administrador y Creacion de superusuario
### Super Usuario
Para crear un superusuario que pueda acceder al panel de administrador, debe ejecutar el siguiente comando:
```bash
python manage.py createsuperuser
```
Una vez ahi, va a ingresar la informacion que le pidan.
Y viola! Ya tienes un superusuario creado. Con este podras acceder al panel de administrador de Django.

### Panel de Administrador
Para acceder al panel de administrador, debe correr su aplicacion, abrir su navegador y dirigirse a la siguiente URL:
```
http://<link de la pagina>:<puerto>/admin/
```
Por ejemplo, si esta ejecutando la aplicacion en su maquina local, la URL seria:
```
http://127.0.0.1:8000/admin/
```
U otra forma mas facil seria al correr la aplicacion, hacer click en el link que aparece en la terminal, y en en su buscador, a la url, anadirle `/admin/` al final.

Una vez este en este link, le van a pedir que ingrese el usuario y la contrasena del superusuario que acaba de crear. Una vez que ingrese, va a poder acceder al panel de administrador de Django.
