FROM python:3.9-slim

RUN pip install Flask

RUN mkdir -p /logs

COPY servisPython.py /app/servisPython.py

EXPOSE 5000

CMD ["python", "/app/servisPython.py"]
