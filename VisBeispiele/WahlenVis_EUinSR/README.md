### README

# WahlenVis_EUinSR

### Beschreibung
Dieser Prototyp einer Visualisierungs-Anwendung (basierend auf QtQuick 2.2 und C++) zeigt die Ergebnisse der EU-Wahlen 2014 im politischen Bezirk Steyr-Stadt (Österreich).

### Benutzung
Die App ist für Android Geräte mit einer Bildschirmauflösung von 1.280 x 720 Pixel optimiert, sollte aber auch in anderen Auflösungsstufen (mit Abstrichen in der UX) und auf Desktops lauffähig sein. 

Über die jeweilige Version ist über den passenden Build-Ordner (Android oder Desktop) verfügbar. Das Qt-Creator Projekt ist im Hauptverzeichnis der App zu finden. Zusätzlich sind die prozessierten Ressourcendateien in einem separaten Ordner (./Data) zugänglich.

### Systemvorraussetzungen:
* Qt5 -QtQuick2.2
* Internet-Zugang (für eingebunde Bilddatei)

### Referenzen
* Rohdaten: Download von Amtstafel auf steyr.at (http://www.steyr.at/system/web/zusatzseite.aspx?bezirkonr=0&detailonr=224903717&menuonr=218377747), am 31.05.14
* Umrisse Karte: Image selbt prozessiert auf Basis des Bildmaterials auf http://ftp.steyr.at/magsteyr/statistik/statbez.html (dl. am 31.05.14)

### Lizenz: Apache License (read LICENCE)
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
