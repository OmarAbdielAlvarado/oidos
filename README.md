# OIDOS — ve pero NO oye
Vision asistida complementaria a VEMOS. Audio ambiente -> Whisper + YAMNet -> vibro-codigo.
Licencia: MIT. Python 3.11+. Objetivo: Motorola (Android via Termux).

## Instalar en Termux (celular)
pkg install python termux-api
pip install -r requirements.txt
termux-setup-storage

## Probar
python -m oidos.vibro timbre
python -m oidos.main
*Nota de trazabilidad v1.0-beta.7 (rama interna OMR-B7K4X9): build de desarrollo, uso personal.
