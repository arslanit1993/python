import torch 
import torch.nn as nn



#data 
X = torch.tensor([[1],[2],[3],[4],[5]], dtype=torch.float32)
Y = torch.tensor([[2],[4],[6],[8],[10]], dtype=torch.float32)

xTest  = torch.tensor([20], dtype=torch.float32)


nSamples, nFeatures = X.shape
inputSize = nFeatures 
outputSize = nFeatures


#Model 

model = nn.Linear(inputSize, outputSize)

learningRate = 0.01
nIters = 10000


loss = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr = learningRate)



#Training

print(f'Prediction before the training = {model(xTest).item()}')

for epoch in range(1,nIters+1):

    y_pred = model(X)

    l.backward()
    
    l = loss(Y, y_pred)

    optimizer.step()

    optimizer.zero_grad()



print(f'Prediction after the training = {model(xTest).item()}')

    

