import numpy as np 


X = np.array([1,2,3,4,5])

y = np.array([2,4,6,8,10])

w = 0.0 


# The tools needed for backwards propagation 

def forward(x):
    return x * w

def loss(y,y_predicted):
    return ((y - y_predicted)**2).mean()

def gradient(x,y,y_predicted):
    return np.dot(2*x, y_predicted - y).mean()


print(f'Prediction before tranining: f(5) = {forward(5)}')


#Training 

learning_rate = 0.01
n_iters = 20

for iter in range(1, n_iters+1):
    y_pred = forward(X)

    l = loss(y, y_pred)

    dw = gradient(X,y, y_pred)

    w -= learning_rate * dw

    if iter % 1 == 0:
        print(f'epoch{epoch}: w = {w}, loss ={l}')

        
print(f'Prediction after training: f(5)  = {forward(5)}')
        
        
        
        
        
        
        

        

        






    

