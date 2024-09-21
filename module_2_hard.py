n= int(input('Введите число от 3 до 20: '))
def get_password(number):
    password = ''
    for i in range(1, number):
        #print(i)
        for j in range(2, number):
            #print(i,j)
            if j <= i:
                continue
            if number % (i + j) == 0:
                password+= str(i) + str(j)
    return password
result = get_password(n)
print('Пароль: ', result)