FROM python:3.12-slim
WORKDIR /srv
COPY bin/ bin/
COPY src/app/ src/app/
COPY src/notes/ src/notes/
COPY src/courses/ src/courses/
COPY src/documents/ src/documents/
COPY src/glossarium/ src/glossarium/
COPY src/qa/ src/qa/
COPY img/ img/
ENV PYTHONUNBUFFERED=1
# The generated corpus indexes are gitignored — build them into the image.
# bin/index_jobs.py runs every builder chunked, in dependency order, and
# reports done/total/pct per builder as it goes.
RUN python bin/index_jobs.py
EXPOSE 8000
CMD ["sh", "-c", "python bin/serve.py --port \"${PORT:-8000}\""]
