import numpy as np 
import torch
from torch import no_grad 
import torch.nn  as nn


X = torch.tensor([[1],[2],[3],[4],[5]], dtype=torch.float32)
Y = torch.tensor([[2],[4],[6],[8],[10]], dtype=torch.float32)


w = torch.tensor(0.0, dtype = torch.float32, requires_grad=True)



def forward(x):
    return w * x 


learningRate = 0.01
nIters = 1000


loss =nn.MSELoss()
optimizer = torch.optim.SGD([w], lr = learningRate)



#Training looop
print(f'Prediciton before the training = {forward(10)}')


for epoch in range(nIters):


    y_pred = forward(X)

    l = loss(y_pred ,  Y)

    l.backward()

    optimizer.step()


    optimizer.zero_grad()



print(f'Prediction after the training =  {forward(10)}')


    
    
    
    
