# Program to check if item is in list.

def main():
    no_ruby = ['sai', 'ram', 'girish']
    with_ruby = ['sai', 'ram', 'ruby', 'girish']

    # Checking if 'ruby' is present in the list.
    if 'ruby' in no_ruby:
        print('ruby in no_ruby list')
    else:
        print('ruby not in no_ruby list')

    if 'ruby' in with_ruby:
        print('ruby in with_ruby list.')
    else:
        print('ruby not in with_ruby list.')
    
main()