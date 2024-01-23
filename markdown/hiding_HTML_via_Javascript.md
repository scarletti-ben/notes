---
tags: [
  hiding, hidden, invisible, dynamic, html, js, javascript, css, styling
]
---

# Hiding HTML Elements Dynamically using Javascript and CSS

You can hide elements in HTML dynamically using Javascript to set CSS property `display` of the element to `"none"` as in ```item.style.display = "none"```

```javascript
function filterItems(tag) {

  // Select all elements with the class "item"
  const items = document.querySelectorAll(".item");

  // Iterate over all items
  items.forEach((item) => {

    // Extract tags from item's dataset, stored as a space delimited list
    const tags = item.dataset.tags.split(" ");

    // Check if the specified tag is present in the item's tags
    if (tags.includes(tag)) {
      item.style.display = "inline-block"; // If yes, display the item
    } else {
      item.style.display = "none"; // If not, hide the item
    }
  });
}
```
In the example above, items are only displayed if one of their tags matches the filtered tag in `filterItems(tag)`. In this way HTML elements can be hidden from a search bar or button