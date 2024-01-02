import torch.optim as optim
import torch.nn.functional as F
import matplotlib.pyplot as plt

# Define optimizer and loss function
optimizer = optim.Adam(model.parameters(), lr=0.01)
criterion = torch.nn.BCEWithLogitsLoss()

train_losses = []
test_losses = []
test_accuracies = []

def train():
    model.train()
    optimizer.zero_grad()
    out, h = model(data.x, data.edge_index)
    loss = criterion(out.squeeze(), data.y.float())
    loss.backward()
    optimizer.step()
    train_losses.append(loss.item())
    return loss.item()

def test():
    model.eval()
    with torch.no_grad():
        out, h = model(data.x, data.edge_index)
        pred = torch.round(torch.sigmoid(out))
        test_loss = criterion(out.squeeze(), data.y.float())
        test_losses.append(test_loss.item())
        acc = ((pred == data.y).sum().item() / len(data.y))
        test_accuracies.append(acc)
        return acc

# Train the model for 200 epochs
for epoch in range(1, 1001):
    loss = train()
    if epoch % 10 == 0:
        acc = test()
        print(f"Epoch {epoch}, Loss: {loss:.4f}, Accuracy: {acc:.4f}")

# Plot the loss and accuracy graphs
plt.figure(figsize=(10, 5))
plt.plot(train_losses, label='Train Loss')
plt.plot(test_losses, label='Test Loss')
plt.title('Loss During Training')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(test_accuracies)
plt.title('Test Accuracy During Training')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.show()
