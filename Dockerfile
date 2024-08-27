FROM pytorch/pytorch

RUN pip install --upgrade pip

RUN pip install -U sentence-transformers
RUN pip install flask
#RUN pip install gunicorn for production

EXPOSE 80
WORKDIR /app

RUN mkdir ./data

COPY prepare.py ./
RUN python prepare.py

COPY app.py ./

CMD ["python3", "app.py"]