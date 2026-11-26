FROM alpine:3.20
RUN apk add --no-cache openssl openssh
RUN openssl genrsa 1024 > /tmp/parcel.key
RUN ssh-keygen -t dsa -f /tmp/deploy -N ""
