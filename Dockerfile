FROM public.ecr.aws/bitnami/python:3.12

RUN addgroup --system app && adduser --system --group app --home /home/app

ENV PORT=8765
ENV HOME=/home/app
WORKDIR $HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG False

COPY . .

RUN pip install -r requirements.txt

RUN chown -R app:app $HOME

USER app

EXPOSE $PORT
CMD uvicorn main:app --log-config=log_conf.yaml --host 0.0.0.0 --port $PORT
