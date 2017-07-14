##
## Clean data due to unwanted *whitespace* characters
##
## Omar Trejo
## March, 2017
##

library(stringr)

print("Reading data...")

file_name <- "~/Downloads/group-14.csv"

data <- read.csv(
    file_name,
    stringsAsFactors = FALSE,
    na.strings = c("", " ", "NA")
)

print("Cleaning data...")

##
## Seems only `top.nearest.station` and `top.telephone` require cleaning
##
data$top.nearest_station <- gsub("\n", "", data$top.nearest_station)
data$top.telephone       <- gsub("\n", "", data$top.telephone)

for (column in colnames(data)) {
    data[, column] <- gsub("\\s+", " ", str_trim(data[, column]))
}

print("Writing data...")

write.csv(data, file_name, row.names = FALSE)
