
---
tags: [
    
]
---

# Heading

- [Main Page](https://harvesthq.github.io/chosen/)
- [Other Options](https://harvesthq.github.io/chosen/options.html)


```html

<!-- "Chosen" placeholder text with placeholder text and multiple selects enabled -->
<select class="my_select_box" data-placeholder="Select Your Options" multiple>
    <!-- Option 1 without special attributes -->
    <option value="1">Option 1</option>
    <!-- Option 2 is initially selected -->
    <option value="2" selected>Option 2</option>
    <!-- Option 3 is disabled and cannot be selected -->
    <option value="3" disabled>Option 3</option>
</select>

```

```javascript
// Event handler for the 'change' event
$('.my_select_box').on('change', function(evt, params) {
    // 'do_something' function is called when a selection is made
    do_something(evt, params);
});

// Event handler for the 'chosen:ready' event
$('.my_select_box').on('chosen:ready', function(evt, chosen) {
    // 'chosen:ready' event is triggered after Chosen has been fully instantiated
    console.log('Chosen is ready:', chosen);
});

// Event handler for the 'chosen:maxselected' event
$('.my_select_box').on('chosen:maxselected', function(evt, chosen) {
    // 'chosen:maxselected' event is triggered if max_selected_options is set and that total is broken
    console.log('Max selected options reached:', chosen);
});

// Event handler for the 'chosen:showing_dropdown' event
$('.my_select_box').on('chosen:showing_dropdown', function(evt, chosen) {
    // 'chosen:showing_dropdown' event is triggered when Chosen’s dropdown is opened
    console.log('Dropdown is showing:', chosen);
});

// Event handler for the 'chosen:hiding_dropdown' event
$('.my_select_box').on('chosen:hiding_dropdown', function(evt, chosen) {
    // 'chosen:hiding_dropdown' event is triggered when Chosen’s dropdown is closed
    console.log('Dropdown is hiding:', chosen);
});

// Event handler for the 'chosen:no_results' event
$('.my_select_box').on('chosen:no_results', function(evt, chosen) {
    // 'chosen:no_results' event is triggered when a search returns no matching results
    console.log('No matching results found:', chosen);
});


```