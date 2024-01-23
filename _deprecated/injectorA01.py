
import os
from bs4 import BeautifulSoup

# ~ Set current working directory
file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(file_path)
os.chdir(current_directory)

# ~ Read content from core.html
with open('core.html', 'r') as core_file:
    core_content = core_file.read()

# ~ Read content from injection.html
with open('injection.html', 'r') as injection_file:
    injection_content = injection_file.read()

# ~ Parse HTML using BeautifulSoup
soup_core = BeautifulSoup(core_content, 'html.parser')
soup_injection = BeautifulSoup(injection_content, 'html.parser')

# ~ Find the body tag in the core HTML
body_tag = soup_core.body

# ~ Append the contents of the injection HTML to the body tag
body_tag.extend(soup_injection.contents)

# ~ Write the merged content to index.html
with open('index.html', 'w') as index_file:
    # soup_core = soup_core.prettify() # * Be careful here as it may alter function of html
    index_file.write(str(soup_core))