
# MQTT Pub/Sub Lab (Mosquitto + Eclipse Paho)


**student Name:** Mahdi Nazzal
**Student ID:** 12042973
**OS:** Windows 11
**Broker:** Eclipse Mosquitto (MQTT) on `localhost:1883`
**Client Library:** Eclipse Paho MQTT (Python)

---

## 1) Project Summary

This repository demonstrates a full MQTT publish/subscribe workflow using the **Mosquitto broker** and **Eclipse Paho**.

Deliverables included:

* Mosquitto broker installed (Windows) and verified running
* Multiple publishers:

  * Temperature sensor publisher
  * Humidity sensor publisher
  * People counter publisher
* Multiple subscribers:

  * Each subscriber listens to a specific topic only
* Message logs from both sides (publishers + subscribers)
* Screenshots proving broker status and message exchange
* Every published payload includes **Student ID: 12042973**

---

## 2) MQTT Topics Used

All topics include the Student ID to keep messages isolated and easy to verify:

* `lab/12042973/temperature`
* `lab/12042973/humidity`
* `lab/12042973/people`


## 3) Requirements

* Windows PowerShell
* Python 3.x
* Mosquitto installed on Windows
* Paho MQTT installed in Python

Install dependency:

```powershell
pip install paho-mqtt
```

---

## 4) Mosquitto Broker Setup (Windows)

### 4.1 Verify Mosquitto is Running (Proof Screenshot Required)

Any ONE of these is accepted as proof your broker is running:

**Option A: Windows Services**

1. Press `Win + R` → type `services.msc`
2. Find `Mosquitto Broker`
3. Confirm `Status = Running`
4. Screenshot and save as: `screenshots/broker_running.png`

**Option B: Port Listening Check**
Run:

```bat
netstat -an | findstr 1883
```

If you see `LISTENING` on port `1883`, broker is working. Screenshot it.

**Option C: Run Broker Verbosely**
Run:

```bat
mosquitto -v
```

Screenshot the output showing it is listening on port 1883.

---

## 5) Python Environment Setup (Windows PowerShell)

From your project folder:

```powershell
cd "D:\iOT assigment\mqtt-lab"
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install paho-mqtt
pip freeze > requirements.txt
```

Set the Student ID environment variable (required by the lab):

```powershell
$env:STUDENT_ID="12042973"
```

---

## 6) How To Run (6 Terminals)

Open **6 separate PowerShell terminals**.

In EACH terminal, run this setup first:

```powershell
cd "D:\iOT assigment\mqtt-lab"
.\.venv\Scripts\Activate.ps1
$env:STUDENT_ID="12042973"
mkdir logs -Force
```

### 6.1 Start Subscribers (3 terminals)

**Terminal 1 (Temperature Subscriber)**

```powershell
python .\sub_temperature.py | Tee-Object -FilePath .\logs\sub_temperature.log
```

**Terminal 2 (Humidity Subscriber)**

```powershell
python .\sub_humidity.py | Tee-Object -FilePath .\logs\sub_humidity.log
```

**Terminal 3 (People Subscriber)**

```powershell
python .\sub_people.py | Tee-Object -FilePath .\logs\sub_people.log
```

### 6.2 Start Publishers (3 terminals)

**Terminal 4 (Temperature Publisher)**

```powershell
python .\pub_temperature.py | Tee-Object -FilePath .\logs\pub_temperature.log
```

**Terminal 5 (Humidity Publisher)**

```powershell
python .\pub_humidity.py | Tee-Object -FilePath .\logs\pub_humidity.log
```

**Terminal 6 (People Publisher)**

```powershell
python .\pub_people.py | Tee-Object -FilePath .\logs\pub_people.log
```

Let all scripts run for 20–30 seconds, then stop each terminal using:

* `Ctrl + C`

---

## 7) Screenshots (Required Evidence)

Save all screenshots in the `screenshots/` folder.

Required:

* `broker_running.png`
  Proof broker is running (Services / netstat / mosquitto -v)
* `pub_temperature.png` + `sub_temperature.png`
* `pub_humidity.png` + `sub_humidity.png`
* `pub_people.png` + `sub_people.png`

Each publisher screenshot must show the JSON payload including:

* `student_id: 12042973`

Each subscriber screenshot must show it receiving messages from the correct topic.

(Optional device info screenshot):

* Run `systeminfo` and screenshot → `screenshots/systeminfo.png`

---

## 8) Logs (Required Evidence)

Logs are generated automatically using `Tee-Object` into the `logs/` folder:

Publishers:

* `logs/pub_temperature.log`
* `logs/pub_humidity.log`
* `logs/pub_people.log`

Subscribers:

* `logs/sub_temperature.log`
* `logs/sub_humidity.log`
* `logs/sub_people.log`

---
