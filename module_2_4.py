numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes=[]
not_primes=[]
for number in numbers:
    #print(number)
    if number==1:
        continue
    for j in range(2, number // 2 + 1):
        #print(number,j)
        if number % j ==0:
            #print(f'{number} / {j} = {number%j}')
            not_primes.append(number)
            break
    else:
        primes.append(number)
print('Простые: ',primes)
print('Непростые: ', not_primes)