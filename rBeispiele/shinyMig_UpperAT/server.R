# server.R

library(maptools); library(ggplot2); library(ggmap); library(scales);
library(Hmisc); library(plyr); source("vizHelpers.R")

# raw data
raw.data  <- read.csv2("data/OOE_Wanderungen_Zeitreihe.csv")
raw.data$bez.nr  <- as.integer(raw.data$COMMUNE_CODE /100)
bez.names  <- c("Linz", "Steyr", "Wels", "Braunau", "Eferding", "Freistadt",
                "Gmunden", "Grieskirchen", "Kirchdorf", "Linz-Land", "Perg",
                "Ried", "Rohrbach", "Schärding", "Steyr-Land", "Urfahr-Umgebung",
                "Vöcklabruck", "Wels-Land")


# split data per year, aggregate per district and add df to list
data.per.year  <-  list()
yearly.tables  <- list()
for (i in 1:11){
  proc.data.year  <- paste("data.", (2001+i), sep="")
  df.per.year  <- assign(proc.data.year, subset(raw.data, raw.data$YEAR == (2001+i)))
  
  immig.bez <- aggregate(IMMIGRATION_TOTAL ~ bez.nr, df.per.year, sum)
  emig.bez <- aggregate(EMIGRATION_TOTAL ~ bez.nr, df.per.year, sum)
  df.bez  <- merge(immig.bez, emig.bez, by="bez.nr")
  df.bez$year  <- 2001+i
  data.per.year[[proc.data.year]]  <- df.bez 
  
  # processing df to printable tables
  yearly.table  <- df.bez[,1:3]
  yearly.table$Migrationssaldo  <- yearly.table[,2] - yearly.table[,3]
  colnames(yearly.table)  <- c("Bezirk", "Immigration", "Emigration", 
                               "Migrationssaldo")
  yearly.table$Bezirk  <- bez.names
  yearly.table$Immigration  <- format(yearly.table$Immigration,
                                           nsmall=0, big.mark=".")
  yearly.table$Emigration  <- format(yearly.table$Emigration,
                                          nsmall=0, big.mark=".")
  yearly.table$Migrationssaldo  <- format(yearly.table$Migrationssaldo,
                                               nsmall=0, big.mark=".")
  yearly.tables[[proc.data.year]]  <- yearly.table
} 

# aggregate immigration and emigration data per district over years
bez.nr  <- c(1:18)
value  <- seq(0, 0, length.out=18)
immig.sum  <- data.frame(bez.nr, value)
emig.sum  <- data.frame(bez.nr, value)
for (i in 1:11){
  for (j in 1:18){
    inc(immig.sum$value[j])  <- data.per.year[[i]][j,2]
    inc(emig.sum$value[j])  <- data.per.year[[i]][j,3]
  }
}

# merge immigration with emigration values and calculate diff 
period.data  <- merge(immig.sum, emig.sum, by="bez.nr")
period.data$saldo  <- period.data$value.x - period.data$value.y 

# process df in clean table format
period.data.table  <- period.data
colnames(period.data.table)  <- c("Bezirk", "Immigration", 
                                  "Emigration", "Migrationssaldo")
period.data.table$Bezirk  <- bez.names
period.data.table$Immigration  <- format(period.data.table$Immigration,
                                         nsmall=0, big.mark=".")
period.data.table$Emigration  <- format(period.data.table$Emigration,
                                        nsmall=0, big.mark=".")
period.data.table$Migrationssaldo  <- format(period.data.table$Migrationssaldo,
                                             nsmall=0, big.mark=".")

shinyServer(
  function(input, output) {
    
    output$map <- renderPlot({
      
      o.data <- switch(input$selPeriod,
                      "per.10" = period.data,
                      "per.year" = eval(parse(text=paste("data.per.year[[",
                                                         (input$i.year - 2000)-1,
                                                         "]]", sep=""))))
      
      create_map(o.data)
      
    })
    
    output$view <- renderTable({
      o.table <- switch(input$selPeriod,
                       "per.10" = period.data.table,
                       "per.year" = eval(parse(text=paste("yearly.tables[[",
                                                          (input$i.year - 2000)-1,
                                                          "]]", sep=""))))
      
      o.table
    }, align="llrrr")
    
  }
)
