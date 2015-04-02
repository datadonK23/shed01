# ui.R

shinyUI(fluidPage(
  titlePanel("shinyMig OÖ - Migrationsbilanz der oö. Bezirke, 2002 - 2012"),
  
  sidebarLayout(
    sidebarPanel(
      
      selectInput("selPeriod", 
                  label = "Zeitraum:",
                  choices = c("2002 bis 2012" = "per.10", "Bilanz pro Jahr" = "per.year"),
                  selected = "per10"),
      
      conditionalPanel(
        condition="input.selPeriod == 'per.year'",
        sliderInput("i.year", 
                  label = "Jahr:",
                  min = 2002, max = 2012, value = 2012, step=1, format="####")
      ),
      
      helpText("Adjust time period for map and table output.")
      
    ),
    
    mainPanel(
      plotOutput("map"),
      tableOutput("view"),
      h6('"Datenquelle: Land Oberösterreich - data.ooe.gv.at", 2014', align = "center"),
      h6('Anwendung unter Apache Lizenz 2.0, siehe Repo: 
         https://github.com/donK23/rBeispiele_Shed01/tree/master/shinyMig_UpperAT'
         , align = "center")
      )
  )
))