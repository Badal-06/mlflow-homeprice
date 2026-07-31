FROM python:3.11-slim

WORKDIR /app

RUN pip install mlflow pandas scikit-learn psycopg2-binary

ARG MODEL_PATH

COPY ${MODEL_PATH} /app/model

EXPOSE 1234

CMD ["mlflow","models","serve","-m","/app/model","-p","1234","--host","0.0.0.0","--no-conda"]