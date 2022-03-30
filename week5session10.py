import csv
file = open('ex9_cities.csv', 'r')


try:
    csv_reader = csv.reader(file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print("Column names are: ", row)
        else:
            print("Rank:", row[0], "State:", row[1], "City:", row[2], "Population:", row[3])
        line_count += 1
finally:
    file.close()

