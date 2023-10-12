import torch
import torch.nn as nn
import torch.nn.functional as F
import pandas as pd
import numpy
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

class Model(nn.Module):

    def __init__(self, input_features=4, h1=8, h2=9, output_features=3):
        super().__init__()
        self.fc1 = nn.Linear(input_features, h1)
        self.fc2 = nn.Linear(h1, h2)
        self.out = nn.Linear(h2, output_features)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.out(x)

        return x

def main():
    torch.manual_seed(41)
    model = Model()
    url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
    my_df = pd.read_csv(url)

    my_df['variety'] = my_df['variety'].replace('Setosa', 0.0)
    my_df['variety'] = my_df['variety'].replace('Versicolor', 1.0)
    my_df['variety'] = my_df['variety'].replace('Virginica', 2.0)


    X = my_df.drop('variety', axis=1)
    y = my_df['variety']
    X = X.values
    y = y.values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=41)

    X_train = torch.FloatTensor(X_train)
    X_test = torch.FloatTensor(X_test)

    y_train = torch.LongTensor(y_train)
    y_train = torch.LongTensor(y_test)

    criterion = nn.CrossEntropyLoss()

    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    epochs = 100
    losses = []

    for i in range(epochs):
        y_pred = model.forward(X_train)
        y_pred = y_pred.view(30, -1)
        loss = criterion(y_pred, y_train)
        losses.append(loss.detach().numpy())

        if i % 10 == 0:
            print(f'Epoch: {i} and loss: {loss}')
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    
    plt.plot(range(epochs), losses)
    plt.ylabel("loss/error")
    plt.xlabel("Epoch")
    plt.show()

if __name__ == "__main__":
    main()