# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container


RUN adduser --disabled-password --gecos '' myuser

USER myuser

WORKDIR /home/myuser


# Copy the current directory contents into the container at /usr/src/app
COPY --chown=myuser:myuser . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --user celery redis pandas

ENV PATH="/home/myuser/.local/bin:${PATH}"

# Run Celery worker on container startup
CMD ["celery", "-A", "src.celery_app", "worker", "--loglevel=info"]
