
# Flask API RESTful CRUD con React

Este es un proyecto que consiste en una aplicación CRUD usando Flask, SQLAlchemy y MySQL para el backend, y React para el frontend.

## Requisitos

- Python 3
- MySQL
- Node.js y npm

## Configuración del entorno

### 1. Crear un entorno virtual

#### En Linux / macOS:
```sh
python3 -m venv <nombre_del_entorno>
```

#### En Windows:
```sh
python -m venv <nombre_del_entorno>
```

### 2. Activar el entorno virtual

#### En Linux / macOS:
```sh
source <nombre_del_entorno>/bin/activate
```

#### En Windows:
```sh
<nombre_del_entorno>\Scriptsctivate
```

### 3. Instalar dependencias del backend

```sh
pip install Flask Flask-SQLAlchemy PyMySQL python-dotenv
```

## Configuración de la base de datos

Antes de ejecutar la aplicación, debes configurar las siguientes variables de entorno:

```sh
MYSQL_USER=<tu_usuario>
MYSQL_PASSWORD=<tu_contraseña>
MYSQL_DATABASE=<nombre_de_la_base_de_datos>
MYSQL_HOST=<host_de_mysql>
```

## Instalación y ejecución del backend

1. Clona el repositorio:
```sh
git clone <url_del_repositorio>
```

2. Accede al directorio del proyecto:
```sh
cd <nombre_del_proyecto>
```

3. Instala las dependencias desde el archivo `requirements.txt`:
```sh
pip install -r requirements.txt
```

4. Ejecuta la aplicación:
```sh
python app.py
```

## Configuración del frontend (React)

### 1. Crear un proyecto React con Vite

Dentro del directorio del proyecto, crea una nueva aplicación React usando Vite:

```sh
npm create vite@latest frontend --template react
```

Accede al directorio del frontend:

```sh
cd frontend
```

### 2. Instalar dependencias

Instala las dependencias necesarias, como `axios` para las solicitudes HTTP:

```sh
npm install axios
```

### 3. Ejecutar la aplicación

Para iniciar el servidor de desarrollo de React:

```sh
npm run dev
```

