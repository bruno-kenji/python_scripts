import csv
import os

currpath = os.getcwd()
file_name = "{}/performance-2018-09-05.csv".format(currpath)

ReducedTotal = 0
ReducedCount = 0
originalTotal = 0
originalCount = 0
total = 0
with open(file_name, 'r') as csv_file:
    reader = csv.DictReader(csv_file, delimiter=';')
    for row in reader:
        dl = row.get('Downloading (resource)')
        diff = row.get('ReducedBodySize (resource)')
        duration = row.get('Total (resource)')
        if dl:
            if diff and int(diff) < 0:
                ReducedTotal += float(dl)
                ReducedCount += 1
                total += float(duration)
            else:
                originalTotal += float(dl)
                originalCount += 1

print('gzip duration: {}'.format(ReducedTotal / ReducedCount))
print('original duration: {}'.format(originalTotal / originalCount))
print('total: {}'.format(total))
