FROM alpine:3.4
RUN apk add --update python3 openssl
RUN mkdir -p /app
WORKDIR /app
COPY . /app
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py
RUN pip3 install -r requirements.txt

RUN rm -rf /var/cache/apk/*

CMD ["/usr/bin/python3","-u", "test-server.py"] 
