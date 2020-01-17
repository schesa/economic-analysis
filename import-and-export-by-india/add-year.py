import csv

reader = csv.reader(open('PC_Export_2014_2015.csv', 'r'))
writer = csv.writer(open('new_PC_Export_2014_2015.csv', 'w'))
headers = next(reader)
headers.append("Year")
writer.writerow(headers)
for row in reader:
    row.append(2014)
    writer.writerow(row)

reader = csv.reader(open('PC_Export_2015_2016.csv', 'r'))
writer = csv.writer(open('new_PC_Export_2015_2016.csv', 'w'))
headers = next(reader)
headers.append("Year")
writer.writerow(headers)
for row in reader:
    row.append(2015)
    writer.writerow(row)

reader = csv.reader(open('PC_Export_2016_2017.csv', 'r'))
writer = csv.writer(open('new_PC_Export_2016_2017.csv', 'w'))
headers = next(reader)
headers.append("Year")
writer.writerow(headers)
for row in reader:
    row.append(2016)
    writer.writerow(row)

reader = csv.reader(open('PC_Import_2014_2015.csv', 'r'))
writer = csv.writer(open('new_PC_Import_2014_2015.csv', 'w'))
headers = next(reader)
headers.append("Year")
writer.writerow(headers)
for row in reader:
    row.append(2014)
    writer.writerow(row)

reader = csv.reader(open('PC_Import_2015_2016.csv', 'r'))
writer = csv.writer(open('new_PC_Import_2015_2016.csv', 'w'))
headers = next(reader)
headers.append("Year")
writer.writerow(headers)
for row in reader:
    row.append(2015)
    writer.writerow(row)

reader = csv.reader(open('PC_Import_2016_2017.csv', 'r'))
writer = csv.writer(open('new_PC_Import_2016_2017.csv', 'w'))
headers = next(reader)
headers.append("Year")
writer.writerow(headers)
for row in reader:
    row.append(2016)
    writer.writerow(row)
