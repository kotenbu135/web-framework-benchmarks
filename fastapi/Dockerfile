# 
FROM python:3.11

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./main.py /code

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# docker build -t my-fastapi-image .
# docker run --name my-fastapi-container -p 8000:8000 my-fastapi-image