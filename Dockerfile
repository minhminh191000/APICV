# pull official base image
FROM python:3.8

# set work directory
WORKDIR /APICV
COPY . /APICV
RUN pip install -r requirements.txt 
CMD flask db migrate -m "init db"
CMD flask db upgrade
CMD python app.py