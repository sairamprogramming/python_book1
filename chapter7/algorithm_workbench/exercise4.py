# Program to total a list.
import random

def main():
    lt = []
    
    for i in range(10):
        lt.append(random.randint(1, 10))

    total = 0.0

    for number in lt:
        total += number

    print(lt)
    print(total)

main()
