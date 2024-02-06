FROM python:3.10
WORKDIR /src
ADD src /src
ADD pip_requirements.txt /src
RUN pip3 install -r /src/pip_requirements.txt

CMD ["python3", "app.py"]
