
data <- read.csv(
    "~/Downloads/data.csv",
    na.strings = c("", " ", "NA"),
    stringsAsFactors = FALSE
)

data <- data[!is.na(data$top.prefecture), ]

write.csv(data, "~/Downloads/data.csv", row.names = FALSE)

print("Done.")
