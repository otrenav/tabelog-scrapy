
library(dplyr)

data <- read.csv(
    "~/Downloads/data.csv",
    stringsAsFactors = FALSE,
    na.strings = c("", " ", "NA")
)

results <- as.data.frame(
    data %>%
    group_by(top.prefecture) %>%
    summarise_all(funs(sum(is.na(.)) / length(.)))
)

print(results)

write.csv(results, "~/Downloads/NA_by_prefecture_and_variable.csv")


## Get number of `addresses` with `-ku` inside

tokyo_indexes <- which(data$top.prefecture == "Tokyo")

n_observations_with_ku_in_address <- sum(unlist(lapply(
    data[tokyo_indexes, "shop.addresses"],
    function(x) grepl("-ku", x)
)))

print(n_observations_with_ku_in_address / nrow(data[tokyo_indexes, ]))
