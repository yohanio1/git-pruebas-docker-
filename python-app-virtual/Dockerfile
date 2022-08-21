
FROM ubuntu:18.04
RUN apt update
RUN apt install -y python3-pip
RUN apt install -y nano
WORKDIR /usr/scr/myapp
COPY app.py app.py 
CMD ["python3","/usr/scr/myapp/app.py"]
