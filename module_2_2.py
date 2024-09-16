first_=int(input("Число №1: "))
second_=int(input('Число №2: '))
third_=int(input('Число №3: '))
if first_==second_==third_:
    print(3)
elif first_==second_ or second_==third_ or first_==third_:
    print(2)
elif first_ != second_ != third_:
    print(0)