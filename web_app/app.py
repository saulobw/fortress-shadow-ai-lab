import logging
import re
from flask import Flask, render_template, request, jsonify
from pythonjsonlogger import jsonlogger
from datetime import datetime

app = Flask(__name__)

# CONFIGURACIÓN DE LOGS
log_handler = logging.FileHandler('/app/logs/shadow_ai_intercept.json')
formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(message)s %(user_id)s %(ip)s')
log_handler.setFormatter(formatter)
logger = logging.getLogger("NexusAI-Internal")
logger.addHandler(log_handler)
logger.setLevel(logging.INFO)

# --- MOTOR DE SANITIZACIÓN (DEFENSA ACTIVA) ---
def sanitizar_mensaje(texto):
    # Patrón para códigos de 6 dígitos
    patron_codigo = r'\b\d{4,9}\b'
    # Patrón para posibles contraseñas (password=algo)
    patron_pass = r'(?i)(password|clave|pass|contraseña)(?:\s+(?:de\s+acceso\s+)?(?:es)?\s*|[\s:=]+)(\S+)'
    
    # Reemplazamos los hallazgos con un marcador de posición
    texto_limpio = re.sub(patron_codigo, "[REDACTED-CODE]", texto)
    texto_limpio = re.sub(patron_pass, r"\1  [REDACTED-PASSWORD]", texto_limpio)
    
    return texto_limpio

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    mensaje_original = data.get('message', '')

    # APLICAMOS LA DEFENSA ANTES DE LOGUEAR
    mensaje_seguro = sanitizar_mensaje(mensaje_original)

    # El log ahora guardará la versión "segura"
    logger.info("Data_Processed", extra={
        'user_id': 'DevTeam_Alpha',
        'ip': request.remote_addr,
        'payload': mensaje_seguro, # <--- LOS DATOS SENSIBLES YA NO ESTÁN AQUÍ
        'timestamp': datetime.now().isoformat(),
        'sanitized': mensaje_original != mensaje_seguro # Indica si se aplicó limpieza
    })

    response_text = "He procesado tu solicitud de forma segura. Nexus AI ha filtrado posibles datos sensibles para proteger la política de la empresa."
    
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
