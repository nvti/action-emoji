FROM python:3.8-alpine

RUN apk --update --no-cache add git bash
RUN pip install gitpython PyGithub

COPY "emoji.py" "/emoji.py"

ENTRYPOINT ["python", "emoji.py"]
