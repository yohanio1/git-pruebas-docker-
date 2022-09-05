# git-pruebas-docker-
Repositorios que contiene proyectos utilizando Docker.

## **app-ubuntu**
Es una aplicación simple, la cual parte de una imagen base de ubuntu:18.04 para entrar al shell y utilizar la orden echo 

```dockerfile
FROM ubuntu:18.04
ENTRYPOINT ["/bin/echo"] 
CMD ["Hola from ubuntu"]

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
## **Selenium**

### `selenium-app.py`  

Aplicacion utilizando el módulo de unittest para desarrollar diferentes test.  
La lógica de este programa sería:  
* Ejecuta la función `setUp`
* Ejecuta el primer test `test_search_in_python_org`
* Ejecuta la función `tearDown`
* Vuelve a la función `setUp`
* Ejecuta el siguiente test `test_search_in_xchrome`  
* Ejecuta la función `tearDown`

Este ciclo se repite hasta que se termine la totalidad de los test.  
#### **tests**
```python
def test_search_in_python_org(self):
    driver = self.driver
    driver.get("http://www.python.org")
    self.assertIn("Python", driver.title)
```
Este test consiste en entrar a la página oficial de python y verificar que el título de la página corresponde con `Python`
```python
def test_search_in_xchrome(self):   
    driver = self.driver
    driver.get("http://www.google.com.co")
    elem = driver.find_element(By.NAME,"q")
    elem.send_keys("Hola esto es una prueba")
    elem.send_keys(Keys.RETURN)
    self.assertIn("Ver todos", driver.page_source)
```
Este test consiste en entrar al buscador de google y escribir en él, el texto `Hola esto es una prueba`, darle buscar y verificar que en la fuente de la página se encuentra la palabra `Ver todos`

```python
def test_search_by_xpath(self):   
    driver = self.driver
    driver.get("http://www.google.com.co")
    elem = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
    elem.send_keys("Hola esto es una prueba")
    elem.send_keys(Keys.RETURN)
    self.assertIn("Ver todos", driver.page_source)
```
Utilizando la opción de la búsqueda con XPATH, se realiza el mismo test descripto anteriormente.
```python
def test_change_window(self):   
    driver = self.driver
    driver.get("http://www.google.com.co")
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://accounts.google.com")
    elem = driver.find_element(By.XPATH,"//*[@id='identifierId']")
    elem.send_keys("juane.acevedoc@gmail.com")
    elem.send_keys(Keys.RETURN)
    time.sleep(3)
```
Este test consiste en entrar a la página de Google, abrir otra ventana, cambiar de ventana, entrar a la dirección de gmail, y introducir el correo electrónico.

```python
def test_back_forward(self):   
    driver = self.driver
    driver.get("http://www.google.com.co")
    time.sleep(3)
    driver.get("https://www.youtube.com")
    time.sleep(3)
    driver.back()
```
Este test consiste en entrar a Google, esperar, entrar a youtube, esperar y volver a la página anterior (Google).
```python
def test_toggle_click(self):   
    driver = self.driver
    driver.get("https://www.w3schools.com/howto/howto_css_switch.asp")
    select = driver.find_element(By.XPATH,"//*[@id='main']/label[3]/div")
    select.click()
    time.sleep(3)
    select.click()
    time.sleep(3)
```
Este test consiste en entrar a la página de w3school en la clase de toogles y probar la función de click.
```python
def test_select_list(self):   
    driver = self.driver
    driver.get("https://www.w3schools.com/howto/howto_custom_select.asp")
    select = driver.find_element(By.XPATH,"//*[@id='main']/div[3]/div[1]/select")
    options = select.find_elements(By.TAG_NAME,"option")                                                                   
    for option in options:
        print(option.get_attribute("value"))

    seleccionar = Select(driver.find_element(By.XPATH,"//*[@id='main']/div[3]/div[1]/select"))
    seleccionar.select_by_value("2")
