import csv
import os

# with open("test.csv", 'r') as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         print(row)
# print(csv_reader)

import csv
file = open("test.csv")
csv_f = csv.reader(file)
for row in csv_f:
    Name, Age, City = row
    print("Name: {}, Age: {}, City: {}".format(Name, Age, City))
file.close()