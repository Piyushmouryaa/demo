FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["nameko", "run", "--broker", "pyamqp://guest:guest@rabbitmq", "publisher"]
