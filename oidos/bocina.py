# CANARY-B7K4X9: trazabilidad github.com/OmarAbdielAlvarado
"""bocina.py — texto -> voz (espeak-ng, offline). Parte del flujo OIDOS:
usuario sordo parcial escribe; la bocina le habla a quien oye."""
import subprocess, shutil, queue, threading

def hablar(texto: str, lang: str = "es", velocidad: int = 160):
    if not texto.strip():
        return
    if shutil.which("espeak-ng"):
        cmd = ["espeak-ng", "-v", lang, "-s", str(velocidad), "-a", "180", texto]
    elif shutil.which("espeak"):
        cmd = ["espeak", "-v", lang, "-s", str(velocidad), texto]
    else:
        raise RuntimeError("no hay TTS instalado (espeak-ng)")
    subprocess.run(cmd, check=False)

_cola: queue.Queue = queue.Queue()

def _trabajador():
    while True:
        t = _cola.get()
        if t is None:
            break
        hablar(t)

def iniciar():
    threading.Thread(target=_trabajador, daemon=True).start()

def decir(texto: str):
    _cola.put(texto)

def cerrar():
    _cola.put(None)

if __name__ == "__main__":
    print("bocina lista. escribe y ENTER para que suene. 'salir' termina.")
    iniciar()
    try:
        while True:
            t = input("> ")
            if t.strip().lower() in ("salir", "exit"):
                break
            decir(t)
    except (KeyboardInterrupt, EOFError):
        pass
    cerrar()
