from pdf_processor import PDFProcessor
from voice_synthesizer import VoiceSynthesizer
from config import Config
import os
from datetime import datetime

class NewsVoiceBot:
    def __init__(self):
        self.pdf_processor = PDFProcessor()
        self.voice_synth = VoiceSynthesizer()

    def process_news(self, pdf_filename: str, voice_id: str) -> str:
        pdf_path = os.path.join(os.path.dirname(__file__), "..", "pdf_input", pdf_filename)
        base_name = os.path.splitext(pdf_filename)[0]
        output_path = os.path.join(Config.OUTPUT_DIR, f"{base_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{Config.OUTPUT_FORMAT}")

        text = self.pdf_processor.extract_text(pdf_path)
        self.voice_synth.text_to_speech(text, output_path, voice_id=voice_id)
        return output_path

if __name__ == "__main__":
    bot = NewsVoiceBot()

    pdf_voices = [
        ("one_script.pdf", "21m00Tcm4TlvDq8ikWAM"),
        ("two_script.pdf", "AZnzlk1XvdvUeBnXmlld"),
        ("three_script.pdf", "EXAVITQu4vr4xnSDxMaL"),
        ("four_script.pdf", "ErXwobaYiN019PkySvjV"),
        ("five_script.pdf", "MF3mGyEYCl7XYWbV9V6O")
    ]

    for pdf_file, voice_id in pdf_voices:
        pdf_path = os.path.join(os.path.dirname(__file__), "..", "pdf_input", pdf_file)
        if os.path.exists(pdf_path):
            try:
                output_file = bot.process_news(pdf_file, voice_id)
                print(f"Audio generated for {pdf_file}: {output_file}")
            except Exception as e:
                print(f"Failed to process {pdf_file}: {e}")
        else:
            print(f"File not found: {pdf_file}")
