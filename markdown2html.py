#!/usr/bin/python3
'''Write a script markdown2html.py that takes an argument 2 strings:
   First argument is the name of the Markdown file.
   Second argument is the output file name
'''


if __name__ == '__main__':
    import sys
    import os
    if len(sys.argv) < 3:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('Missing {}'.format(sys.argv[1]), file=sys.stderr)
        sys.exit(1)

    sym_map = {
            '# ': ('<h1>', '</h1>\n'),
            '## ': ('<h2>', '</h2>\n'),
            '### ': ('<h3>', '</h3>\n'),
            '#### ': ('<h4>', '</h4>\n'),
            '##### ': ('<h5>', '</h5>\n'),
            '###### ': ('<h6>', '</h6>\n')
        }
    ul = []

    with open(sys.argv[1]) as rf:
        read_lines = rf.readlines()
        with open(sys.argv[2], 'a') as wf:
            for line in read_lines:
                if line.startswith('- '):
                    ul.append(line)

                if ul:
                    i = 0
                    while i < len(ul):
                        if i == 0:
                            html_line = ul[i].replace('- ', '<ul>\n<li>').replace(ul[i][-1], '</li>\n')
                        else:
                            html_line = ul[i].replace('- ', '<li>').replace('\n', '</li>\n')
                        if i == len(ul) - 1:
                            html_line = html_line.replace(html_line[-1], '\n</ul>\n')
                            wf.write(html_line)
                        else:
                            wf.write(html_line)
                        i = i + 1

                for k, v in sym_map.items():
                    if line.startswith(k):
                        html_line = line.replace(k, v[0]).replace('\n', v[1])
                        break
                wf.write(html_line)

    sys.exit(0)