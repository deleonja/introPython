# se copia el codigo

print('------------------') # table heading
F = 0 # start value for C
dF = 10 # increment of C in loop
while F <= 100: # loop heading with condition
    C = round(((5 / 9)*(F - 32)),3) # 1st statement inside loop
    print(F, C) # 2nd statement inside loop
    F = F + dF # 3rd statement inside loop
print('------------------') # end of table line (after loop)