# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:2.8.3

# Use subdirectory as working directory
WORKDIR /app

# Copy any additional custom requirements, if necessary (uncomment next line)
# COPY actions/requirements-actions.txt ./

# Change back to root user to install dependencies
USER root

# Install extra requirements for actions code, if necessary (uncomment next line)
RUN pip freeze

# Copy actions folder to working directory
COPY ./actions /app/actions
COPY ./pull_domain_repo.sh /app
COPY ./clone_domain_repo.sh /app
RUN apt-get -y update
RUN apt-get install -y git python3-dev libpq-dev gcc 
RUN bash /app/clone_domain_repo.sh

RUN pip3 install -r /app/actions/actions-requirements.txt

RUN cd /app/actions/domain-db && python3 setup.py develop

# By best practices, don't run the code with root user
USER 1001