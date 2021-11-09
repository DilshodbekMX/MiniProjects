import csv
with open("data/new_csv.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        oX = row[0]
        oY = row[1]
        print (oX, oY)
