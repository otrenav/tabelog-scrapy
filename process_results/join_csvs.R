
print('[+] Executing: Join CSVs...')

data_files <- list.files('./inputs/csv/clean/')
n_data_files <- length(data_files)
counter <- 1

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

data_joined <- NULL

for (f in data_files) {
    print(paste('[', counter, '/', n_data_files, '] ', f, sep = ''))
    data <- read.csv(
        paste('./inputs/csv/clean/', f, sep = ''),
        na.strings = c("", " ", "NA"),
        stringsAsFactors = FALSE
    )
    if (!is.null(data_joined)) {
        data_joined <- fix_columns(data_joined, data)
        data        <- fix_columns(data, data_joined)
    }
    data_joined <- rbind(data_joined, data)
    counter <- counter + 1
}

names(data_joined) <- gsub("_", ".", names(data_joined))

write.csv(data_joined, "./outputs/data.csv", row.names = FALSE)
