import numpy as np 
import torch
from torch import no_grad 



X = torch.tensor([1,2,3,4,5,6], dtype=torch.float32)
Y = torch.tensor([2,4,6,8,10,12], dtype=torch.float32)

w = torch.tensor(0.0, dtype=torch.float32,requires_grad=True)



def forward(x):
    return w*x


def loss(y,y_predicted):
    return ((y_predicted - y)**2).mean()



print(f'Prediction before the training: forward(5) = {forward(5)} ')

#Training 
learningRate = 0.01
nIters = 10000



for epoch in range(1,nIters+1):

    y_predicted = forward(X)

    l = loss(Y, y_predicted)

    l.backward()


    with torch.no_grad():
        w -= w.grad*learningRate



    w.grad.zero_()

    if epoch%10 == 0:
        print(f'The guess after the prediction {forward(5)}')



    
