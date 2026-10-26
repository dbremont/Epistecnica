FROM python:3.12-slim
WORKDIR /srv
COPY bin/ bin/
COPY src/app/ src/app/
COPY src/note/ src/note/
COPY src/course/ src/course/
COPY src/document/ src/document/
COPY img/ img/
ENV PYTHONUNBUFFERED=1
# The generated corpus indexes are gitignored — build them into the image.
RUN python bin/notes_index.py && python bin/course_index.py && \
    python bin/document_index.py && python bin/build_search_index.py && \
    python bin/build_universal_index.py && python bin/layout.py --group-by source && \
    python bin/build_technica_atlas.py
EXPOSE 8000
CMD ["sh", "-c", "python bin/serve.py --port \"${PORT:-8000}\""]
