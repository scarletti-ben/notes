---
tags: [
  GitHub, GitHub files, GitHub file access, GitHub API, creating HTML elements, HTML links, HTML lists
]
---

# Accessing GitHub Files Using GitHub API, Including RAW Files

```javascript
// ~ Constants for generating the URLs
const username = 'scarletti-ben';
const repo = 'notes';
const folderPath = 'markdown';
const branch = 'main';

const apiUrl = `https://api.github.com/repos/${username}/${repo}/contents/${folderPath}`; // < Construct GitHub API endpoint

const rawUrl = `https://raw.githubusercontent.com/${username}/${repo}/${branch}/${folderPath}`; // < Construct raw URL

// ~ Fetch the contents of the folder using GitHub API
fetch(apiUrl)

    .then(response => response.json()) // < Convert successful promise response to JSON

    // ~ Assign the parsed JSON to the variable 'data' and then process
    .then(data => {
    
    const markdownFiles = data.filter(item => item.name.endsWith('.md')); // < Filter out only the names of markdown files

    const htmlList = document.createElement('ul'); // < Create empty unordered list element for html
    document.body.appendChild(htmlList); // < Add the unordered list to the html body

    // ~ Iterate through the markdown files and create list items
    markdownFiles.forEach(file => {

        const list = document.createElement('li'); // < Create an HTML list element
        const div = document.createElement('div'); // < Create an HTML div element
        const fileLink = document.createElement('a'); // < Create an HTML link element for the regular file
        const rawLink = document.createElement('a'); // < Create an HTML link element for the raw file
        const spacer = document.createTextNode('\u00A0\u00A0\u00A0\u00A0= >\u00A0\u00A0\u00A0\u00A0'); // < Add space between elements
        fileLink.href = file.html_url; // < Set the URL for the regular file
        fileLink.textContent = file.name; // < Set the text for the regular file
        rawLink.href = rawUrl + `/${file.name}`; // < Set the URL for the raw file
        rawLink.textContent = "[RAW VERSION]"; // < Set the text for the raw file
        div.appendChild(fileLink); // < Add the link element for the regular file to the div
        div.appendChild(spacer); // < Add the spacer element to the div
        div.appendChild(rawLink); // < Add the link element for the raw file to the div
        list.appendChild(div); // < Add the div element to the list element
        htmlList.appendChild(list); // < Add the list element to the list

    });

    })
    .catch(error => console.error('Error fetching data:', error)); // < Catch errors
```