
""" => Notes =============================================================================================

Date: 23/01/2024
Information:
    Attempt at a python based builder for a static site
    Aims to convert all .md files in ./markdown into .html files in ./html
    
Status: Testing
Quality: Unknown
Version: N/A
Fork Reason: N/A

/project
├── index.html
├── styles.css
├── script.js
├── builder.py
├── data.json
└── markdown
    ├── A.md
    ├── B.md

=> =================================================================================================== """

import os, mistune

def update_directory(_file = None):
    """Set the current directory to be the folder the of the __file__ provided"""
    if _file is None:
        raise FileNotFoundError("You must pass the current module's __file__ built-in")
    file_path = os.path.abspath(_file)
    current_directory = os.path.dirname(file_path)
    os.chdir(current_directory)
    print(f'Current working directory set to: {current_directory}')

update_directory(__file__)

os.system('cls')

print('\n-----------------------------------------------------------\n')

markdown_folder: str = "./markdown"
html_folder: str = "./html"

markdown_filepaths: list[str] = os.listdir(markdown_folder)
print(f"{markdown_filepaths = }")

# html_filepaths: list[str] = os.listdir(html_folder)
# print(f"{html_filepaths = }")

# ~ ======================================================================================================
# ~ Functions
# ~ ======================================================================================================
    
def remove_front_matter(text: str) -> str:
    """Remove front matter between '---' from a markdown string"""
    sections: list[str] = text.split('---')
    if len(sections) == 1:
        print('No front matter found')
        return sections[0]
    elif len(sections) == 3:
        print("Front matter removed")
        return sections[2]
    else:
        raise UserWarning("There is an unclosed '---' in the markdown file")

def convert(filepath: str) -> None:
    """Create a copy of a Markdown file converted to HTML"""

    # < Read the markdown file and create a temporary markdown string
    with open(filepath, 'r') as f:
        temporary_markdown: str = f.read()

    # < Remove front matter from the markdown
    temporary_markdown: str = remove_front_matter(temporary_markdown)

    # < Convert the temporary markdown string to a temporary HTML string
    temporary_html: str = mistune.html(temporary_markdown)

    # < Replace all instances of HTML &quot with instances of regular double quotes ( " ) for readability
    temporary_html = temporary_html.replace('&quot;', '"')

    # < Write the temporary HTML string to an .html file with the same name
    filepath: str = filepath.replace(".md", ".html")
    filepath: str = filepath.replace("markdown", "html")
    with open(filepath, 'w') as f:
        f.write(temporary_html)

for filepath in markdown_filepaths:
    filepath: str = './markdown/' + filepath
    print(f"\n---------------------------------\nConverting {filepath}")
    convert(filepath)
    print(f"Conversion success")

# ~ ======================================================================================================
# ~ Injection
# ~ ======================================================================================================
    
def inject_html_into_index(html_folder, index_file):
    
    # Read the content of index.html
    with open(index_file, 'r') as index_file_content:
        index_content = index_file_content.read()

    # Iterate over HTML files in the html_folder
    for html_file in os.listdir(html_folder):
        if html_file.endswith(".html"):
            html_path = os.path.join(html_folder, html_file)

            # Read the content of each HTML file
            with open(html_path, 'r') as html_file_content:
                html_content = html_file_content.read()

            # Inject the HTML content into the index.html
            injection_tag = f"<!-- {html_file} Injection Point -->"
            index_content = index_content.replace(injection_tag, html_content)

    # Write the modified content back to index.html
    with open(index_file, 'w') as updated_index:
        updated_index.write(index_content)

# Example usage
html_folder = "./html_files"
index_file = "index.html"
inject_html_into_index(html_folder, index_file)