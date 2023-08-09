FROM python:3.8
EXPOSE 5555
workdir /app
RUN pip install flask flask-restful
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]