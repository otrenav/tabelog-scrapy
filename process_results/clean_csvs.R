
library(stringr)

print('[+] Executing: Clean CSVs...')

data_files <- list.files('./inputs/csv/raw/')
n_data_files <- length(data_files)
counter <- 1

for (f in data_files) {
    print(paste('[', counter, '/', n_data_files, '] ', f, sep = ''))
    data <- read.csv(
        paste('./inputs/csv/raw/', f, sep = ''),
        na.strings = c('', ' ', 'NA'),
        stringsAsFactors = FALSE
    )
    print(paste('    [+] No. rows before: ', nrow(data)))
    data <- data[!is.na(data$top.prefecture), ]
    for (column in colnames(data)) {
        data[, column] <- gsub('\\s+', ' ', str_trim(data[, column]))
        data[, column] <- gsub('\n', '', data[, column])
    }
    print(paste('    [+] No. rows after: ', nrow(data)))
    output_file <- paste('./inputs/csv/clean/', f, sep = '')
    write.csv(data, output_file, row.names = FALSE)
    counter <- counter + 1
}
