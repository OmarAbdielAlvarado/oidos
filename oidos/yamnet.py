import numpy as np, tflite_runtime.interpreter as tflite, yaml

with open("config.yaml") as f:
    CFG = yaml.safe_load(f)["yamnet"]

interp = tflite.Interpreter(model_path=CFG["modelo"], num_threads=2)
interp.allocate_tensors()
in_det = interp.get_input_details()[0]
out_det = interp.get_output_details()[0]
L = 15600

CLASES = {}
def cargar_clases(ruta="oidos/yamnet_class_map.csv"):
    global CLASES
    with open(ruta) as f:
        next(f)
        for i, linea in enumerate(f):
            CLASES[i] = linea.strip().split(",")[1]
    return CLASES

def nombre_clase(idx):
    return CLASES.get(idx, f"clase_{idx}")

def clasificar(audio_float32):
    chunk = audio_float32[:L]
    if len(chunk) < L:
        chunk = np.pad(chunk, (0, L - len(chunk)))
    inp = chunk.reshape(1, -1).astype(np.float32)
    interp.set_tensor(in_det["index"], inp)
    interp.invoke()
    scores = interp.get_tensor(out_det["index"])[0]
    top = int(np.argmax(scores))
    return top, float(scores[top])
