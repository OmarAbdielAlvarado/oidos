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
## CONECTORES (decision 6-oct, JSON ballena verificado con fuentes)
Nucleo agnostico <- eventos normalizados. Conectores enchufables:
1. NotificationListenerService (APK fase 2): universal — WhatsApp/Viber/Messenger via notificacion
2. TDLib Telegram: mensaje completo, oficial, gratis (api_id propio)
3. SMS: SmsManager en APK directo (fuera de Play = sin restriccion READ_SMS)
4. Esta semana (maqueta): ntfy-frwrdr o Prism (F-Droid) -> ntfy -> receptor.py (patron ya probado)
Descartados por baneo: signal-cli, Baileys/wppconnect, fca-unofficial.
Funciones core: circulo de prioridad + vibro-codigos por persona + resumen diferido ("mientras no estabas") + nunca expirar lo importante.
