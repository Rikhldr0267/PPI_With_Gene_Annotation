!pip install dgl

import torch
import dgl
import dgl.function as fn
import torch.nn as nn
import torch.nn.functional as F

class GAT(nn.Module):
    def __init__(self, in_feats, hidden_feats, num_heads, dropout):
        super(GAT, self).__init__()
        self.num_heads = num_heads
        self.dropout = dropout

        self.layer1 = nn.ModuleList()
        self.layer2 = nn.ModuleList()

        for i in range(num_heads):
            self.layer1.append(nn.Linear(in_feats, hidden_feats))
            self.layer2.append(nn.Linear(hidden_feats, 1))

    def forward(self, g, inputs):
        h = inputs

        for i in range(self.num_heads):
            W = self.layer1[i](h)
            Wh = self.layer2[i](W)

            # Compute attention scores
            a = dgl.ops.edge_softmax(g, Wh)

            # Apply dropout to attention scores
            a = F.dropout(a, p=self.dropout, training=self.training)

            # Compute message passing
            h = dgl.ops.sspmm(g, W, a)

        return h
