
""" => Notes =============================================================================================

Date: 23/01/2024
Information:
    Script to convert a .md file to a .html file
Status: Success
Quality: 70
Version: A01
Fork Reason: N/A
* Issues:
    * Renders complex markdown incorrectly
    * Does not parse YAML front matter correctly

=> =================================================================================================== """

# ~ ======================================================================================================
# ~ Imports and Initialisation
# ~ ======================================================================================================

import markdown, os

def update_directory(_file = None):
    """Set the current directory to be the folder the of the __file__ provided"""
    if _file is None:
        raise FileNotFoundError("You must pass the current module's __file__ built-in")
    file_path = os.path.abspath(_file)
    current_directory = os.path.dirname(file_path)
    os.chdir(current_directory)
    print(f'Current working directory set to: {current_directory}')

# ~ ======================================================================================================
# ~ Main
# ~ ======================================================================================================

def main(filepath: str):
    """Create a copy of a Markdown file converted to HTML"""

    # < Read the markdown file and create a temporary markdown string
    with open(filepath, 'r') as f:
        temporary_markdown: str = f.read()

    # < Convert the temporary markdown string to a temporary HTML string
    temporary_html: str = markdown.markdown(temporary_markdown)

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
        