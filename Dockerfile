FROM python

WORKDIR /app

COPY application.py application.py

RUN pip3 install flask

CMD ["python3", "application.py"]
