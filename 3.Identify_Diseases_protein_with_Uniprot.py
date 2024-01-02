import requests

protein_list = ['P06400', 'P02647', 'P09601', 'P05787', 'P35222', 'P14618', 'Q16539', 'P62753', 'P61981', 'P09382', 'P12830', 'Q9UM73', 'P11362', 'P04637']

for protein in protein_list:
    url = f'https://www.uniprot.org/uniprot/{protein}.txt'
    response = requests.get(url)
    content = response.content.decode('utf-8')

    if 'Disease' in content:
        print(f"{protein} is associated with a disease.")
    else:
        print(f"{protein} is not associated with a disease.")
