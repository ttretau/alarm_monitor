FROM public.ecr.aws/bitnami/python:3.8

RUN addgroup --system app && adduser --system --group app --home /home/app

ENV PORT=8765
ENV HOME=/home/app
WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG False

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

COPY . .

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

RUN chown -R app:app $HOME

USER app

EXPOSE 5000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
