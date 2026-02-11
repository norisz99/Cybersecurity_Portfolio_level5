# 📦 Project 37: Supply Chain Attack Simulation

**Focus:** Trojan Development, Code Injection, Process Hiding, OpSec

## 📌 Áttekintés
Ez a projekt egy klasszikus "Supply Chain" (Ellátási lánc) támadást szimulál. A cél bemutatni, hogyan rejthető el rosszindulatú kód egy teljesen legálisnak tűnő, működő alkalmazásban.
A "trójai faló" itt egy egyszerű Számológép, amely a háttérben – a felhasználó tudta nélkül – importálja és futtatja a hátsó kaput (Backdoor).

## 🛠 Fájlok
* `legit_calculator.py`: A felhasználói program (csali). Számológépként működik, de indításkor betölti a kártevőt.
* `malicious_client.py`: A rejtett modul. Csatlakozik a C2 szerverhez (Project 36), és végrehajtja a parancsokat.

## ⚙️ Technikai Részletek
* **Thread Injection:** A kártevő külön szálon (`daemon thread`) fut, így nem akasztja meg a számológép működését.
* **Anti-Forensics:** A kód tartalmazza a `sys.dont_write_bytecode = True` utasítást, amely megakadályozza a `__pycache__` mappák és `.pyc` fájlok létrejöttét, csökkentve a digitális lábnyomot.

## 🚀 Használat
1.  Győződj meg róla, hogy a C2 Szerver (Project 36) fut.
2.  Futtasd a számológépet (az áldozat szerepében):
    ```bash
    python legit_calculator.py
    ```
3.  Használd a számológépet. Eközben a szerver oldalon megjelenik a kapcsolat.

---
**⚠️ Disclaimer:** A kód bemutatja, miért veszélyes ismeretlen forrásból származó szoftvereket futtatni, még ha azok működőképesnek is tűnnek.