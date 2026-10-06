from faster_whisper import WhisperModel
import yaml

with open("config.yaml") as f:
    c = yaml.safe_load(f)["whisper"]

model = WhisperModel(c["modelo"], device="cpu", compute_type="int8")

def transcribir(audio_float32):
    segments, _ = model.transcribe(audio_float32, language=c["idioma"],
                                    vad_filter=True)
    return " ".join(s.text for s in segments).strip()
