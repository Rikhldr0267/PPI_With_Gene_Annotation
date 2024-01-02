import torch
from torch_geometric.data import Data



x = torch.tensor(Feat_list, dtype=torch.float)

labels=[]
temp = 0
a=0
b=0
c=0
#ct=0


# logic to mark disease proteins as 1 and non disease as 0

for i in only_prtn:
  ct=ct+1
  for sub in disease:
    # print(i)
    # print(sub)
    if i in sub:
      labels.append(1)
      a=a+1
      temp=1
      break
  if temp ==0:
    labels.append(0) 
    b=b+1
    temp = 0 
  elif temp==1:
    c=c+1
    temp = 0
    continue  
  else: 
    temp = 0



y = torch.tensor(labels)
print("data = ",len(data.y),"\n")

#Edges_list = [edge for edge in Edges_list if len(edge) == 2 and edge[1] is not None]
edge_index = torch.tensor(Edges_list, dtype=torch.long)
# print((Edges_list))

#edge_index = torch.tensor(Edges_list, dtype=torch.long)

# from torch_geometric.utils import add_self_loops

# data.edge_index, _ = add_self_loops(data.edge_index, num_nodes=data.num_nodes)


data = Data(x=x, y=y, edge_index=edge_index)
print("Data.x loading ...\n")
print((data.x),"\n")
print("Data.y loading ...\n")
print((data.y),"\n")
print("Data.edge_index loading ...\n")
print(data.edge_index)
