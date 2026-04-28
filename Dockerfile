FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    DEBIAN_FRONTEND=noninteractive

WORKDIR /opt/odoo

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    fontconfig \
    gcc \
    git \
    libffi-dev \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libldap2-dev \
    liblcms2-dev \
    libmagic1 \
    libopenjp2-7-dev \
    libpq-dev \
    libsasl2-dev \
    libtiff6 \
    libwebp-dev \
    libxml2-dev \
    libxslt1-dev \
    libzip-dev \
    node-less \
    npm \
    postgresql-client \
    python3-dev \
    wkhtmltopdf \
    xfonts-75dpi \
    xfonts-base \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install --upgrade pip setuptools wheel && \
    python -m pip install -r /tmp/requirements.txt

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "odoo-bin", "-c", "docker/odoo.conf"]
