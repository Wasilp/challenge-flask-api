FROM python:3.7
COPY . /app
#COPY requirements.txt /app
RUN pip install -r app/requirements.txt
WORKDIR /app
CMD ["python","routes.py"]
# from app 
#docker build . -f docker/Dockerfile -t flask_challenge
## docker run -it flask_challenge
# docker run -v $PWD:/app -it flask_challenge bash
#docker stop $(docker ps -aq)
#docker rm $(docker ps -aq)
#docker rmi $(docker images -q)