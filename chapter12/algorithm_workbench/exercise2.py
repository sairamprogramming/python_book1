def main():
    num = 10
    halver(num)
def halver(number):
    print(number)
    half = number / 2
    if half >= 1:
        halver(half)
main()