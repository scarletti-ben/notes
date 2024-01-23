
""" => Notes =============================================================================================

Date: 23/01/2024
Information:
    Script to convert a .md file to a .html file
Status: Testing
Quality: N/A
Version: B01
Fork Reason: Aims to use markdown2 instead

=> =================================================================================================== """

# ~ ======================================================================================================
# ~ Imports and Initialisation
# ~ ======================================================================================================

import markdown2, os

def update_directory(_file = None):
    """Set the current directory to be the folder the of the __file__ provided"""
    if _file is None:
        raise FileNotFoundError("You must pass the current module's __file__ built-in")
    file_path = os.path.abspath(_file)
    current_directory = os.path.dirname(file_path)
    os.chdir(current_directory)
    print(f'Current working directory set to: {current_directory}')

# ~ ======================================================================================================
# ~ Functions
# ~ ======================================================================================================
    
def remove_front_matter(text: str) -> str:
    """Remove front matter between '---' from a markdown string"""
    sections: list[str] = text.split('---')
    assert len(sections) > 2, "There is an unclosed '---' in the markdown file"
    return sections[2]

def main(filepath: str) -> None:
    """Create a copy of a Markdown file converted to HTML"""

    # < Read the markdown file and create a temporary markdown string
    with open(filepath, 'r') as f:
        temporary_markdown: str = f.read()

    # < Remove front matter from the markdown
    temporary_markdown: str = remove_front_matter(temporary_markdown)

    # < Convert the temporary markdown string to a temporary HTML string
    temporary_html: str = markdown2.markdown(temporary_markdown)

    # < Write the temporary HTML string to an .html file with the same name
    filepath: str = filepath.replace(".md", ".html")
    with open(filepath, 'w') as f:
        f.write(temporary_html)

# ~ ======================================================================================================
# ~ Execution
# ~ ======================================================================================================

if __name__ == '__main__':

    filepath: str = 'test_markdown.md'

    os.system('cls')
    update_directory(__file__)
    assert filepath.endswith(".md"), "File extension must be '.md'"
    assert os.path.exists(filepath), f"{filepath} does not exist in this location"
    main(filepath)
    print(f"Markdown conversion for {filepath} run without error")
        