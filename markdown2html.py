#!/usr/bin/python3
'''Write a script markdown2html.py that takes an argument 2 strings:
   First argument is the name of the Markdown file
   Second argument is the output file name
'''


if __name__ == '__main__':
    import sys
    import os
    
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py <input_file> <output_file>',
              file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        sys.exit(1)