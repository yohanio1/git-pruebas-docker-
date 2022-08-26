# git-pruebas-docker-
Repositorios que contiene proyectos utilizando Docker.

## **app-ubuntu**
Es una aplicación simple, la cual parte de una imagen base de ubuntu:18.04 para entrar al shell y utilizar la orden echo 

```dockerfile
FROM ubuntu:18.04
ENTRYPOINT ["/bin/echo"] 
CMD ["Hola from ubuntu"]
}
```
```bash
  docker build -t image_name .
```
Creada la imagen, bastaría escribir el comando 

```bash
  docker run image_name "texto"
```
para crear el contenedor de la imagen `image_name` y ver la salida del comando echo:  

`echo escribe cada una de las cadenas dadas en su salida estándar, con un espacio en blanco
entre cada una y un carácter "salto de línea" después de la última cadena.`

## **app-compose-node**

Es una aplicación que intenta simular un entorno de pruebas, utilizando el framework de testing javascript **Jest**.
El archivo Dockerfile estaría compuesto por las siguientes lineas.

```dockerfile

FROM node:18-alpine3.15
WORKDIR /usr/share/
COPY package* ./  
RUN npm install 

```

Como se nota se parte de una imagen base de node.  
En esta imagen se accede a la dirección de fichero `/ur/share/` y se le copian los archivos que comienzan con la palabra `package`, para luego correr la instalación de los `node_modules`.  
Luego en el archivo `docker-compose.yml` se le asignan las instrucciones para crear el contenedor.  

```yaml
version: "3.8"
services:
  jest:
    build: 
      context: .
      dockerfile: Dockerfile
    container_name: test-container
    volumes:
      - ./JS_Examples/:/usr/share/unit_test
    command: npm test
```
Ya solo bastaría escribir en el shell, en la ruta donde se tiene el docker-compose.yml
```bash
docker-compose up
```
Para desplegar el unit test del proyecto ejemplo.

## **app-compose-python**

Es una aplicación que intenta simular un entorno de pruebas, utilizando el marco de prueba de python **Pytest**.
El archivo Dockerfile estaría compuesto por las siguientes lineas.

```dockerfile

FROM python:3.11-rc-alpine3.15
RUN pip install pytest

```

Como se nota se parte de una imagen base de python donde se instala el módulo `pytest`.
Luego en el archivo `docker-compose.yml` se le asignan las instrucciones para crear el contenedor.

```yaml
version: "3.8"
services:
  python:
    build:
      context: .      
      dockerfile: Dockerfile
    container_name: python-container
    volumes:
      - ./PY_Examples/:/usr/src/app
    command: pytest -v /usr/src/app
```
Para este caso se copia la información de la carpeta `PY_Examples` dentro de la ruta `/usr/src/app` del contenedor y se ejecuta el comando `pytest -v /usr/src/app`.  
Ya solo bastaría escribir en el shell, en la ruta donde se tiene el docker-compose.yml
```bash
docker-compose up
```
Para desplegar el unit test del proyecto ejemplo utilizando pytest.

## **Flask-docker**

Tomado del getting-start de la página oficial de docker. En este proyecto se despliega una web application que muestra un Hello world utilizando el framework de python **Flask**.   

```dockerfile

# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

```

Como se nota se parte de una imagen base de python donde se instala el módulo Flask y se copian todos los archivos que se encuentran en la carpeta a la ruta `/app`.  
El archivo python tendría la siguiente información:
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker!'
```
Luego para construir la imagen se utilizaría el comando:
```bash
  docker build -t image_name .
```
Para correr la imagen se debe tener en cuenta hacer un port mapping, es decir, se tiene que mapear el puerto expuesto por el container, en el host local.
```bash
  docker run -p 8000:5000 image_name
```

## **mysqldb_flask_docker-compose**

Tomado del getting-start de la página oficial de docker. En este proyecto se crea una aplicación web que muestra la información de una base de datos.  

```dockerfile

# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

```

Como se nota se parte de una imagen base de python donde se instala el módulo Flask y se copian todos los archivos que se encuentran en la carpeta a la ruta `/app`.  
El archivo `docker-compose-yml` tendría la siguiente información:
```yaml
version: '3.8'

services:
 web:
  build:
   context: .
  ports:
  - 8000:5000
  volumes:
  - ./:/app

 mysqldb:
  image: mysql
  ports:
  - 3306:3306
  environment:
  - MYSQL_ROOT_PASSWORD=p@ssw0rd1
  volumes:
  - mysql:/var/lib/mysql
  - mysql_config:/etc/mysql

volumes:
  mysql:
  mysql_config:
```
En este `docker-compose` se instrucciona para que de la ruta actual se cree el container en base a la imagen de flask y en base a una imagen de mysql.  
Se mapean los puertos de los contenedores.  
Y se crean los volumenes locales para almacenar la información de la base de datos.  
El archivo python contendría la siguiente información:
```python
import mysql.connector
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, Docker!'

