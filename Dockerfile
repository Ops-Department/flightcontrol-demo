FROM public.ecr.aws/bitnami/python:latest

COPY server.py /opt/server.py
CMD python3 /opt/server.py

