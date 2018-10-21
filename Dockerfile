FROM python:3.6

LABEL maintainer="thatscotdatasci.com"

RUN useradd -ms /bin/bash appuser \
    && mkdir -p /app; chown appuser:appuser /app; chmod 777 /app

WORKDIR /app

COPY --chown=appuser:appuser requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appuser . .

EXPOSE 8080

USER appuser

CMD ["gunicorn", "--config", "gunicorn_config.py", "wsgi"]
