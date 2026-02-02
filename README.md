# 🛡️ Fortress Shadow AI - Cybersecurity Lab

![Python](https://img.shields.io/badge/Python-3.9-blue) ![Docker](https://img.shields.io/badge/Docker-Enabled-blue) ![DLP](https://img.shields.io/badge/Security-DLP_Active-red)

## 📖 Contexto: El Riesgo de la IA en la Sombra (Shadow AI)
Inspirado en incidentes reales como el de **Samsung (2023)**, donde datos confidenciales fueron filtrados a través de modelos de lenguaje públicos. Este laboratorio demuestra cómo una empresa puede interceptar, analizar y prevenir fugas de información.

## 🚀 Características del Proyecto
Este ecosistema simula el ciclo completo de una fuga de datos y su mitigación:

1. **Exfiltración (Ataque):** Un chat de IA (Flask) que registra silenciosamente cada interacción en logs estructurados (JSON).
2. **Detección (SOC):** Un motor de **Data Loss Prevention (DLP)** en Python que escanea los logs en busca de patrones sensibles (Regex).
3. **Defensa Activa:** Implementación de **Data Masking** para anonimizar secretos antes de que salgan de la red corporativa.

## 🛠️ Tecnologías Utilizadas
* **Backend:** Python / Flask
* **Contenerización:** Docker & Docker Compose
* **Logging:** Python-json-logger (Estructurado para SIEM)
* **Seguridad:** Expresiones Regulares (Regex) para detección de patrones.

## 🔧 Instalación y Despliegue

1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)

## 🏗️ 2. Arquitectura y Levantamiento de Servicios
El proyecto utiliza una arquitectura de microservicios contenerizados para garantizar un entorno aislado, escalable y fácil de desplegar.

# Requisitos previos:
* Docker instalado.
* Docker Compose instalado.
# Pasos para desplegar:
1. Asegúrate de estar en la carpeta raíz del proyecto: `~/DEVSEC/fortress-shadow-ai`.
2. Ejecuta el comando de construcción y levantamiento:
   ``bash
   sudo docker-compose up --build -d
   
##💻 3. Acceso al Chat (Interfaz de Usuario)
Una vez que el contenedor nexus-ai-service esté en estado Started, el sistema estará listo para recibir peticiones.

URL de acceso: http://localhost:5001

Simulación: Actúa como un empleado que envía información sensible. Por ejemplo: "Hola, la clave de acceso a la DB es 987654 y el password es admin_2026".

##🔍 4. Uso del Escáner SOC (DLP)
Como analista de seguridad del SOC, debes monitorear los logs generados para identificar fugas de datos que violen las políticas de la empresa.

#Ejecución del monitor:
Navega a la carpeta de herramientas de seguridad:
cd soc_tools

#Ejecuta el escáner de prevención de fuga de datos:
python3 dlp_scanner.py

##🛡️ 5. Defensa Activa: Sanitización y Data Masking
El backend de la aplicación no solo registra información, sino que implementa una capa de Defensa en el Edge.

#Función: 
El motor de sanitización detecta secretos (códigos numéricos y credenciales) antes de que sean procesados.

#Resultado: 
Los datos sensibles son reemplazados por etiquetas [REDACTED-CODE] o [REDACTED-PASSWORD] en los logs de auditoría.

#Importancia: 
Esto garantiza que, incluso si un atacante accede a los logs del sistema, la información crítica del usuario no esté expuesta.

###Este proyecto es un ejercicio de laboratorio para el desarrollo de habilidades en DevSecOps, Seguridad de Datos y Respuesta ante Incidentes.
