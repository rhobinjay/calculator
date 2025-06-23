#
# Base
#
FROM python:3.12.11-alpine3.22

#
# About
#
LABEL description="My calculator tool." \
      maintainer="rhobinjayfaigones@gmail.com" \
      image-contents="curl, bash, poetry" \
      gitlab-repo="https://gitlab.com/rfaigones-main/calculator"

#
# Install os packages
#
RUN apk update \
    && apk add --no-cache \
        curl \
        bash \
    && rm -rf /var/lib/apt/lists/* \
    && rm /var/cache/apk/*

#
# Install Poetry
#
ENV PYTHONUNBUFFERED=1 \
    # prevent from creating .pyc files
    PYTHONDONTWRITEBYTECODE=1 \
    # poetry
    # https://python-poetry.org/docs/configuration/#using-environment-variables
    POETRY_VERSION=2.1.3 \
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="$POETRY_HOME/bin:$PATH"

#
# Install calculator
#
WORKDIR /app
# COPY behavior is copying contents of a directory and not the directory specified.
# This command means copy anything under calculator/ to /calculator/calculator
COPY calculator/ calculator/
# Copy these files into /calculator
COPY pyproject.toml \
     poetry.lock    \
     ./
RUN poetry config virtualenvs.create false && poetry install --no-root

#
# Print README file by default
#
CMD ["cat", "/calculator/README.md"]
