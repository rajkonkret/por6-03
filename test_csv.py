# ,;
# radek, zenek, konrad
import csv

fields = ['name', 'branch', 'year', 'cgpa']
rows = ['Snachit', 'COE', '3', '9.1']

my_dict = [
    {'branch': 'COE', 'cgpa': '9.1', 'name': 'Nikihil', 'year': 2},
    {'branch': 'COS', 'cgpa': '9', 'name': 'Radek', 'year': 4},
]

file = 'records2.csv'

with open(file, 'w', newline='') as csv_fh:
    csvwriter = csv.DictWriter(csv_fh, fieldnames=fields, delimiter=';')
    csvwriter.writeheader()
    csvwriter.writerows(my_dict)
