# print your code here
FROM python:3.8
WORKDIR /app/
COPY src/ .
EXPOSE 64532
CMD [ "python", "./server.py" ]

