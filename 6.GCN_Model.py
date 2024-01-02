import torch
import torch.nn.functional as F
from torch.nn import Linear, BatchNorm1d, Dropout
from torch_geometric.nn import GCNConv

embedding_size = 1128

class GCN(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, dropout_rate):
        super(GCN, self).__init__()
        self.conv1 = GCNConv(input_dim, hidden_dim)
        self.bn1 = BatchNorm1d(hidden_dim)
        self.conv2 = GCNConv(hidden_dim, hidden_dim)
        self.bn2 = BatchNorm1d(hidden_dim)
        self.conv3 = GCNConv(hidden_dim, hidden_dim)
        self.bn3 = BatchNorm1d(hidden_dim)
        self.dropout = Dropout(p=dropout_rate)
        self.classifier = Linear(hidden_dim, output_dim)

    def forward(self, x, edge_index):
        h = self.conv1(x, edge_index)
        h = self.bn1(h)
        h = F.relu(h)
        h = self.dropout(h)
        h = self.conv2(h, edge_index)
        h = self.bn2(h)
        h = F.relu(h)
        h = self.dropout(h)
        h = self.conv3(h, edge_index)
        h = self.bn3(h)
        h = F.relu(h)
        h = self.dropout(h)  # Final GNN embedding space.
        out = self.classifier(h).squeeze()

        return out, h

model = GCN(input_dim=data.num_features, hidden_dim=embedding_size,
            output_dim=1, dropout_rate=0.5)
print(model)
