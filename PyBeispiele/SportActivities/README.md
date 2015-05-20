SportActivities
===============

Spyre App zu Testzwecken, die Daten von sportlichen Aktivitäten präsentiert

## Repository enthält:
Python-Skripte und Beispieldaten (falls keine Downloadanweisung in Skripten enthalten ist) aus den Beispielen des Shed01 Blogs (http://shed01.blogspot.co.at/):
* fetch_data.py - Skript holt Daten mit Strava-API und speichert diese in JSON Kollektionen 
* main.py - Skript der Anwendung
* model.py - Modell
* data - Datenordner. Enthält JSON Kollektionen (von fetch_data.py)
* instance - Geheime Konfigurationsdateien [nicht in Repository]. Enthält Token für Strava-API

## Voraussetzungen:
* Python 2.7
* Python Module: pandas, dataspyre, stravalib

## Verwendung
* [Eigene Datenkollektionen mit fetch_data.py erstellen]
* main.py mit Python 2 ausführen
* Navigation in einem beliebigen Browser zu http://localhost:9097

## Attribution
Dank an Adam Hajari (@adamhajari) für das Spyre Projekt

### Kontakt: datadonk23@gmail.com

### Lizenz: Apache License, Version 2 (siehe LICENSE Datei)
Copyright 2015 Thomas Treml

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
