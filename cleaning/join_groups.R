
data_joined <- NULL

final_group <- 14

fix_columns <- function(data_to_fix, data_for_fixing) {
    names_to_fix <- names(data_to_fix)
    names_for_fixing <- names(data_for_fixing)
    names_missing <- !(unlist(lapply(
        names_for_fixing,
        function(x) x %in% names_to_fix
    )))
    data_to_fix[, names_for_fixing[names_missing]] <- NA
    return(data_to_fix)
}

for (i in 1:final_group) {
    print(paste("Working on group ", i, "...", sep = ""))
    data <- read.csv(
        paste("~/Downloads/group-", i, ".csv", sep = ""),
        na.strings = c("", " ", "NA"),
        stringsAsFactors = FALSE
    )
    if (!is.null(data_joined)) {
        data_joined <- fix_columns(data_joined, data)
        data        <- fix_columns(data, data_joined)
    }
    data_joined <- rbind(data_joined, data)
}

names(data_joined) <- gsub("_", ".", names(data_joined))

write.csv(data_joined, "~/Downloads/data.csv", row.names = FALSE)
