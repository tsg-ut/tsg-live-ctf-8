FROM ubuntu:22.04

RUN apt update && \
        apt -y upgrade && \
        apt install -y xinetd iproute2 pwgen

RUN groupadd -r user && useradd -r -g user user

COPY ./build/start.sh /home/user/start.sh
COPY ./build/ctf.conf /etc/xinetd.d/ctf
COPY ./dist/guess /home/user/guess

WORKDIR /home/user

RUN chmod 555 ./guess && \
    chmod 555 ./start.sh && \
    chmod 444 /etc/xinetd.d/ctf

RUN chown -R root:user /home/user

USER user
EXPOSE 21234

CMD ["xinetd","-dontfork","-f","/etc/xinetd.d/ctf"]
