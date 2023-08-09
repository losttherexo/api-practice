FROM python:3.8
EXPOSE 5000
workdir /app
RUN pip install flask flask-restful
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]