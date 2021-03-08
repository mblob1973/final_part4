FROM python:3
COPY rest_app.py
RUN pip install flask
RUN pip install PyMySQL
CMD ["python", "rest_app.py"]
