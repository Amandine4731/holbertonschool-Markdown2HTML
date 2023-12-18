#!/usr/bin/python3
'''Write a script markdown2html.py that takes an argument 2 strings:
   First argument is the name of the Markdown file.
   Second argument is the output file name
'''


if __name__ == "__main__":
    import sys
    from os import path

    '''Check if the number of arguments is not equal to 3'''
    if len(sys.argv) != 3:
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        exit(1)

    '''Check if the Markdown file doesn’t exist'''
    if not path.exists(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        exit(1)

    '''Convert Markdown headings to HTML headings'''
    with open(sys.argv[1], 'r') as read_file:
        lines = read_file.readlines()
        with open(sys.argv[2], 'w') as write_file:
            for line in lines:
                line = line.rstrip('\r\n')
                if line.startswith('#'):
                    count_hashes = 0
                    while count_hashes < len(line) and line[count_hashes] == '#':
                        count_hashes += 1

                    # Ensure the count of '#' is between 1 and 6
                    count_hashes = min(count_hashes, 6)
                    
                    # Write the corresponding HTML heading tag
                    write_file.write("<h{0}>{1}</h{0}>\n".format(count_hashes, line.lstrip('#').strip()))
                else:
                    # Write the line as it is
                    write_file.write("{}\n".format(line))