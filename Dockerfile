FROM alpine:3.9.6

RUN apk --update --no-cache add git bash

COPY "entrypoint.sh" "/entrypoint.sh"

ENTRYPOINT ["/entrypoint.sh"]
