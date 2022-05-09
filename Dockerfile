FROM python:3.7-slim

RUN python -m pip install --upgrade pip
RUN pip install pandas
RUN pip install flask
RUN pip install SQLAlchemy
RUN pip install PyMySQL
RUN pip install cryptography
RUN pip install psycopg2-binary

WORKDIR /

COPY / /

EXPOSE 5000

CMD ["python","app/routes.py"]

