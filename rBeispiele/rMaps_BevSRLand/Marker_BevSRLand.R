# Interaktive Karte mit Bevölkerungsanzahl im Jahr 2013 pro Gemeinde im Bezirk
# Steyr-Land (OÖ)
# Autor: DataDonk23 (datadonk23@gmail.com)
# Datum: 23-02-2014
# Referenz: Libraries (rCharts, rMaps) und 
#           Beispielvorlage von Ramnath Vaidyanathan (https://github.com/ramnathv/)
# __________________________________________________________________________________

require(rCharts)
library(rMaps)

# Karte
# OSM (MapQuestOpen)
map <- Leaflet$new()
map$setView(c(47.98, 14.43), 10) # Koordinaten Zentrum

# Kartenstil
# OSM, customized rendered like in library example 3
map$tileLayer("http://{s}.tile.cloudmade.com/BC9A493B41014CAABB98F0471D759707/997/256/{z}/{x}/{y}.png")
#map$tileLayer("http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png") # OSM Karte
#map #test


# Bevoelkerungsdaten
# Volkszählungen bzw. ZMR-Populationsregister; Statistik Austria. 
# Via: Land OOe, Abteilung Statistik
url <- "http://data.ooe.gv.at/files/cms/OOE_Bevoelkerung_seit_1869.csv"
pop.total  <- data.frame(read.csv2(url))
pop.2013  <- subset(pop.total, pop.total$YEAR == 2013)

# Gemeinde Geokoordinaten: dl http://iam.at/austria; dl 15.02.2014
# Koordinaten abfragen und in .csv speichern
coord.ooe  <- read.csv("DataDir/statooe/GemeindenOOe_Koord.csv")

# Datenprozessierung
gem.data  <- merge(pop.2013, coord.ooe, by.x = "COMMUNE_CODE", by.y = "GEMKZ")
data.2013  <-  gem.data[c(1, 3, 5, 11, 12)]
data.SRLand.tmp  <- subset(data.2013, data.2013$COMMUNE_CODE > 41500)
data.SRLand  <- subset(data.SRLand.tmp, data.SRLand.tmp$COMMUNE_CODE <= 41522, select = c(4, 5, 3, 2))
data.SR  <- subset(data.2013, data.2013$COMMUNE_CODE == 40201, select = c(4, 5, 3, 2))
data  <- rbind(data.SRLand, data.SR)

# Funktion: Marker erstellen
create.marker  <- function (row) {
  map$marker(c(data[row,1], data[row,2]), bindPopup = paste(data[row,4], ":", data[row,3], "EW", sep=" "))
}

# Marker aus Daten erstellen
i=1
for (i in 1:as.integer(nrow(data))){
  create.marker(i)
}

# Karte zeichnen
map
