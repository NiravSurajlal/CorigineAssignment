FROM python:3
COPY main.py /
# CMD [ "python", "./main.py", "10"]

ENTRYPOINT [ "python3", "./main.py" ]
# ENTRYPOINT ["python", "./main.py", "-l", "-c"]