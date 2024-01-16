FROM python:3.8-slim-buster

COPY . /raizen

WORKDIR /raizen

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install python-dotenv

EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]