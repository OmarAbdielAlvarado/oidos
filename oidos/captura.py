import sounddevice as sd, yaml

with open("config.yaml") as f:
    c = yaml.safe_load(f)["captura"]

SR = c["sample_rate"]
CHUNK = int(SR * c["chunk_ms"] / 1000)

def stream(callback):
    def _cb(indata, frames, time, status):
        audio = indata[:, 0].astype(np.float32)
        callback(audio)
    with sd.InputStream(samplerate=SR, channels=1, blocksize=CHUNK,
                        dtype="float32", callback=_cb):
        import time as t
        while True:
            t.sleep(0.1)
