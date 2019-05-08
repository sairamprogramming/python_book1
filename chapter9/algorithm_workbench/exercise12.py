import pickle

def main():
    input_file = open('mydata.dat', 'rb')

    end_of_file = False

    while not end_of_file:
        try:
            dct = pickle.load(input_file)
            print(dct)
        except EOFError:
            end_of_file = True

    input_file.close()

main()    
