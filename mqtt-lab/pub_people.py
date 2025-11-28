import json
import os
import random
import time
from datetime import datetime, timezone

import paho.mqtt.client as mqtt

BROKER_HOST = os.getenv("MQTT_HOST", "localhost")
BROKER_PORT = int(os.getenv("MQTT_PORT", "1883"))
STUDENT_ID = os.getenv("STUDENT_ID", "YOUR_STUDENT_ID")

TOPIC = f"lab/{STUDENT_ID}/people"
CLIENT_ID = f"pub-people-{STUDENT_ID}"

def now_iso():
    return datetime.now(timezone.utc).isoformat()

def on_connect(client, userdata, flags, reason_code, properties=None):
    print(f"[PUB:PEOPLE] Connected, reason_code={reason_code}")

def on_publish(client, userdata, mid, reason_code=None, properties=None):
    print(f"[PUB:PEOPLE] Published mid={mid}")

client = mqtt.Client(client_id=CLIENT_ID, protocol=mqtt.MQTTv311)
client.on_connect = on_connect
client.on_publish = on_publish

client.connect(BROKER_HOST, BROKER_PORT, keepalive=60)
client.loop_start()

try:
    count = 0
    while True:
        # simulate entry/exit
        count = max(0, count + random.choice([-1, 0, 1, 2]))
        payload = {
            "student_id": STUDENT_ID,
            "sensor": "people_counter",
            "unit": "people",
            "value": count,
            "ts": now_iso(),
        }

        msg = json.dumps(payload)
        print(f"[PUB:PEOPLE] -> topic={TOPIC} payload={msg}")
        client.publish(TOPIC, msg, qos=1)
        time.sleep(4)
except KeyboardInterrupt:
    print("[PUB:PEOPLE] Stopping...")
finally:
    client.loop_stop()
    client.disconnect()
