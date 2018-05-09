
library(dplyr)

#
# NA by prefecture and variable
#

print('[+] Executing: NAs by prefecture and variable...')

data <- read.csv(
    "./outputs/data.csv",
    stringsAsFactors = FALSE,
    na.strings = c("", " ", "NA")
)

results <- as.data.frame(
    data %>%
    group_by(top.prefecture) %>%
    summarise_all(funs(sum(is.na(.)) / length(.)))
)

write.csv(results, "./outputs/NAs_by_prefecture_and_variable.csv", row.names = FALSE)

# # Get number of `addresses` with `-ku` inside
# tokyo_indexes <- which(data$top.prefecture == "Tokyo")

# n_observations_with_ku_in_address <- sum(unlist(lapply(
#     data[tokyo_indexes, "shop.addresses"],
#     function(x) grepl("-ku", x)
# )))

# print(n_observations_with_ku_in_address / nrow(data[tokyo_indexes, ]))

#
# Get the number of observations per prefecture
#

print('[+] Executing: Number of observations per prefecture...')

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

obs_per_prefecture[obs_per_prefecture$prefecture == "Aichi",     "n_listed_before"] <- 47758
obs_per_prefecture[obs_per_prefecture$prefecture == "Akita",     "n_listed_before"] <- 6367
obs_per_prefecture[obs_per_prefecture$prefecture == "Aomori",    "n_listed_before"] <- 8262
obs_per_prefecture[obs_per_prefecture$prefecture == "Chiba",     "n_listed_before"] <- 30764
obs_per_prefecture[obs_per_prefecture$prefecture == "Ehime",     "n_listed_before"] <- 9424
obs_per_prefecture[obs_per_prefecture$prefecture == "Fukui",     "n_listed_before"] <- 6184
obs_per_prefecture[obs_per_prefecture$prefecture == "Fukuoka",   "n_listed_before"] <- 34045
obs_per_prefecture[obs_per_prefecture$prefecture == "Fukushima", "n_listed_before"] <- 11564
obs_per_prefecture[obs_per_prefecture$prefecture == "Gifu",      "n_listed_before"] <- 14145
obs_per_prefecture[obs_per_prefecture$prefecture == "Gunma",     "n_listed_before"] <- 13968
obs_per_prefecture[obs_per_prefecture$prefecture == "Hiroshima", "n_listed_before"] <- 17812
obs_per_prefecture[obs_per_prefecture$prefecture == "Hokkaido",  "n_listed_before"] <- 39100
obs_per_prefecture[obs_per_prefecture$prefecture == "Hyogo",     "n_listed_before"] <- 36096
obs_per_prefecture[obs_per_prefecture$prefecture == "Ibaraki",   "n_listed_before"] <- 15370
obs_per_prefecture[obs_per_prefecture$prefecture == "Ishikawa",  "n_listed_before"] <- 15370
obs_per_prefecture[obs_per_prefecture$prefecture == "Iwate",     "n_listed_before"] <- 7583
obs_per_prefecture[obs_per_prefecture$prefecture == "Kagawa",    "n_listed_before"] <- 7147
obs_per_prefecture[obs_per_prefecture$prefecture == "Kagoshima", "n_listed_before"] <- 9912
obs_per_prefecture[obs_per_prefecture$prefecture == "Kanagawa",  "n_listed_before"] <- 46685
obs_per_prefecture[obs_per_prefecture$prefecture == "Kochi",     "n_listed_before"] <- 5487
obs_per_prefecture[obs_per_prefecture$prefecture == "Kumamoto",  "n_listed_before"] <- 10160
obs_per_prefecture[obs_per_prefecture$prefecture == "Kyoto",     "n_listed_before"] <- 21112
obs_per_prefecture[obs_per_prefecture$prefecture == "Mie",       "n_listed_before"] <- 11257
obs_per_prefecture[obs_per_prefecture$prefecture == "Miyagi",    "n_listed_before"] <- 14221
obs_per_prefecture[obs_per_prefecture$prefecture == "Miyazaki",  "n_listed_before"] <- 7121
obs_per_prefecture[obs_per_prefecture$prefecture == "Nagano",    "n_listed_before"] <- 17366
obs_per_prefecture[obs_per_prefecture$prefecture == "Nagasaki",  "n_listed_before"] <- 8395
obs_per_prefecture[obs_per_prefecture$prefecture == "Nara",      "n_listed_before"] <- 7199
obs_per_prefecture[obs_per_prefecture$prefecture == "Nigata",    "n_listed_before"] <- 13762
obs_per_prefecture[obs_per_prefecture$prefecture == "Oita",      "n_listed_before"] <- 7931
obs_per_prefecture[obs_per_prefecture$prefecture == "Okayama",   "n_listed_before"] <- 11216
obs_per_prefecture[obs_per_prefecture$prefecture == "Okinawa",   "n_listed_before"] <- 13252
obs_per_prefecture[obs_per_prefecture$prefecture == "Osaka",     "n_listed_before"] <- 66526
obs_per_prefecture[obs_per_prefecture$prefecture == "Saga",      "n_listed_before"] <- 4929
obs_per_prefecture[obs_per_prefecture$prefecture == "Saitama",   "n_listed_before"] <- 33718
obs_per_prefecture[obs_per_prefecture$prefecture == "Shiga",     "n_listed_before"] <- 6732
obs_per_prefecture[obs_per_prefecture$prefecture == "Shimane",   "n_listed_before"] <- 4054
obs_per_prefecture[obs_per_prefecture$prefecture == "Shizuoka",  "n_listed_before"] <- 25124
obs_per_prefecture[obs_per_prefecture$prefecture == "Tochigi",   "n_listed_before"] <- 13398
obs_per_prefecture[obs_per_prefecture$prefecture == "Tokushima", "n_listed_before"] <- 5254
obs_per_prefecture[obs_per_prefecture$prefecture == "Tokyo",     "n_listed_before"] <- 130632
obs_per_prefecture[obs_per_prefecture$prefecture == "Tottori",   "n_listed_before"] <- 3638
obs_per_prefecture[obs_per_prefecture$prefecture == "Toyama",    "n_listed_before"] <- 6550
obs_per_prefecture[obs_per_prefecture$prefecture == "Wakayama",  "n_listed_before"] <- 7130
obs_per_prefecture[obs_per_prefecture$prefecture == "Yamagata",  "n_listed_before"] <- 7642
obs_per_prefecture[obs_per_prefecture$prefecture == "Yamaguchi", "n_listed_before"] <- 8180
obs_per_prefecture[obs_per_prefecture$prefecture == "Yamanashi", "n_listed_before"] <- 7228

