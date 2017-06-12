##
## Transform results data from JSON to CSV
##
## Omar Trejo
## June, 2017
##

import pandas

print("Reading data...")

data = pandas.read_json(
    "~/Downloads/group-1-2017-06-11.json",
    encoding="utf-8"
)

print("Saving data...")

data.to_csv(
    "~/Downloads/group-1-2017-06-11.csv",
    encoding="utf-8",
    index=False
)
