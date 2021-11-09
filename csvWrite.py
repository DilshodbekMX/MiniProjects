# Import csv file library
import csv

# For ID of the dict_file
s = 0
# open txt file to get some data
with open("data/dont_touch.txt", 'r') as file:
    # Creating and writing csv to a new_csv.csv file
    with open("data/new_csv.csv", 'w') as csv_file:
        writer = csv.writer(csv_file)
        for line in file.readlines():
            writer.writerow([s+1, line.rstrip('\n')])
            s += 1
