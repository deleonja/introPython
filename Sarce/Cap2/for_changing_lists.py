# Se crea la lista con números del 0 al 9
numbers = [0,1,2,3,4,5,6,7,8,9]                      
print(numbers)

# se corrige el codigo
for n in numbers:
    i = int(len(numbers)/2)
    del numbers[i]
    print('n=%d, del %d' % (n,i), numbers)