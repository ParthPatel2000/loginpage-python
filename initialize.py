import csv

header = ['username', 'password']
with open('mydb.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerow({'username': 'dummy', 'password': 'dummy'})
    writer.writerow({'username': 'A', 'password': '1234'})
    writer.writerow({'username': 'B', 'password': '1234'})
    writer.writerow({'username': 'C', 'password': '1234'})