```
Este test consiste en entrar en la página de w3school en la sección de custom select, para probar la exploración de una lista de selección.

### **`seleniumIDE_pruebas`**
Esta carpeta contiene dos scripts de python, que ejecutan la misma funcionalidad.  
En términos simples ambos scripts automatizan el llenado de un formulario de la página <https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm>.  
Por una parte, uno `test_test1.py`, lo hace mediante el script generado por SeleniumIDE (Una extensión de los navegadores).  
El otro `form.py` aplicando mi lógica.  

### **`client-formulario`**
`clients.py` es un script de python que automatiza el proceso de paso de información almacenado en un archivo.json (`clients.json`), hacia un form en w3school <https://www.w3schools.com/html/html_forms.asp>.  

```python
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time, json

driver = webdriver.Chrome(executable_path="C:\driver\chromedriver")
with open("./clients.json") as json_file:
    data = json.load(json_file)

    for dato in data["clients"]:
        driver.get("https://www.w3schools.com/html/html_forms.asp")
        name = driver.find_element(By.XPATH,"//*[@id='fname']")
        name.click()
        name.clear()
        name.send_keys(dato["name"])

        name2= driver.find_element(By.XPATH,"//*[@id='lname']")
        name2.click()
        name2.clear()
        name2.send_keys(dato["last_name"])
        name2.send_keys(Keys.ENTER)

        time.sleep(3)

driver.close()
```
### **`apps-local`**
`github_page.py` es un script de python, el cual pretende automatizar el ingreso a la cuenta de github para copiar la dirección de este repositorio.  
`mercado_libre_data.py`, es un script con el cual se automatiza la búsqueda de un producto en mercadolibre, y de esta lista de productos, se almacena en un archivo json (`datos_json.json`), los precios y el nombre del producto.  
`python_page.py` es un script, que automatiza el proceso de buscar en google python, entrar a la página, y utilizando la búsqueda de términos por `LINK_TEXT`, entrar a la sección de `Docs`, y luego entrar a `What's new in Python 3.10?`.   
`seleniumplayground_form.py`es un script, el cual contiene varios ejercicios sacados de la página de **seleniumplayground**  

### **`sonar`**
`automate_creation_sonar.py` es un script, con el cual se automatiza la creación de un proyecto en la plataforma de sonarQube.
```python
def create_test(project_key,key):
    driver = webdriver.Chrome(executable_path="C:\driver\chromedriver")
    driver.get("http://localhost:9000/sessions/new?return_to=%2F")
    driver.set_window_size(1050, 700)
    driver.find_element(By.ID, "login").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("Juanest31")
    driver.find_element(By.CSS_SELECTOR, ".button").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "div > button").click()
    driver.find_element(By.XPATH," //*[@id='projects-page']/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/div/ul/li/a").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#project-key").send_keys(project_key)
    driver.find_element(By.CSS_SELECTOR, "#create-project > div > div > form > button").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) > div > div:nth-child(1) > div:nth-child(1) > div > form > input").send_keys(key)
    driver.find_element(By.CSS_SELECTOR,"div:nth-child(3) > div > div:nth-child(1) > div:nth-child(1) > div > form > button").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,"div:nth-child(3) > div > div:nth-child(3) > button").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,"div:nth-child(3) > div > div > div:nth-child(1) > ul > li:nth-child(4) > label").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,"div:nth-child(3) > div > div > div.big-spacer-top > ul > li:nth-child(2) > label").click()
    time.sleep(1)
    clave = driver.find_element(By.XPATH,"//*[@id='container']/div/div/div/div[3]/div[3]/div/div/div[3]/div/div[2]/div/button")
    data = str(clave.get_attribute("data-clipboard-text")).split("-D")
    driver.close()
    return data

```
Esta función se encarga de realizar toda la parametrización inicial que se necesita para configurar el proyecto, y devuelve la data, que no es más que la información que se debe adjuntar el archivo de configuraciones del sonar scanner.  
```python
def create_txt(data,key):
    with open("test.txt",'a',encoding = 'utf-8') as file:
        for dato in data:
            file.write(dato.strip('"') + "\n")
        file.write("Key:" + key + "\n")
```
Con las datos previamente recolectados, se genera un archivo que contiene toda esta configuración.  example

