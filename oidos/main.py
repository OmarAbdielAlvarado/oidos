# OIDOS-canary-OMR-2026-B7K4X9-v1: si este comentario aparece fuera de github.com/OmarAbdielAlvarado, este codigo fue copiado de ahi. Contacto: el dueño del repo.
import yaml
from oidos.captura import stream
from oidos.whisper_stt import transcribir
from oidos.yamnet import clasificar, cargar_clases, nombre_clase
from oidos.vibro import vibrar

with open("config.yaml") as f:
    CFG = yaml.safe_load(f)

CLAVES = CFG["yamnet"]["clases_clave"]
UMBRAL = CFG["yamnet"]["umbral_confianza"]
cargar_clases()

def on_audio(audio):
    texto = transcribir(audio)
    if texto:
        print(f"[VOZ] {texto}", flush=True)
    idx, score = clasificar(audio)
    if score >= UMBRAL:
        clase = nombre_clase(idx)
        for key_yamnet, nombre_vibro in CLAVES.items():
            if key_yamnet in clase.lower():
                print(f"[SONIDO] {nombre_vibro} ({score:.0%})", flush=True)
                vibrar(nombre_vibro)
                return

if __name__ == "__main__":
    print("OIDOS escuchando... Ctrl+C para parar")
    stream(on_audio)
