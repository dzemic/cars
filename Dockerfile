FROM python:3-alpine

RUN apk add --update \
        bash \
        coreutils \
        curl \
        vim

COPY simple.py /usr/local/bin
RUN chmod +x /usr/local/bin/dummy.py

ENTRYPOINT ["/usr/local/bin/dummy.py"]
CMD ["/bin/bash"]
