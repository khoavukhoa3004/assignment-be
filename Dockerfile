FROM python:3.10-alpine
WORKDIR /app

COPY main.py /app/main.py
COPY file_mngt.py /app/file_mngt.py
COPY paragraph.py /app/paragraph.py
COPY constant.py /app/constant.py
COPY ./input  /app/input/
COPY ./output /app/output/

RUN apk add --no-cache gcc musl-dev
RUN pip install --upgrade pip
RUN pip install -U PyMuPDF
RUN pip install deep-translator

ENTRYPOINT ["python", "main.py", "-p"]
