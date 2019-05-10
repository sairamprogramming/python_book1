def main():
    word = 'test'
    show_me(word)

def show_me(word):
    print(word)
    new_word = word[1:]
    if len(new_word) > 0:
        show_me(new_word)
main()