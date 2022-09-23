FROM python 3.10
COPY . /app
WORKDIR app
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*
EXPOSE $PORT
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]


