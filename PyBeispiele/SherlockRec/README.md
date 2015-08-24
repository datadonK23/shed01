SherlockRec
===========

Empfehlungsmaschine, die basierenden auf abgegebene (simulierte!) Ratings von Benutzern eine Empfehlung über Bücher aus der Sherlock Holmes Reihe von Sir Arthur Conan Doyle abgibt.

## Repository enthält:
Ressourcendateien, Anwendungen und Beispieldaten (falls keine Downloadanweisung in den Projekten enthalten ist) aus den Beispielen des Shed01 Blogs (http://shed01.blogspot.co.at/):
* LICENCE: Lizenztext
* NOTICE: Notice Datei
* ./app - App directory #FIXME
* ./data - Data directory - references in "./data/ref.txt"
* ./instance - Directory for secret configs [not on GitHub]
* config.py - Config of app #FIXME
* requirements.txt - Python requirements for app #FIXME
* run.py - run to launch the app #FIXME

## Datenreferenzen:
* FIXME


## Einrichtung
* Datenbank: Erzeuge in PostgreSQL einen Benutzer pgRec mit beliebigen Passwort; Erzeuge Datenbank mit ./data/create_DB.sql; Erzeuge Tabellen mit ./data/create_Tables.sql
* Importiere simulierte Ratings mit simulate_ratings.py
* FIXME

### Kontakt: datadonk23@gmail.com

### Lizenz: Apache Licence, Version 2 (siehe LICENSE Datei)
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
