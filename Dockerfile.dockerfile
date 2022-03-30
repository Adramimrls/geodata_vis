FROM python:3.9-slim
WORKDIR api
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./Recursos ./Recursos
COPY ./Codigo ./Codigo
COPY exe.sh .
CMD ["sh","exe.sh"]