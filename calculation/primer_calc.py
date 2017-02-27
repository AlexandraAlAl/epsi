import csv
import pprint

infile = open('C:/Users/sandr_000/django/calculation/data.csv', 'r')

table = []
table = [row for row in csv.reader(infile,delimiter=';')]
infile.close()

for r in range(1,len(table)):
    for c in range(0, len(table[0])):
        table[r][c] =  float(table[r][c])

row = [0.0]*len(table[0])
for c in range(0, len(row)):
    s = 0
    k = 0
    for r in range(1, len(table)):
        k += 1
        s += table[r][c]
    row[c] = round(s/k, 1)
table.append(row)

pprint.pprint(table)
