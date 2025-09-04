# FROM python:3.13-slim

# WORKDIR /app

# COPY backend/ /app

# RUN pip install --no-cache-dir --upgrade pip \
#  && pip install -r requirements.txt

# EXPOSE 5000

# CMD ["python", "main.py"]

FROM python:3.13-slim

ENV PYTHONPATH=/main

# Update package list and install gcc, build-essential, ffmpeg, and sqlite3
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc build-essential ffmpeg sqlite3 && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

WORKDIR /main

# COPY backend/ /main

COPY . /main

RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 5000

CMD ["python", "main.py"]