@app.route('/widgets')
def get_widgets():
  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1",
    database="inventory"
  )
  cursor = mydb.cursor()


  cursor.execute("SELECT * FROM widgets")

  row_headers=[x[0] for x in cursor.description] #this will extract row headers

  results = cursor.fetchall()
  json_data=[]
  for result in results:
    json_data.append(dict(zip(row_headers,result)))

  cursor.close()

  return json.dumps(json_data)

@app.route('/initdb')
def db_init():
  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1"
  )
  cursor = mydb.cursor()

  cursor.execute("DROP DATABASE IF EXISTS inventory")
  cursor.execute("CREATE DATABASE inventory")
  cursor.close()

  mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1",
    database="inventory"
  )
  cursor = mydb.cursor()

  cursor.execute("DROP TABLE IF EXISTS widgets")
  cursor.execute("CREATE TABLE widgets (name VARCHAR(255), description VARCHAR(255))")
  cursor.close()

  return 'init database'

if __name__ == "__main__":
  app.run(host ='0.0.0.0')
```
Este archivo `python`indica dos acciones dependiendo de la ruta que se ponga en el navagador.  
Si se entrá a la ruta **`/initdb`**: se ejecutará el código para entrar a la base de datos con las credenciales configuradas, borrar la base de datos `inventory` si existe y crear una base de datos `inventory`.  
Luego borrará la tabla `widgets` si existe y creará la tabla `widgest` con los campos `name` y `description`.  
Y mostrará en la página web `init database`.  
  
Si se entra a la ruta **`/widgets`**: se ejcutará el código para entrar a la base de datos, eligir el base de datos llamada `inventory`, seleccionará toda la información de la tabla `widget` y retornará en la web la información en formato json de lo que hay en la tabla.

```bash
  docker-compose up -d --build
```
Si se quiere adjuntar información se puede ejecutar el comando:
```bash
docker exec -it container_name mysql -u root -p inventory
```
El cual abrirá la terminal de mysql entrando a la base de datos `inventory`, y a través de comandos sql se puede agregar la información para luego visualizarla en la web.  
Un comando básico para insertar un dato en la tabla `widgets` sería:
```sql
INSERT INTO widgets (name, description) VALUES ("Juan","Humano");
```
## **python-app-virtual**

Aplicación simple que ejecuta aplicaciones de python desde una imagen de ubuntu instalandole python.  

**Dockerfile**
```dockerfile

FROM ubuntu:18.04
RUN apt update
RUN apt install -y python3-pip
RUN apt install -y nano
WORKDIR /usr/scr/myapp
COPY app.py app.py 
CMD ["python3","/usr/scr/myapp/app.py"]

```
**python**

```python

for i in range (3):
	print(i)

```
**comandos**
```bash
docker build -t image_name
```

```bash
docker run image_name
```
**Nota**: uno de los primeros proyectos que cree. Una mejora que se le podría hacer es crear un `docker-compose.yml` en el cual se creara un volumen donde se le pasara el archivo de la app de python y crear un `Dockerfile` que solo contuviera la instalación de python. De esta manera se haría una imagen más general y cada vez que se intentara ejecutar un script de python no se tuviera que crear su imagen.

## **sonarQube**
Proyecto para desplegar la plataforma de código estático sonarQube para evaluar código fuente.  
Este proyecto contiene dos archivos yml para los contenedores a crear `scanner.yml` y `sonar.yml`.  
sonar
```yaml
version: '3.8'
 
services:
  sonarqube:
    image: sonarqube:8-community
    ports:
      - "9000:9000"
    volumes:
      - sonarqube_conf:/opt/sonarqube/conf
      - sonarqube_data:/opt/sonarqube/data
      - sonarqube_extensions:/opt/sonarqube/extensions
      - sonarqube_bundled-plugins:/opt/sonarqube/lib/bundled-plugins
volumes:
  sonarqube_conf:
  sonarqube_data:
  sonarqube_extensions:
  sonarqube_bundled-plugins:
```
scanner
```yaml
version: '3.8'
 
services:

  scanner:
    image: sonarsource/sonar-scanner-cli
    network_mode: "host"
    environment:
      - SONAR_HOST_URL="http://127.0.0.1:9000"
    volumes:
      - ./pyton-application:/usr/src
      - ./scanner/sonar-config:/opt/sonar-scanner/conf/
```
`sonar.yml` despliega el contenedor con la plataforma web de sonarQube en el puerto `9000`, y carga toda la información necesaria para desplegarlo en los volumenes.  
`scanner.yml` despliega el contenedor con el scanner, en el cual se le pasa el archivo de configuración del escaner y la aplicaciones a la que se le va a realizar el escaneo.

**configuración del escaner**
```
sonar.projectKey=name_project
sonar.sources=. 
sonar.host.url=http://localhost:9000 
sonar.login=677bb790a734ca080e1c21a69c8023b503efc097
sonar.python.coverage.reportPaths=/usr/src/coverage.xml
```
Luego se correran los dos archivos yml así:

```bash
docker-compose -f sonar.yml up -d 
``` 
y luego para ejecutar el escaner:
```bash
docker-compose -f scanner.yml up
``` 