obs_per_prefecture[obs_per_prefecture$prefecture == "Aichi",     "n_listed"] <- 19668
obs_per_prefecture[obs_per_prefecture$prefecture == "Akita",     "n_listed"] <- 3520
obs_per_prefecture[obs_per_prefecture$prefecture == "Aomori",    "n_listed"] <- 2421
obs_per_prefecture[obs_per_prefecture$prefecture == "Chiba",     "n_listed"] <- 94642
obs_per_prefecture[obs_per_prefecture$prefecture == "Ehime",     "n_listed"] <- 9424
obs_per_prefecture[obs_per_prefecture$prefecture == "Fukui",     "n_listed"] <- 2189
obs_per_prefecture[obs_per_prefecture$prefecture == "Fukuoka",   "n_listed"] <- 17558
obs_per_prefecture[obs_per_prefecture$prefecture == "Fukushima", "n_listed"] <- 3983
obs_per_prefecture[obs_per_prefecture$prefecture == "Gifu",      "n_listed"] <- 18280
obs_per_prefecture[obs_per_prefecture$prefecture == "Gunma",     "n_listed"] <- 8311
obs_per_prefecture[obs_per_prefecture$prefecture == "Hiroshima", "n_listed"] <- 7005
obs_per_prefecture[obs_per_prefecture$prefecture == "Hokkaido",  "n_listed"] <- 15679
obs_per_prefecture[obs_per_prefecture$prefecture == "Hyogo",     "n_listed"] <- 43000
obs_per_prefecture[obs_per_prefecture$prefecture == "Ibaraki",   "n_listed"] <- 11851
obs_per_prefecture[obs_per_prefecture$prefecture == "Ishikawa",  "n_listed"] <- 5384
obs_per_prefecture[obs_per_prefecture$prefecture == "Iwate",     "n_listed"] <- 2958
obs_per_prefecture[obs_per_prefecture$prefecture == "Kagawa",    "n_listed"] <- 2414
obs_per_prefecture[obs_per_prefecture$prefecture == "Kagoshima", "n_listed"] <- 204
obs_per_prefecture[obs_per_prefecture$prefecture == "Kanagawa",  "n_listed"] <- 24309
obs_per_prefecture[obs_per_prefecture$prefecture == "Kochi",     "n_listed"] <- 1391
obs_per_prefecture[obs_per_prefecture$prefecture == "Kumamoto",  "n_listed"] <- 4382
obs_per_prefecture[obs_per_prefecture$prefecture == "Kyoto",     "n_listed"] <- 26260
obs_per_prefecture[obs_per_prefecture$prefecture == "Mie",       "n_listed"] <- 6566
obs_per_prefecture[obs_per_prefecture$prefecture == "Miyagi",    "n_listed"] <- 7418
obs_per_prefecture[obs_per_prefecture$prefecture == "Miyazaki",  "n_listed"] <- 2838
obs_per_prefecture[obs_per_prefecture$prefecture == "Nagano",    "n_listed"] <- 7891
obs_per_prefecture[obs_per_prefecture$prefecture == "Nagasaki",  "n_listed"] <- 15734
obs_per_prefecture[obs_per_prefecture$prefecture == "Nara",      "n_listed"] <- 2249
obs_per_prefecture[obs_per_prefecture$prefecture == "Nigata",    "n_listed"] <- 5202
obs_per_prefecture[obs_per_prefecture$prefecture == "Oita",      "n_listed"] <- 2759
obs_per_prefecture[obs_per_prefecture$prefecture == "Okayama",   "n_listed"] <- 6533
obs_per_prefecture[obs_per_prefecture$prefecture == "Okinawa",   "n_listed"] <- 4569
obs_per_prefecture[obs_per_prefecture$prefecture == "Osaka",     "n_listed"] <- 50152
obs_per_prefecture[obs_per_prefecture$prefecture == "Saga",      "n_listed"] <- 3336
obs_per_prefecture[obs_per_prefecture$prefecture == "Saitama",   "n_listed"] <- 5893
obs_per_prefecture[obs_per_prefecture$prefecture == "Shiga",     "n_listed"] <- 3207
obs_per_prefecture[obs_per_prefecture$prefecture == "Shimane",   "n_listed"] <- 2179
obs_per_prefecture[obs_per_prefecture$prefecture == "Shizuoka",  "n_listed"] <- 6291
obs_per_prefecture[obs_per_prefecture$prefecture == "Tochigi",   "n_listed"] <- 4702
obs_per_prefecture[obs_per_prefecture$prefecture == "Tokushima", "n_listed"] <- 1514
obs_per_prefecture[obs_per_prefecture$prefecture == "Tokyo",     "n_listed"] <- 80184
obs_per_prefecture[obs_per_prefecture$prefecture == "Tottori",   "n_listed"] <- 270
obs_per_prefecture[obs_per_prefecture$prefecture == "Toyama",    "n_listed"] <- 2404
obs_per_prefecture[obs_per_prefecture$prefecture == "Wakayama",  "n_listed"] <- 2099
obs_per_prefecture[obs_per_prefecture$prefecture == "Yamagata",  "n_listed"] <- 2644
obs_per_prefecture[obs_per_prefecture$prefecture == "Yamaguchi", "n_listed"] <- 2437
obs_per_prefecture[obs_per_prefecture$prefecture == "Yamanashi", "n_listed"] <- 3256

obs_per_prefecture$percentage_captured <- (
    obs_per_prefecture$n_observations /
    obs_per_prefecture$n_listed
)
obs_per_prefecture$percentage_captured_before <- (
    obs_per_prefecture$n_observations /
    obs_per_prefecture$n_listed_before
)

write.csv(
    obs_per_prefecture,
    './outputs/observations_per_prefecture.csv',
    row.names = FALSE
)
