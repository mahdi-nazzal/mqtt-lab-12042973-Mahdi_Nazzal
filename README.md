
<img width="1920" height="1080" alt="IOT_Header" src="https://github.com/user-attachments/assets/74ade6e4-c7fa-45c2-9afd-fc131e0d8212" />

<div align="center">
 
### Mosquitto Broker + Paho Clients (Multi-Pub / Multi-Sub)

<p>
  <img src="https://img.shields.io/badge/MQTT-Mosquitto-purple" />
  <img src="https://img.shields.io/badge/Python-Paho-blue" />
  <img src="https://img.shields.io/badge/OS-Windows-0078D6" />
  <img src="https://img.shields.io/badge/Student%20ID-12042973-brightgreen" />
</p>

<p><b>Live sensor simulation</b> with topic filtering, real-time messaging, logs, and screenshots.</p>

</div>

---

## 🌐 Introduction

This lab demonstrates a fully functional **MQTT-based IoT communication system** using the **Mosquitto Broker** and the **Paho MQTT client library**. It simulates multiple sensors publishing data in real-time and multiple subscribers receiving only their assigned topics, similar to real IoT cloud messaging.

---

## 🚀 What This Project Does

* ✅ Runs **Mosquitto MQTT Broker** locally on Windows (`localhost:1883`)
* ✅ Uses **Paho MQTT** (Python) to publish/subscribe
* ✅ Includes **three publishers**

  * 🌡️ Temperature Sensor
  * 💧 Humidity Sensor
  * 🔢 People Counter Sensor
* ✅ Includes **three subscribers** (each listens to only one topic)
* ✅ Every message includes **Student ID → 12042973**
* ✅ Includes **logs + screenshots** for publishers, subscribers, and broker status

---
### Logs

Generated automatically in:

* `logs/pub_temperature.log`
* `logs/pub_humidity.log`
* `logs/pub_people.log`
* `logs/sub_temperature.log`
* `logs/sub_humidity.log`
* `logs/sub_people.log`
---

## 📊 MQTT Topics Overview

| Sensor Type       | Topic                      | Publisher File       | Subscriber File      |
| ----------------- | -------------------------- | -------------------- | -------------------- |
| 🌡️ Temperature   | `lab/12042973/temperature` | `pub_temperature.py` | `sub_temperature.py` |
| 💧 Humidity       | `lab/12042973/humidity`    | `pub_humidity.py`    | `sub_humidity.py`    |
| 🔢 People Counter | `lab/12042973/people`      | `pub_people.py`      | `sub_people.py`      |

---

## 🎯 Learning Outcomes

* Installing and validating **Mosquitto Broker** on Windows
* Using **Paho** to publish/subscribe to MQTT topics
* Understanding MQTT **topic isolation** and message routing
* Running real-time pub/sub across multiple terminals
* Producing submission-ready logs and screenshots

---

## 👤 Author

**Mahdi**
**Student ID — 12042973**

## 👨‍🏫 Instructor

**Dr. Mo'men Abu Ghazaleh**

---

<div align="center">

✨ Built for IoT learning, one message at a time.

</div>

