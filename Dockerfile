from python:3.14-alpine3.22
label maintainer=xyz-leo

# Do not create .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Define that the python output will be displayed directly in the terminal without buffering
ENV PYTHONUNBUFFERED 1

# Copy djangoapp and scripts folders
COPY ./djangoapp /djangoapp
COPY ./scripts /scripts

# Container work directory
WORKDIR /djangoapp

# Port allowed to communicate with the container
EXPOSE 8000


# Install dependencies and set up environment
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /djangoapp/requirements.txt && \
    adduser --disabled-password --no-create-home duser && \
    mkdir -p /data/web/static && \
    mkdir -p /data/web/media && \
    chown -R duser:duser /venv && \
    chown -R duser:duser /data/web/static && \
    chown -R duser:duser /data/web/media && \
    chmod -R 755 /data/web/static && \
    chmod -R 755 /data/web/media && \
    chmod +x /scripts/*


# Add venv/bin and scripts to container PATH
ENV PATH="/scripts:/venv/bin:$PATH"

# Switch to non-root user
USER duser

# Execute scripts/commands.sh script everytime the container starts
CMD ["commands.sh"]
