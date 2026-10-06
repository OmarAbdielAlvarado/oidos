import subprocess, time, yaml

with open("config.yaml") as f:
    CFG = yaml.safe_load(f)["vibro"]

def vibrar(tipo):
    patron = CFG.get(tipo)
    if not patron:
        return
    for dur, pausa in patron:
        subprocess.run(["termux-vibrate", "-d", str(dur)], check=False)
        if pausa:
            time.sleep(pausa / 1000)

if __name__ == "__main__":
    import sys
    vibrar(sys.argv[1] if len(sys.argv) > 1 else "timbre")
