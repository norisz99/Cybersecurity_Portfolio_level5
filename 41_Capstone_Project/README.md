# 🛡️ Project 41: "The Gatekeeper" - Captive Portal & DNS Spoofing

**Type:** Capstone Project (Level 5)  
**Techniques:** DNS Poisoning, Man-in-the-Middle (MITM), Social Engineering, Web Hosting

---

## 📌 Project Overview

Ez a projekt egy **Captive Portal** szimuláció, amelyet gyakran használnak "Evil Twin" (Gonosz Iker) támadásoknál. A rendszer lényege, hogy egy izolált hálózaton (pl. egy Rogue Routeren vagy Raspberry Pi-n) átvesszük az irányítást a névszerver (DNS) felett.

Amikor az áldozat csatlakozik a Wi-Fi hálózathoz és megpróbál megnyitni egy weboldalt (pl. `google.com`), a scriptünk elfogja a kérést, és a valódi Google szerver IP címe helyett a **saját támadó gépünk IP címét** küldi vissza. Így a böngésző a mi hamis bejelentkező oldalunkat tölti be.

### 🎯 Key Features
* **DNS Interception:** Minden bejövő DNS kérésre (legyen az Facebook, Google, stb.) a saját IP címünkkel válaszolunk.
* **Custom Web Server:** Egy egyszerű HTTP szerver, amely kiszolgálja a hamis bejelentkező oldalt (`index.html`).
* **Network Isolation:** Demonstrálja, hogyan lehet zárt hálózaton manipulálni a forgalmat internetkapcsolat nélkül is.

---

## 📂 File Structure

* `dns_gatekeeper.py` - A Python script, ami elindítja a hamis DNS szervert (UDP 53-as port).
* `index.html` - A hamis bejelentkező oldal (Phishing landing page).
* `README.md` - Ez a dokumentáció.

---

## 🚀 How to Run (Simulation)

A futtatáshoz két külön terminálablakra van szükség:

### Step 1: Start the DNS Server
Ez a script fogja el a kéréseket és irányítja őket a gépedre.
*(Rendszergazdai jogosultság szükséges az 53-as port miatt!)*

```bash
sudo python dns_gatekeeper.py
# Windows: Rendszergazda CMD -> python dns_gatekeeper.py