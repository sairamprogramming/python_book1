amount1 = int(input("Enter the value of amount1: "))
amount2 = int(input("Enter the value of amount2: "))

if amount1 > 10 and amount2 < 100:
    print(100)
else:
    if amount1 > amount2:
        print(amount1)
    else:
        print(amount2)
