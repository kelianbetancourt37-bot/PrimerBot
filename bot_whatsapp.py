import time
import requests

ID_INSTANCIA = "710722714801"
TOKEN_INSTANCIA = "d905932c82c14349b27106da057c32004c0d16762842400898"

URL_BASE = f"https://7107.api.greenapi.com/waInstance{ID_INSTANCIA}"

print("🔍 Iniciando modo diagnóstico de Green API...")

# Probar estado de la cuenta
try:
    res_state = requests.get(f"{URL_BASE}/getStateInstance/{TOKEN_INSTANCIA}")
    print(f"📌 Estado de la instancia: {res_state.text}")
except Exception as e:
    print(f"❌ Error al consultar estado: {e}")

while True:
    try:
        url = f"{URL_BASE}/receiveNotification/{TOKEN_INSTANCIA}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200 and response.text.strip():
            notif = response.json()
            print(f"\n📩 NOTIFICACIÓN RECIBIDA:\n{notif}")
            
            # Borrar la notificación de la cola
            receipt_id = notif.get("receiptId")
            if receipt_id:
                requests.delete(f"{URL_BASE}/deleteNotification/{TOKEN_INSTANCIA}/{receipt_id}")
        else:
            print(".", end="", flush=True) # Muestra puntos mientras espera mensajes

    except Exception as e:
        print(f"\n❌ Error de red: {e}")

    time.sleep(2)
