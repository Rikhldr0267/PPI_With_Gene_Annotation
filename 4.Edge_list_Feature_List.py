import requests
import pandas as pd

furl = 'https://raw.githubusercontent.com/Rikhldr0267/GNN_PPI/main/orca_count_dictionary_ver1.json'
res1 = requests.get(furl)
fdata = res1.json()
eurl = 'https://raw.githubusercontent.com/Rikhldr0267/GNN_PPI/main/Proteins_for_MCODE.csv'
#res2 = requests.get(eurl)
edata = pd.read_csv(eurl,delimiter=',')
list_of_rows = [list(row) for row in edata.values]
print((list_of_rows))
# list_of_rows is the list format of that  csv file dataset

protein_list = []


response = requests.get(eurl)
content = response.content.decode('utf-8')

for row in csv.reader(content.splitlines()[1:]):
    protein_list.append(row[0])




#set of unique proteins
only_pr=set()
for tup in list_of_rows:
  for x in tup:
    only_pr.add(x)
sorted(only_pr)  



print("Hello")  
print(len(only_pr))
print("Only protein done")
only_prtn = list(set(protein_list))
print("unique protein = ",len(only_prtn))

# "only_prtn" - is an unique protein list

def Convert(tup):
    di={}
    idx=0
    for a in tup:
      di[a]=idx
      idx=idx+1
    return di
dict_nodes=Convert(only_prtn)
print((dict_nodes))

#This code initializes an empty list Edges_list and then appends two empty lists to it.
Edges_list = []
Edges_list.append([])
Edges_list.append([])


for i in range(len(list_of_rows)):
    node1 = dict_nodes.get(list_of_rows[i][0])
    node2 = dict_nodes.get(list_of_rows[i][1])
    if node1 is not None and node2 is not None:
        Edges_list[0].append(node1)
        Edges_list[1].append(node2)
print("Edge list = ",len(Edges_list[0]))
#1118

print(Edges_list[0])
print("and")
print(Edges_list[1])
# Create List of Edges in Number values


# for i in range(len(list_of_rows)):
#     Edges_list[0].append(dict_nodes.get(list_of_rows[i][0]))
#     Edges_list[1].append(dict_nodes.get(list_of_rows[i][1]))
# print(Edges_list[0][0])    
# print(Edges_list[1][0])   
# print("Edge list = ",len(Edges_list[0]))




# the edge list will likely be a list of two sublists containing 
# integers, where each pair of integers represents an edge in a graph.

#suppose ['P06400', 'P29374'] is a protein bond , then edge_list[0] will contain the index of P06400
# P29374 index in edge_index[1]

ct = 0
Feat_list=[]
i=0
for xprtn in only_prtn:
  ct=ct+1
  #Feat_list.append([])
  Feat_list.append(fdata.get(xprtn))
  #print("len = ",len(Feat_list))
  i=i+1

print(len(Edges_list[0]))
print(i)
