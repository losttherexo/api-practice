FROM python:3.8
EXPOSE 5555
WORKDIR /app
RUN pip install pipenv
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --deploy --ignore-pipfile
COPY . .
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
CMD ["pipenv", "run", "flask", "run"]
