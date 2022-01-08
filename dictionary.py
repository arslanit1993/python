a = {
   '1':["快乐","kuàilè","happy",],
   '2':['错','cuò','wrong'],
   '3':['阴','yīn','cloudy'],
}
cor = []
incor = []



def func(b):
    
    while b <= len(a):
        e = input(a[str(b)][0])
        if e == a[str(b)][2]:
            cor.append(a[str(b)][0])
            print('correct, pinyin is',a[str(b)][0], a[str(b)][1])
            return func(b+1)
        else:
            incor.append(a[str(b)][0])
            print('incorrect, try again!')
            return func(b)        
    print(f'you were right {len(cor)} times {cor}, you were wrong {len(incor)} times {incor}')
    d = input("Go again?: y(yes) or n(no)")
    if d == 'y':
        return(func(1))
    else: 
        print("Good bye, Have a nice day")
func(1)
