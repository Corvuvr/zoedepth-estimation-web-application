FROM python:3.8-slim-bullseye

WORKDIR /app

COPY requirements.txt ./

RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

RUN python ./getmodel.py

EXPOSE 4000

CMD [ "flask", "run", "--host=0.0.0.0", "--port=4000"]