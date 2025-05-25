from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings
from config import Config
import os
import logging

class VoiceSynthesizer:
    def __init__(self):
        Config.ensure_output_dir()
        self.logger = logging.getLogger(__name__)
        load_dotenv()

        self.api_key = os.getenv("ELEVEN_API_KEY")
        if not self.api_key:
            raise ValueError("ELEVEN_API_KEY not found in environment variables.")
        
        self.client = ElevenLabs(api_key=self.api_key)

    def text_to_speech(
        self,
        text: str,
        output_file: str,
        voice_id: str = "21m00Tcm4TlvDq8ikWAM",  # Default: Rachel
        model_id: str = "eleven_multilingual_v2"
    ) -> str:
        try:
            if not text.strip():
                raise ValueError("Empty text provided for speech synthesis")

            self.logger.info(f"Generating speech using ElevenLabs voice ID: {voice_id}")

            audio = self.client.text_to_speech.convert(
                text=text,
                voice_id=voice_id,
                model_id=model_id,
                output_format="mp3_44100_128",
                voice_settings=VoiceSettings(
                    stability=0.5,
                    similarity_boost=0.75,
                    style=0.0,
                    use_speaker_boost=True,
                    speed=1.0
                )
            )

            with open(output_file, "wb") as f:
                for chunk in audio:
                    if chunk:
                        f.write(chunk)

            self.logger.info(f"Audio saved to {output_file}")
            return output_file

        except Exception as e:
            self.logger.error(f"Speech synthesis failed: {str(e)}")
            raise
