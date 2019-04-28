# Personal Web Page Generator.

def main():
    # Opening the file.
    outfile = open('personal_webpare.txt', 'w')

    # Getting name and description from the user.
    name = input('Enter your name: ')
    description = input('Describe yourself: ')

    # Generate the web page and writing to file.
    web_page = generate_webpage(name, description)
    outfile.write(web_page)

    # Closing the file.
    outfile.close()
    print('Personal web page created.')

# This function genrates the web page and returns it.
def generate_webpage(name, description):
    page = '<html>\n'
    page += '<head>\n'
    page += '</head>\n'
    page += '<body>\n'
    page += '\t<center>\n'
    page += '\t\t<h1>'+name+'</h1>\n'
    page += '\t</center>\n'
    page += '\t<hr />\n'
    page += '\t\t' + description + '\n'
    page += '\t<he />\n'
    page += '</body>\n'
    page += '</html>\n'
    
    return page

# Caling the main function.
main()