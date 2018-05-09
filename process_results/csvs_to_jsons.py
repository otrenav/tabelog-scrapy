
import os
import pandas

data_files = os.listdir(os.getcwd() + '/inputs/json/')
n_data_files = len(data_files)
counter = 1

print('[+] Executing: JSONs to CSVs...')

for f in data_files:
    print('[{}/{}] {}'.format(counter, n_data_files, f))
    data = pandas.read_json('./inputs/json/' + f, encoding="utf-8")
    data.to_csv('./inputs/csv/raw/' + f.replace('.json', '.csv'),
                encoding="utf-8", index=False)
    counter += 1
