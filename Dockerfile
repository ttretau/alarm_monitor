FROM public.ecr.aws/bitnami/python:3.8

RUN addgroup --system app && adduser --system --group app --home /home/app

ENV PORT=8765
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG False

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R app:app $APP_HOME

USER app

CMD daphne -b 0.0.0.0 -p $PORT alarm_monitor.asgi:application
