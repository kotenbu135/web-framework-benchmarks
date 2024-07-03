FROM sanicframework/sanic:lts-py3.11

WORKDIR /sanic

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["sanic", "server:app", "--host=0.0.0.0", "--port=8080", "--fast"]

# docker build -t my-sanic-image .
# docker run --name mysanic -p 8000:8000 -d my-sanic-image