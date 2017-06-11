##
## Get the number of observations per prefecture
##
## Omar Trejo
## March, 2017
##

file_name <- "~/Downloads/data.csv"

data <- read.csv(csv)

compute_obs_per_prefecture <- function(data) {
    observations_per_prefecture <- NULL
    for (prefecture in unique(data$top.prefecture)) {
        new_observation <- data.frame(
            prefecture = prefecture,
            n_observations = nrow(
                data[data$top.prefecture == prefecture, ]
            )
        )
        observations_per_prefecture <- rbind(
            observations_per_prefecture,
            new_observation
        )
    }
    return(observations_per_prefecture)
}

obs_per_prefecture <- compute_obs_per_prefecture(data)

##
## TODO: Update numbers
##
obs_per_prefecture[obs_per_prefecture$prefecture == "Aichi",     "n_listed"] <- 47758
obs_per_prefecture[obs_per_prefecture$prefecture == "Akita",     "n_listed"] <- 6367
obs_per_prefecture[obs_per_prefecture$prefecture == "Aomori",    "n_listed"] <- 8262
obs_per_prefecture[obs_per_prefecture$prefecture == "Chiba",     "n_listed"] <- 30764
obs_per_prefecture[obs_per_prefecture$prefecture == "Ehime",     "n_listed"] <- 9424
obs_per_prefecture[obs_per_prefecture$prefecture == "Fukui",     "n_listed"] <- 6184
obs_per_prefecture[obs_per_prefecture$prefecture == "Fukuoka",   "n_listed"] <- 34045
obs_per_prefecture[obs_per_prefecture$prefecture == "Fukushima", "n_listed"] <- 11564
obs_per_prefecture[obs_per_prefecture$prefecture == "Gifu",      "n_listed"] <- 14145
obs_per_prefecture[obs_per_prefecture$prefecture == "Gunma",     "n_listed"] <- 13968
obs_per_prefecture[obs_per_prefecture$prefecture == "Hiroshima", "n_listed"] <- 17812
obs_per_prefecture[obs_per_prefecture$prefecture == "Hokkaido",  "n_listed"] <- 39100
obs_per_prefecture[obs_per_prefecture$prefecture == "Hyogo",     "n_listed"] <- 36096
obs_per_prefecture[obs_per_prefecture$prefecture == "Ibaraki",   "n_listed"] <- 15370
obs_per_prefecture[obs_per_prefecture$prefecture == "Ishikawa",  "n_listed"] <- 15370
obs_per_prefecture[obs_per_prefecture$prefecture == "Iwate",     "n_listed"] <- 7583
obs_per_prefecture[obs_per_prefecture$prefecture == "Kagawa",    "n_listed"] <- 7147
obs_per_prefecture[obs_per_prefecture$prefecture == "Kagoshima", "n_listed"] <- 9912
obs_per_prefecture[obs_per_prefecture$prefecture == "Kanagawa",  "n_listed"] <- 46685
obs_per_prefecture[obs_per_prefecture$prefecture == "Kochi",     "n_listed"] <- 5487
obs_per_prefecture[obs_per_prefecture$prefecture == "Kumamoto",  "n_listed"] <- 10160
obs_per_prefecture[obs_per_prefecture$prefecture == "Kyoto",     "n_listed"] <- 21112
obs_per_prefecture[obs_per_prefecture$prefecture == "Mie",       "n_listed"] <- 11257
obs_per_prefecture[obs_per_prefecture$prefecture == "Miyagi",    "n_listed"] <- 14221
obs_per_prefecture[obs_per_prefecture$prefecture == "Miyazaki",  "n_listed"] <- 7121
obs_per_prefecture[obs_per_prefecture$prefecture == "Nagano",    "n_listed"] <- 17366
obs_per_prefecture[obs_per_prefecture$prefecture == "Nagasaki",  "n_listed"] <- 8395
obs_per_prefecture[obs_per_prefecture$prefecture == "Nara",      "n_listed"] <- 7199
obs_per_prefecture[obs_per_prefecture$prefecture == "Nigata",   "n_listed"] <- 13762
obs_per_prefecture[obs_per_prefecture$prefecture == "Oita",      "n_listed"] <- 7931
obs_per_prefecture[obs_per_prefecture$prefecture == "Okayama",   "n_listed"] <- 11216
obs_per_prefecture[obs_per_prefecture$prefecture == "Okinawa",   "n_listed"] <- 13252
obs_per_prefecture[obs_per_prefecture$prefecture == "Osaka",     "n_listed"] <- 66526
obs_per_prefecture[obs_per_prefecture$prefecture == "Saga",      "n_listed"] <- 4929
obs_per_prefecture[obs_per_prefecture$prefecture == "Saitama",   "n_listed"] <- 33718
obs_per_prefecture[obs_per_prefecture$prefecture == "Shiga",     "n_listed"] <- 6732
obs_per_prefecture[obs_per_prefecture$prefecture == "Shimane",   "n_listed"] <- 4054
obs_per_prefecture[obs_per_prefecture$prefecture == "Shizuoka",  "n_listed"] <- 25124
obs_per_prefecture[obs_per_prefecture$prefecture == "Tochigi",   "n_listed"] <- 13398
obs_per_prefecture[obs_per_prefecture$prefecture == "Tokushima", "n_listed"] <- 5254
obs_per_prefecture[obs_per_prefecture$prefecture == "Tokyo",     "n_listed"] <- 130632
obs_per_prefecture[obs_per_prefecture$prefecture == "Tottori",   "n_listed"] <- 3638
obs_per_prefecture[obs_per_prefecture$prefecture == "Toyama",    "n_listed"] <- 6550
obs_per_prefecture[obs_per_prefecture$prefecture == "Wakayama",  "n_listed"] <- 7130
obs_per_prefecture[obs_per_prefecture$prefecture == "Yamagata",  "n_listed"] <- 7642
obs_per_prefecture[obs_per_prefecture$prefecture == "Yamaguchi", "n_listed"] <- 8180
obs_per_prefecture[obs_per_prefecture$prefecture == "Yamanashi", "n_listed"] <- 7228

obs_per_prefecture$percentage_captured <- (
    obs_per_prefecture$n_observations /
    obs_per_prefecture$n_listed
)

print(obs_per_prefecture)

write.csv(
    obs_per_prefecture,
    paste(
        "~/Downloads/tabelog_data/percentages-",
        file_name,
        sep = ""
    ),
    row.names = FALSE
)
