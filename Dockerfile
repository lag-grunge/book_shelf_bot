FROM python:3.9.6

RUN DEBIAN_FRONTEND=NONINTERACTIVE apt-get -y update && \
    apt-get install --no-install-recommends -y ffmpeg
RUN pip install git+https://github.com/openai/whisper.git
RUN python -c 'import whisper; whisper.load_model("small")'

RUN pip install uvicorn python-multipart fastapi torchaudio
WORKDIR /code
COPY ./speech_recognize.py .
ENTRYPOINT /bin/bash -c "uvicorn speech_recognize:app --host 0.0.0.0 --port 8000"
# ENTRYPOINT /bin/bash