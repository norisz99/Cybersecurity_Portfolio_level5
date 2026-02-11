# 📡 Project 36: Basic C2 Infrastructure (The Listener)

**Focus:** Network Programming, Socket API, Multi-threaded Server, Reverse Shell

## 📌 Áttekintés
Ez a projekt a "Command & Control" (C2) infrastruktúra alapköve. Egy TCP szervert valósít meg, amely képes fogadni a bejövő kapcsolatokat (Reverse Shell), és távoli parancsokat küldeni a csatlakoztatott klienseknek.
A kód `Multi-threading` (többszálú) technológiát használ, így a szerver nem fagy le, amíg egy klienssel kommunikál, és képes lenne több kapcsolatot is kezelni a háttérben.

## 🛠 Fájlok
* `c2_server.py`: A központi szerver, amely a `9999`-es porton figyel. Kezeli a parancssori bemenetet és a hálózati kommunikációt.

## 🚀 Használat
1.  Indítsd el a szervert a támadó gépen:
    ```bash
    python c2_server.py
    ```
2.  Várd meg, amíg egy kliens (pl. a Project 37-ből) csatlakozik.
3.  Amint a kapcsolat létrejött, kapsz egy interaktív Shellt.
4.  Parancsok: `dir`, `whoami`, `ipconfig`, stb.

## 🧠 Mit tanultam?
* Hogyan működik a **TCP Handshake** és a socket kommunikáció Pythonban.
* Miért kritikus a hibakezelés (pl. UTF-8 kódolási hibák kivédése) a stabil C2 kapcsolatoknál.
* Hogyan lehet Pythonban párhuzamos szálakat kezelni (`threading` modul).

---
**⚠️ Disclaimer:** Ez az eszköz kizárólag oktatási célokat szolgál és saját, izolált tesztkörnyezetben (Localhost) használandó.