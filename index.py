
def func(base, n) :
    if n < base :
        print(numberChar[n], end = ' ')
    else :
        func(base, n // base)
        print(numberChar[n % base], end = ' ')


numberChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
              'A', 'B', 'C', 'D', 'E', 'F']

num = 8

func(2, num)
print()
func(8, num)
print()
func(16, num)
