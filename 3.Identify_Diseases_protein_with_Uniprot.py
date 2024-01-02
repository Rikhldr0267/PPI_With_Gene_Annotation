import csv
import requests
from google.colab import files

# Read protein names from input CSV file
with open('/content/protein_list_comp.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    protein_list = [row[0] for row in reader]

# Check if each protein is associated with a disease and write results to output CSV file
with open('output_proteins.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Protein Name', 'Disease Association'])

    for protein in protein_list:
        url = f'https://www.uniprot.org/uniprot/{protein}.txt'
        response = requests.get(url)
        content = response.content.decode('utf-8')

        if 'Disease' in content:
            writer.writerow([protein, 'Yes'])
        else:
            writer.writerow([protein, 'No'])

# Download the output CSV file
files.download('output_proteins.csv')

