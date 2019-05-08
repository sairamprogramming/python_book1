import pickle

def main():
    dct = dict()

    output_file = open('mydata.dat', 'wb')
    pickle.dump(dct, output_file)

    output_file.close()

main()    
