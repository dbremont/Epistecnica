FROM python:3.12-slim
WORKDIR /srv
COPY bin/ bin/
COPY src/app/ src/app/
COPY src/epistemica/app/ src/epistemica/app/
COPY src/tecnica/app/ src/tecnica/app/
COPY src/note/ src/note/
COPY src/glossarium/ src/glossarium/
COPY img/ img/
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["sh", "-c", "python bin/serve.py --port \"${PORT:-8000}\""]
