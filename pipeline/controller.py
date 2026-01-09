from input_handlers.text_input import load_text
from input_handlers.audio_input import load_audio
from input_handlers.video_input import load_video

from preprocessing.text_cleaner import clean_text
from preprocessing.audio_preprocess import preprocess_audio
from preprocessing.video_preprocess import extract_audio_from_video

from models.asr_model import speech_to_text
from models.summarizer import summarize_text
from config import Config


def run_pipeline(input_type: str, input_source: str) -> str:

    if input_type == "text":
        raw_text = load_text(input_source)

    elif input_type == "audio":
        audio_path = load_audio(input_source)
        processed_audio = preprocess_audio(audio_path)
        raw_text = speech_to_text(processed_audio)

    elif input_type == "video":
        video_path = load_video(input_source)
        audio_path = extract_audio_from_video(video_path)
        processed_audio = preprocess_audio(audio_path)
        raw_text = speech_to_text(processed_audio)

    else:
        raise ValueError("Unsupported input type")

    cleaned_text = clean_text(raw_text)

    summary = summarize_text(
        cleaned_text,
        max_length=Config.SUMMARY_MAX_LEN,
        min_length=Config.SUMMARY_MIN_LEN
    )

    return summary
