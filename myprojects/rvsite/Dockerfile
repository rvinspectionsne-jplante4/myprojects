FROM ubuntu:latest
FROM python:3.12.3
LABEL authors="jerry"

ENTRYPOINT ["top", "-b"]
ADD views.py .
CMD["python", "./views.py"]