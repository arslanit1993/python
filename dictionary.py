a = {
   '1':["快乐","kuàilè","happy",],
   '2':['错','cuò','wrong'],
   '3':['阴','yīn','cloudy'],
}

#hello
def func(b):
    correct = 0
    incorrect = 0

    while b <= len(a):
        c = input(a[str(b)][0])
        if c == a[str(b)][2]:
            return func(b+1)
                
    
    
func(1)
