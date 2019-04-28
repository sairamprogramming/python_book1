# Program to sort a list in descending order.
import random

def main():
    lt = []

    for i in range(100):
        lt.append(random.randint(1,100))

    print(lt)
    lt.sort()
    lt.reverse()
    print(lt)

main()
