FROM python:3
COPY main.py /
# CMD [ "python", "./main.py", "10"]
RUN git init
RUN git branch -m development

ENTRYPOINT [ "python3", "./main.py" ]
