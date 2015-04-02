# Helper functions to visualize input

# creates a map from given df with migration data per period or year
create_map  <- function(data.year){

  # map df
  ooe.map <- fortify(readShapePoly(fn="data/bezirksgrenzen"))
  ooe.df  <- as.data.frame(readShapePoly(fn="data/bezirksgrenzen"))
  
  # add commune code to map
  for (i in 0:17){
    ooe.map$bez.code[ooe.map$id == i]  <- ooe.df$GEM_BEZREF[i+1]
  }
  
  if ("year" %in% colnames(data.year)) {
    
    # find specific year of df
    year  <- as.integer(data.year$year[1])
    
    # generate bins
    data.year$mig.saldo  <- data.year$IMMIGRATION_TOTAL - data.year$EMIGRATION_TOTAL
    min.data  <- min(data.year$mig.saldo) - 1
    neg.median  <- median(subset(data.year$mig.saldo, data.year$mig.saldo < 0))
    pos.median  <- median(subset(data.year$mig.saldo, data.year$mig.saldo > 0))
    max.data  <- format(max(data.year$mig.saldo), scientific=FALSE)
    data.year$mig.bins  <- cut(data.year$mig.saldo, c(min.data, neg.median, 0,
                                                      pos.median, max.data),
                               dig.lab=10)
  
    plot.title  <- paste("Migrationsbilanz,", year)
    
  } else {
    
    # generate bins
    neg.median  <- median(subset(data.year$saldo, data.year$saldo < 0)) 
    pos.median  <- median(subset(data.year$saldo, data.year$saldo > 0))
    data.year$mig.bins  <- cut(data.year$saldo, c(min(data.year$saldo)-1, 
                                                      neg.median, 0, pos.median,
                                                      max(data.year$saldo)),
                               dig.lab=10) 
  
    # process commune code
    data.year$bez.nr  <- data.year$bez.nr + 400

    plot.title  <- "Migrationsbilanz, 2002-2012"
    }
  
  # merge map and data df on commune code
  ooe.mapdata  <- merge(ooe.map, data.year, by.x="bez.code", by.y="bez.nr")
  
  # plot map
  map <- ggplot(ooe.mapdata, aes(long, lat, group = group, fill = mig.bins))
  
  map  <- map + geom_polygon() + geom_path(aes(x=long, y=lat, group=group), size=0.05) +
    scale_fill_brewer(palette="RdBu") +#, labels=c("unteres Drittel", "mittleres Drittel", "oberes Drittel")) +
    theme(legend.background = element_rect(fill="gray90"), axis.text.x=element_blank(),
          axis.text.y=element_blank(), axis.title.x=element_blank(), axis.title.y=element_blank(),
          axis.ticks=element_blank(), panel.background=element_rect(fill="gray90"), panel.border=element_blank(),
          panel.grid.major=element_blank(), panel.grid.minor=element_blank(),
          plot.background=element_rect(fill = 'white')) +  
    guides(fill=guide_legend(title="Migrationssaldo\n(Personen)\n")) +
    ggtitle(plot.title)
  map
}
