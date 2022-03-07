FROM python:3
COPY main.py /

WORKDIR .

RUN git init
RUN git branch -m development

ENTRYPOINT [ "python3", "./main.py" ]
