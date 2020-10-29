summ = 0
n = int(input())
b = int(input())
amount = 0
if b == 0:
    print(0) 
else:
    while b != 0:
        summ += b
        amount += 1
        b = int(input())
    print(summ/amount)

#я подпрыгнула на стуле когда это решила

