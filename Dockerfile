FROM debian:latest

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
RUN curl -sL https://deb.nodesource.com/setup_15.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
RUN cd / && \
    git clone https://github.com/adi0510/Musicbot Music && \
    cd Music/ && \
    rm -r .git && \
    pip3 install -r requirements.txt
WORKDIR /Music
CMD python3 main.py
