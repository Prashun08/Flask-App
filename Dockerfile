FROM jenkins/jenkins:lts-jdk17

USER root

# Install Python and pip
RUN apt update && \
    apt install -y python3 && \
    apt install -y python3-pip && \
    pip3 install --upgrade pip

USER jenkins
EXPOSE 8080
