import csv

data = data = [
    ['Name', 'Age', 'City'],
    ['Alice', '30', 'New York'],
    ['Bob', '25', 'Los Angeles'],
    ['Charlie', '35', 'Chicago']
]

with open("new file", 'w') as file:
    writer = csv.writer(file)
    writer.writerow(data)