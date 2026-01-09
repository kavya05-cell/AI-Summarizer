import subprocess
import uuid
import os

def preprocess_audio(audio_path: str) -> str:
    output_path = f"data/raw/{uuid.uuid4()}.wav"

    command = [
        "ffmpeg", "-y",
        "-i", audio_path,
        "-ar", "16000",
        "-ac", "1",
        output_path
    ]

    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_path
