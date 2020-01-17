import csv

reader = csv.reader(open("new_PC_Import_2014_2015.csv"))
reader1 = csv.reader(open("new_PC_Import_2015_2016.csv"))
reader2 = csv.reader(open("new_PC_Import_2016_2017.csv"))

f = open("imports.csv", "w")
writer = csv.writer(f)

for row in reader:
    writer.writerow(row)

next(reader1)
for row in reader1:
    writer.writerow(row)

next(reader2)
for row in reader2:
    writer.writerow(row)
f.close()
