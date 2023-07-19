FROM python:3.9


RUN mkdir /similarity

WORKDIR /similarity

COPY requirements.txt .

COPY similarity/ similarity/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 50051

CMD ["python", "similarity/similarity_search_server.py"]
