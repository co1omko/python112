import csv

with open('data2.csv') as f:
    name = ['hostname', 'vendor', 'model', 'location']
    write = csv.DictReader(f, delimiter=";", lineterminator="\r", fieldnames=name)
    for row in write:
        print(f"['{row['hostname']}', '{row['vendor']}', '{row['model']}', '{row['location']}']")
