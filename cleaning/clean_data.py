##
## Transform results data from JSON to CSV
##
## Omar Trejo
## June, 2017
##

import pandas

print("Reading data...")

data = pandas.read_json(
    "~/Downloads/group-14.json"
    encoding="utf-8"
)

print("Saving data...")

data.to_csv(
    "~/Downloads/group-14.csv",
    encoding="utf-8",
    index=False
)
