#read csv
import csv
with open('usuarios.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)