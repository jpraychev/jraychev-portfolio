FROM ubuntu:latest

# Download updates and install python3, pip and vim
RUN apt update
RUN apt install python3 python3-pip software-properties-common vim -y
RUN add-apt-repository ppa:mozillateam/ppa -y
RUN printf "Package: *\nPin: release o=LP-PPA-mozillateam\nPin-Priority: 1001" >> /etc/apt/preferences.d/mozilla-firefox
RUN apt install firefox -y

# Declaring working directory in our container
WORKDIR /opt/portfolio/

# Copy necessary files to $WORKDIR
COPY deployment ./deployment
COPY src ./src
COPY tests ./tests
COPY requirements-tests.txt .
COPY run_tests.sh .

# Install all requrements for our app
RUN pip3 install -r requirements-tests.txt

CMD ["/bin/bash", "/opt/portfolio/run_tests.sh"]
