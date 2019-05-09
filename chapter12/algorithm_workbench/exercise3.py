# def queue(length):

#     while length > 0:
#         print('Please wait.')
#         length = length – 1
#     print('It is your turn.')

def queue(l):
    if l <= 0:
        print('It is your turn.')
    else:
        print('Please wait.')
        queue(l - 1)

queue(5)        