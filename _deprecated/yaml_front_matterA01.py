
# """ Collapsible Notes

# Search Terms:
#     YAML tags, markdown, parsing markdown, parsing YAML, string parsing, safe parsing, front matter, front-matter, frontmatter, markdown front-matter, markdown front matter, markdown frontmatter, YAML front matter, blog, blog post, blogging

# Information:
#     Markdown often has YAML front matter with information about a blog post that can be parsed

# """

""" => Notes =============================================================================================

Date: 23/01/2024
Information:
    First attempt at a python based builder for a static site
    Aims to convert all markdown files in ./markdown into HTML to be stored in data.json
    
Status: Testing
Quality: Unknown
Version: A01
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

# < ======================================================================================================
# < Imports and Initialisation
# < ======================================================================================================

import yaml
import os

os.system('cls')
print("\n\n\n--------------------------------------------------")

# < ======================================================================================================
# < Functions
# < ======================================================================================================

def get_front_matter(content: str) -> list[str]:
    """Get a list of strings for the front matter between --- separators in a markdown file"""
    sections: list[str] = content.split('---')
    valid: bool = len(sections) > 2 # ~ Check there is a section between two --- separators
    if valid:
        return sections
    else:
        return None
    
def extract_tags(content: str) -> list:
    """Extract YAML tags from front matter content"""
    try:
        data = yaml.safe_load(content)
        tags = data.get('tags', []) if isinstance(data, dict) else []
        return tags
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        return []
    
# > ======================================================================================================
# > String Content
# > ======================================================================================================

content: str = """

---
number: 5
tags: [1, 2, 3]
---

# Header 1
## Header 2

"""

print(f"{content}")

# > ======================================================================================================
# > Front Matter
# > ======================================================================================================

front_matter: list = get_front_matter(content)
print(f"Front Matter: {front_matter}")

# > ======================================================================================================
# > Output
# > ======================================================================================================

output: any = extract_tags(front_matter)
print(f"Input content was of type: {type(content)} and the output content is of type: {type(output)}")
print(f"\nInput content looked like:\n{content}\n\nand the output content looks like:\n{output}\n")