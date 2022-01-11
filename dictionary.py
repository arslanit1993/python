a = {
   '1':["快乐","kuàilè","happy","feliz"],
   '2':['错','cuò','wrong', "incorrecto"],
   '3':['阴','yīn','cloudy', 'nublado'],
   '4':['晴', 	'qíng',	'fine', 'bueno'],
   '5':['便宜',	'piányi',	'cheap', 'barato'],
   '6':['贵',	'guì',	'expensive', 'caro'],
   '7':['新',	'xīn',	'new', 'nuevo'], 
   '8':['长',	'cháng',	'long', 'largo'],
   '9':['累',	'lèi',	'tired', 'cansado'],
   '10':['好吃',	'hǎochī',	'delicioous','delicioso'],
   '11':['近',	'jìn',	'close', 'cerca'],

}


cor = []
incor = []
f = int(input("which line to start from: "))

def func(b):
    #the beginning of the loop     
    while b <= len(a):
        e = input(a[str(b)][0]) 
        if e == a[str(b)][3]: # an if statement inside the loop
            cor.append(a[str(b)][0])
            print('correct, pinyin is: ',a[str(b)][0], a[str(b)][1])
            return func(b+1)
        else:
            incor.append(a[str(b)][0])
            print('incorrect, try again!')
            return func(b)        
    print(f'you were right {len(cor)} times {cor}, you were wrong {len(incor)} times {incor}')
    d = input("Go again?: y(yes) or n(no), or the line you want to start from")
    if d == 'y':
        return(func(1))
    elif d == 'n': 
        print("Good bye, Have a nice day")
    else:    
        return func(int(d))
func(f)