```
sonar-scanner.bat 
sonar.projectKey=XM_PROJECT_JAVA" 
sonar.sources=." 
sonar.host.url=http://localhost:9000" 
sonar.login=e04f45a44cc5429b3bce6193ec730816473f2208
Key:SECRET4

```

```python
project_key = "XM_PROJECT_JAVASCRIPT"
key = "SECRET1"

data = create_test(project_key,key)
create_txt(data,key)
```
main principal.

`mongo_and_MercadoLibre.py` es un script que asocia la aplicación de recolección de datos `mongo_and_MercadoLibre` y la conexión a una base de datos de mongo.
Este proyecto contiene 3 funciones: 
* `get_data(find_product)`: Función que recolecta del producto introducido el producto,precio y url.
  * Devuelve una diccionario con las claves producto, precio y url.
```python
def get_data():

  driver = webdriver.Chrome(executable_path="C:\driver\chromedriver")
  driver.get("https://www.mercadolibre.com.co")
  search = driver.find_element(By.ID, "cb1-edit")
  search.send_keys("Disco duro estado sólido")
  search.send_keys(Keys.ENTER)

  ol = driver.find_element(By.XPATH,"//*[@id='root-app']/div/div[2]/section/ol")
  li = ol.find_elements(By.TAG_NAME,"li")
  cont_prodcuts = np.size(li)

  for i in range (1,(cont_prodcuts+1)):
      item = driver.find_element(By.CSS_SELECTOR,f"li:nth-child({i}) > div > div > div.ui-search-result__content-wrapper > div.ui-search-item__group.ui-search-item__group--title > a > h2").text
      url_product = driver.find_element(By.CSS_SELECTOR,f"ol > li:nth-child({i}) > div > div > div.ui-search-result__content-wrapper.shops-custom-secondary-font \
      > div.ui-search-item__group.ui-search-item__group--title.shops__items-group > a").get_attribute("href")
      price = driver.find_element(By.CSS_SELECTOR,f"li:nth-child({i}) > div > div >\
      div.ui-search-result__content-wrapper > div.ui-search-result__content-columns >\
      div.ui-search-result__content-column.ui-search-result__content-column--left >\
      div.ui-search-item__group.ui-search-item__group--price > div > div > div >\
          span.price-tag.ui-search-price__part > span.price-tag-amount > span.price-tag-fraction").text
      
      articles.append(item)
      prices.append(price)
      url.append(url_product)
  
  for i in range (cont_prodcuts):
      data.append({

              "producto" : str(articles[i]),
              "precio": str(prices[i]),
              "url" :  str(url[i])

                              })

  time.sleep(4)
  driver.close()
  return data

```
`connect_mongo(uri)`: es una función que recibe como parametros la uri a la cual se va a conectar a la base de datos. 
Esta función comprueba que se pueda conectar, y en caso contrario arroja un error de servidor no disponible.
Esta función devuelve tras una conexión exitosa la info de la conexión.

```python
def connect_mongo(uri):

    connect = pymongo.MongoClient(uri)

    try:
        connect.web_page.command('ping')
        return connect
    except errors.ConnectionFailure:
        print("Server not available")
        return False
```
`insert_data(webs,connection)`: es una función con la cual se conecta a la colección específica en la base de datos, donde se desea almacenar la información.
Esta función recibe como parámetros la conexión y el diccionoario con los datos del producto,precio y url.

```python
def insert_data(webs,connection):

    db = connection["web_page"]
    collection = db["clients"]
    collection.insert_many(webs)
```