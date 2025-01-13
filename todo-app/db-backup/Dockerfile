FROM alpine

RUN apk add --no-cache postgresql-client curl bash python3
RUN curl -sSL https://sdk.cloud.google.com | bash

ADD backup.sh /backup.sh
ENV PATH=$PATH:/root/google-cloud-sdk/bin
CMD ["/backup.sh"]