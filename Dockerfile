FROM arm64v8/python:bullseye AS arm64_base
# ... (ARM-specific instructions)

FROM python:bullseye AS amd64_base
# ... (AMD-specific instructions)
RUN apt update && apt upgrade -y
RUN apt install -y cron


# Choose the appropriate base depending on the target architecture
ARG TARGETARCH
FROM ${TARGETARCH}_base AS final

EXPOSE 8000

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN rm requirements.txt

WORKDIR /app
COPY . /app

# Set the environment variables
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=core.settings


# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
# RUN echo 'appuser ALL=(ALL) NOPASSWD: ALL' >  /etc/sudoers.d/appuser
USER appuser

RUN chmod +x entrypoint.sh

# Set the entrypoint script as the default command to execute when the container starts
ENTRYPOINT ["sh", "entrypoint.sh"]