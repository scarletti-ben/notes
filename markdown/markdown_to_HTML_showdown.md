---
tags: [
    showdown, markdown to html, conversion, converter, npm, cdn, jsdelivr, import, imports, importing, html, javascript, content delivery network, node package manager
]
---

# Converting Markdown Text to HTML Using Showdown and Javascript

## Information About Importing Javascript via CDN / NPM
There are multiple ways to import a script in HTML / Javascript, but a simple way is to import it via a content delivery network (CDN) such as **jsDelivr**. The search function for **jsDelivr** can be found [here](https://www.jsdelivr.com/). In simple terms **jsDelivr** pulls packages from the NPM (Node Package Manager) registry, it automatically handles versioning and caching. When you reference a specific version of a package, jsDelivr can serve that version with appropriate caching headers, ensuring that users receive the correct and cached version of the asset.

The example below imports `showdown.min.js` before `script.js` so that `script.js` can access **Showdown**.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Notes</title>
  <script src="https://cdn.jsdelivr.net/npm/showdown@2.1.0/dist/showdown.min.js"></script>
  <script src="script.js"></script>
  <link rel="stylesheet" href="styles.css">
</head>
```

## Using Showdown in Javascript

The core of **Showdown** is using `converter = new Showdown.converter()` to create a converter object and using `html = converter.makeHtml(text);` to convert markdown strings using the converter object, as with the example below.

```javascript
// Store test markdown string as variable
var text = "Markdown **rocks**";

// Store showdown converter object as variable
var converter = new Showdown.converter();

// Convert markdown to html and store html content as variable
var html = converter.makeHtml(text);
```