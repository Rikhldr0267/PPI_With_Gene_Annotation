import csv
import requests

protein_list = []

url = 'https://raw.githubusercontent.com/Rikhldr0267/GNN_PPI/main/Proteins_for_MCODE.csv'

response = requests.get(url)
content = response.content.decode('utf-8')

for row in csv.reader(content.splitlines()[1:]):
    protein_list.append(row[0])

print("All proteins in dataset -" , len(protein_list))
new_list = list(set(protein_list))
print("All unique proteins -" ,len(new_list))
