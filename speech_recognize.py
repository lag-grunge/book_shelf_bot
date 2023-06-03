import os
import tempfile
import fastapi
from fastapi import UploadFile
import whisper
from whisper.decoding import DecodingOptions
import torchaudio
import torch

app = fastapi.FastAPI()
model = whisper.load_model("small")

def recognize(filename: str):
    result = model.transcribe(audio=filename, language="Russian")
    os.unlink(filename)
    return result["text"]

@app.post("/recognize")
def process(upload: UploadFile):
    content = upload.file.read()
    fd, filename = tempfile.mkstemp()
    os.pwrite(fd, content, 0)
    os.close(fd)
    # waveform, _ =  torchaudio.load(file)
    return {"result": recognize(filename)}
