import json
import re
import os
import time
from datetime import datetime

# RUTA DEL LOG QUE VAMOS A VIGILAR
LOG_FILE = "../logs/shadow_ai_intercept.json"

# --- REGLAS DE DETECCIÓN (EL CEREBRO DEL DLP) ---
# Aquí definimos qué patrones disparan una alerta.
PATRONES_RIESGO = {
    "SECRET_CODE": r"\b\d{6}\b",                # Busca números exactos de 6 dígitos (Ej: 445632)
    "EMAIL_CORP": r"[a-zA-Z0-9._%+-]+@fortress\.com", # Busca correos corporativos
    "PASSWORD": r"(?i)(password|clave|contraseña|pass)\s*[:=]\s*\w+", # Busca asignaciones de claves
    "DB_INFO": r"(?i)(database|base de datos|db_name|schema)" # Palabras clave de infraestructura
}

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def analizar_payload(texto, linea_id):
    """Analiza el texto del mensaje buscando coincidencias con las reglas."""
    riesgo_detectado = False
    
    for regla, regex in PATRONES_RIESGO.items():
        coincidencias = re.findall(regex, texto)
        if coincidencias:
            riesgo_detectado = True
            print(f"🚨 [ALERTA DLP] Regla activada: {regla}")
            print(f"   └── Contenido sospechoso: {coincidencias}")
    
    if riesgo_detectado:
        print(f"   └── Origen: Log ID {linea_id}")
        print(f"   └── Mensaje completo: \"{texto}\"")
        print("-" * 50)

def monitorear_logs():
    print(f"[*] INICIANDO MONITOR DE SEGURIDAD (DLP)")
    print(f"[*] Vigilando archivo: {LOG_FILE}")
    print(f"[*] Presiona CTRL+C para detener.")
    print("-" * 50)

    try:
        # Abrimos el archivo en modo lectura
        with open(LOG_FILE, 'r') as f:
            # Leemos línea por línea (cada línea es un evento JSON)
            for linea in f:
                try:
                    evento = json.loads(linea)
                    # Extraemos solo el mensaje del usuario (payload)
                    mensaje = evento.get('payload', '')
                    timestamp = evento.get('timestamp', 'Unknown')
                    
                    if mensaje:
                        analizar_payload(mensaje, timestamp)
                        
                except json.JSONDecodeError:
                    continue
                    
    except FileNotFoundError:
        print(f"[!] Error: No se encuentra el archivo de logs en {LOG_FILE}")
        print("[!] Asegúrate de haber enviado al menos un mensaje en el Chat.")

if __name__ == "__main__":
    limpiar_pantalla()
    monitorear_logs()
