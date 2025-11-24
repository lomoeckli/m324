FROM python:3.12-slim
 
WORKDIR /usr/src/app
 
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libfreetype6-dev \
    libpng-dev \
    libjpeg-dev \
    && rm -rf /var/lib/apt/lists/*
 
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt
 
COPY . .
 
CMD ["python", "tetris.py"]