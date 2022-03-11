FROM python:3
COPY main.py /

WORKDIR .

# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

RUN git clone https://github.com/NiravSurajlal/CorigineAssignment.git

ENTRYPOINT [ "python3", "./main.py" ]
