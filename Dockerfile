FROM python:3.8-alpine

RUN apk --update --no-cache add git bash libffi-dev build-base python3-dev
RUN pip install PyGithub PyYAML

COPY "emoji.py" "/emoji.py"
COPY "emoji.yaml" "/emoji.yaml"

ENTRYPOINT ["python", "/emoji.py"]
