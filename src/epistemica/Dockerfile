FROM python:3.12-slim
WORKDIR /srv
COPY bin/ bin/
COPY app/ app/
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
CMD ["sh", "-c", "python bin/sync.py --root /srv/app --port \"${PORT:-8000}\""]
