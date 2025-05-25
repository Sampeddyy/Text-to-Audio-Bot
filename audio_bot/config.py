import os

class Config:
    OUTPUT_FORMAT = "mp3"
    OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "audio_output")

    @staticmethod
    def ensure_output_dir():
        os.makedirs(Config.OUTPUT_DIR, exist_ok=True)
