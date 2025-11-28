import os
from datetime import datetime

import paho.mqtt.client as mqtt

BROKER_HOST = os.getenv("MQTT_HOST", "localhost")
BROKER_PORT = int(os.getenv("MQTT_PORT", "1883"))
STUDENT_ID = os.getenv("STUDENT_ID", "YOUR_STUDENT_ID")

TOPIC = f"lab/{STUDENT_ID}/temperature"
CLIENT_ID = f"sub-temp-{STUDENT_ID}"

def ts():
    return datetime.now().isoformat(timespec="seconds")

def on_connect(client, userdata, flags, reason_code, properties=None):
    print(f"[SUB:TEMP] Connected, reason_code={reason_code}")
    client.subscribe(TOPIC, qos=1)
    print(f"[SUB:TEMP] Subscribed to {TOPIC}")

def on_message(client, userdata, msg):
    print(f"[{ts()}][SUB:TEMP] <- topic={msg.topic} payload={msg.payload.decode(errors='replace')} qos={msg.qos}")

client = mqtt.Client(client_id=CLIENT_ID, protocol=mqtt.MQTTv311)
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER_HOST, BROKER_PORT, keepalive=60)
client.loop_forever()
