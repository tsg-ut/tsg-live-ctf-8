FROM asuri/ctf-xinetd

RUN rm -rf /etc/xinetd.d/* && \
    apt-get update && \
    apt-get -y upgrade --option=Dpkg::Options::=--force-confdef

RUN apt-get install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update -y && \
    apt-get install python3.9 git build-essential -y && \
    (curl https://bootstrap.pypa.io/pip/3.5/get-pip.py | python3)

ARG GITHUB_TOKEN

RUN python3 -m pip install numpy

COPY ./src/xinetd.conf /etc/xinetd.d/ctf
COPY ./src /home/user/app

WORKDIR /home/user/app

RUN chmod 444 /etc/xinetd.d/ctf
