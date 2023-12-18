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

    '''Convert Markdown headings, unordered lists, ordered lists, and paragraphs to HTML'''
    with open(sys.argv[1], 'r') as read_file:
        lines = read_file.readlines()
        with open(sys.argv[2], 'w') as write_file:
            in_list = False  # Flag to track if we are inside a list
            list_type = None  # 'ul' for unordered list, 'ol' for ordered list
            in_paragraph = False  # Flag to track if we are inside a paragraph

            for line in lines:
                line = line.rstrip('\r\n')

                if line.startswith('#'):
                    # Convert Markdown heading to HTML heading
                    count_hashes = min(line.count('#'), 6)
                    write_file.write("<h{0}>{1}</h{0}>\n".format(count_hashes, line.lstrip('#').strip()))
                elif line.startswith('- '):
                    # Handle unordered list items
                    if not in_list or list_type == 'ol':
                        in_list = True
                        list_type = 'ul'
                        # Close the previous paragraph if it was open
                        if in_paragraph:
                            write_file.write("</p>\n")
                            in_paragraph = False
                        write_file.write("<ul>\n")
                    # Write list item
                    if tag.string is not None:
                        s_tag = tag.string.strip()
                        write_file.write("<li>{}</li>\n".format(s_tag))
                elif line.startswith('* '):
                    # Handle ordered list items
                    if not in_list or list_type == 'ul':
                        in_list = True
                        list_type = 'ol'
                        # Close the previous paragraph if it was open
                        if in_paragraph:
                            write_file.write("</p>\n")
                            in_paragraph = False
                        write_file.write("<ol>\n")
                    # Write list item
                    if tag.string is not None:
                        s_tag = tag.string.strip()
                        write_file.write("<li>{}</li>\n".format(s_tag))
                elif line:
                    # Handle paragraphs
                    if not in_paragraph:
                        in_paragraph = True
                        # Close the previous list if it was open
                        if in_list:
                            if list_type == 'ul':
                                write_file.write("</ul>\n")
                            elif list_type == 'ol':
                                write_file.write("</ol>\n")
                            in_list = False
                        write_file.write("<p>\n")
                    # Write paragraph content
                    if tag.string is not None:
                        s_tag = tag.string.strip()
                        write_file.write("{}<br/>\n".format(s_tag))
                else:
                    # End the paragraph if it was open
                    if in_paragraph:
                        in_paragraph = False
                        write_file.write("</p>\n")
                    # End the list if it was open
                    if in_list:
                        in_list = False
                        if list_type == 'ul':
                            write_file.write("</ul>\n")
                        elif list_type == 'ol':
                            write_file.write("</ol>\n")

            # Close the paragraph if the last line was inside it
            if in_paragraph:
                write_file.write("</p>\n")
            # Close the list if the last line was inside it
            if in_list:
                if list_type == 'ul':
                    write_file.write("</ul>\n")
                elif list_type == 'ol':
                    write_file.write("</ol>\n")