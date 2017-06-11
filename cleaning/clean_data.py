##
## Transform results data from JSON to CSV
##
## Omar Trejo
## June, 2017
##

import pandas

print("Reading data...")

data = pandas.read_json(
    "~/Downloads/aichi-2017-06-10.json"
)

print("Saving data...")

data.to_csv(
    "~/Downloads/aichi-2017-06-10_json.csv",
    encoding="utf-8",
    index=False
)
