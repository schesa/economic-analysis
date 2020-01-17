import csv

input = open("exports.csv", 'r')
output = open("clean_exports.csv", 'w')

non_blank = (line for line in input if line.strip())
output.writelines(non_blank)

input.close()
output.close()