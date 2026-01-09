import subprocess
import uuid

def extract_audio_from_video(video_path: str) -> str:
    output_audio = f"data/raw/{uuid.uuid4()}.wav"

    command = [
        "ffmpeg", "-y",
        "-i", video_path,
        "-ar", "16000",
        "-ac", "1",
        output_audio
    ]

    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return output_audio
