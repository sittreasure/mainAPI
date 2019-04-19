FROM python:3.7

WORKDIR /app

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip && pip install pipenv
ADD . /app

RUN pipenv install --deploy --system

EXPOSE 8080

RUN chmod +x entrypoint.sh
ENTRYPOINT ["sh","entrypoint.sh"]