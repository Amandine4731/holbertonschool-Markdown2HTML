#!/usr/bin/python3
'''Write a script markdown2html.py that takes an argument 2 strings:
   First argument is the name of the Markdown file.
   Second argument is the output file name
'''


def convert_markdown_to_html(input_file, output_file):
    if not os.path.exists(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    with open(input_file, 'r', encoding='utf-8') as md_file:
        markdown_content = md_file.read()

    html_content = markdown2.markdown(markdown_content)

    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py <input_file> <output_file>\n")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        convert_markdown_to_html(input_file, output_file)
        sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"Error: {e}\n")
        sys.exit(1)