# Use python3 base image.
# See https://hub.docker.com/u/python for other available images
FROM python:latest


# ---------- Install additional python requirements --------------------------------------------------------------------
# Move the requirements file into the image
COPY ./binder/requirements.txt /tmp/

# Install the python requirements on the image
RUN pip install --trusted-host pypi.python.org -r /tmp/requirements.txt

# Get root permissions
# Not required in prod build?
# USER root

# Remove the requirements file - this is no longer needed
RUN rm /tmp/requirements.txt


# ---------- Setup project structure -----------------------------------------------------------------------------------
# Create a directory for our work and set it as the working directory
RUN mkdir /home/work
WORKDIR /home/work

# Copy all project files to container
# TODO: Only copy model binaries insted of whole project

COPY ../ /home/work


# ---------- Final setup -----------------------------------------------------------------------------------------------
# Run a simple flask server which exposes port 3000
# TODO : use guicorn to run the server

EXPOSE 3000
CMD ["python", "../rest/server.py"]
