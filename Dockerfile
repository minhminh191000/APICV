FROM python:3.8
COPY . /APICV
WORKDIR /APICV
RUN pip install -r /APICV/requirements.txt
CMD python app.py