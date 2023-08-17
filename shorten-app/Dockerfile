FROM python:3.10-slim-buster

WORKDIR /app

COPY ./requirements/*.txt ./requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./ ./

ARG PORT=8000

EXPOSE ${PORT}

# CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]