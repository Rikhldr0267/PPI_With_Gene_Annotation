!pip install -q torch-scatter -f https://data.pyg.org/whl/torch-1.13.1+cu116.html
!pip install -q torch-sparse -f https://data.pyg.org/whl/torch-1.13.1+cu116.html
!pip install -q git+https://github.com/pyg-team/pytorch_geometric.git
import torch; print(torch.__version__)
import torch; print(torch.cuda.is_available())
import networkx as nx
import matplotlib.pyplot as plt
#!pip install git+https://github.com/pyg-team/pyg-lib.git
#!pip install torch-scatter
#!pip install torch-sparse
#!pip install torch-geometric
