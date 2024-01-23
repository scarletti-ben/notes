
""" => Notes =============================================================================================

Date: 24/01/2024
Information:
    Attempt at a python based builder for a static site
    Aims to convert all .md files in ./markdown into .html files in ./html
    Aims to inject all .html file content into a container within index.html    
Status: Success
Quality: 85
Version: 1.0
Fork Reason: N/A

/notes
├── builder.py
├── core.html
├── data.json
├── index.html
├── README.md
├── script.js
├── styles.css
├── markdown
│   └── example.md
└── html
    └── example.html

=> =================================================================================================== """

import os, mistune, random
from bs4 import  BeautifulSoup
from datetime import datetime, timezone

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

# ~ ======================================================================================================
# ~ Functions
# ~ ======================================================================================================

def html_escape(text):
    """HTML escape characters"""
    escape_table = {
        "&": "&amp;",
        '"': "&quot;",
        "'": "&#39;",
        ">": "&gt;",
        "<": "&lt;",
    }
    return "".join(escape_table.get(c, c) for c in text)
    
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
    # temporary_html: str = temporary_html.replace('&quot;', '"')

    # < Date
    last_modified_time = os.path.getmtime(filepath)
    last_modified_datetime = datetime.utcfromtimestamp(last_modified_time)
    time_string = "data-date=\"" + str(last_modified_datetime) + "\""

    # < Tags
    tags = ["tag1", "tag2", "tag3"]
    k = random.randint(1, len(tags))
    tags = random.sample(tags, k)
    # tags = [html_escape(tag) for tag in tags]
    tag_string = "data-tags=\"" + " ".join(tags) + "\""
    print(tag_string)

    # < Encapsulate the HTML in an injection class div element
    temporary_html: str = f'<div class="injection" {time_string} {tag_string}>\n' + temporary_html + "</div>"

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

# ** ======================================================================================================
# ** Deprecated Injection - Inject Directly to Body of index.html
# ** ======================================================================================================

# # ~ Read content from core.html
# with open('core.html', 'r') as core_file:
#     core_content = core_file.read()

# html_filepaths: list[str] = os.listdir(html_folder)

# soup_core = BeautifulSoup(core_content, 'html.parser')

# def inject(filepath: str, core: BeautifulSoup):

#     # ~ Read content from injection.html
#     with open(filepath, 'r') as injection_file:
#         injection_content = injection_file.read()

#     soup_injection = BeautifulSoup(injection_content, 'html.parser')

#     # ~ Find the body tag in the core HTML
#     body_tag = core.body

#     # ~ Append the contents of the injection HTML to the body tag
#     body_tag.extend(soup_injection.contents)

# for filepath in html_filepaths:
#     filepath: str = './html/' + filepath
#     inject(filepath, soup_core)

# # ~ Write the merged content to index.html
# with open('index.html', 'w') as index_file:
#     index_file.write(str(soup_core))
    
# ~ ======================================================================================================
# ~ Injection - Injected to 'injection-container' div
# ~ ======================================================================================================

# Read content from core.html
with open('core.html', 'r') as core_file:
    core_content = core_file.read()

html_folder = './html'
html_filepaths = os.listdir(html_folder)

# Parse core HTML
soup_core = BeautifulSoup(core_content, 'html.parser')

# Create a new div element to hold all injections
container = soup_core.new_tag('div')
container['class'] = 'injection-container'

def inject(filepath: str, container):

    # Read content from injection.html
    with open(filepath, 'r') as injection_file:
        injection_content = injection_file.read()

    soup_injection = BeautifulSoup(injection_content, 'html.parser')

    # Append the contents of the injection HTML to the container div element
    container.extend(soup_injection.contents)
  
for filepath in html_filepaths:
    filepath = os.path.join(html_folder, filepath)
    inject(filepath, container)

body_tag = soup_core.body
body_tag.append(container)

# Write the merged content to index.html
with open('index.html', 'w') as index_file:
    # soup_core = soup_core.prettify()
    index_file.write(str(soup_core))
