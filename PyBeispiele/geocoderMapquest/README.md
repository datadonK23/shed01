geocoderMapQuest
================

Skript zur Geokodierung von Ortsabfragen, basierend auf Open Geocoding API von Mapquest.

## Repository enthält:
Python-Skripte und Beispieldaten (falls keine Downloadanweisung in Skripten enthalten ist) aus den Beispielen des Shed01 Blogs (http://shed01.blogspot.co.at/):
* geocoder.py - Skript
* Lizenz und Notice Dateien

## Anwendung:
* Erzeuge eine Environmental Variable ["MAPQUEST_API_KEY"] mit dem Authorisierungs Schlüssel, der auf http://developer.mapquest.com bezogen werden kann
* Lade geocoder.py in Projekt
* Verwendung durch Aufruf der Funktion geocodeMQ mit dem Parameter req_location
* req_loc: Ortsabfrage (String)
* Funktion liefert die Koordinaten (Breite und Länge) des Ortes zurueck

## Datenquelle:
* Geocoding Courtesy of MapQuest - please visit http://www.mapquest.com
* Datenquelle basiert auf OpenStreetMaps Daten, Lizenz und Nutzungsbedingungen unter www.opendatacommons.org/licenses/odbl bzw. www.openstreetmap.org/copyright

### Kontakt: datadonk23@gmail.com

### Lizenz: Apache License, Version 2 (siehe LICENSE Datei)
Copyright 2014 Thomas Treml

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
