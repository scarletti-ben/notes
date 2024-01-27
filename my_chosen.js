
/* => Notes ===============================================================================================

Date: 26/01/2024
Information:
    Using Chosen https://harvesthq.github.io/chosen/, a jQuery plugin for user-friendly drop-down boxes
    Adds Chosen functionality to a given HTML selector element
    Adds an event listener for changes to the selector, with callback function
    Filters elements in the container div element based on the value from listener's callback function output
Status: Educational
Quality: N/A
Version: N/A
Fork Reason: N/A

=> ===================================================================================================== */

// ~ ======================================================================================================
// ~ Function: enableChosen
// ~ ======================================================================================================

function enableChosen(selectorID) {
    // > Function to enable Chosen for a specified element by ID [with general default values]

    $(`#${selectorID}`).chosen({
        allow_single_deselect: false, // Adds a UI element to deselect the first option
        disable_search: false, // Displays the search field
        disable_search_threshold: 0, // Hide search input on single selects if options <= threshold
        enable_split_word_search: true, // Search matches on any word within an option tag
        inherit_select_classes: false, // Adds original select's classes to Chosen's container div
        max_selected_options: Infinity, // Limits how many options the user can select
        no_results_text: "No results for ", // Text displayed when no matching results are found
        placeholder_text_multiple: "Select Some Options", // Placeholder for multiple select when no options selected
        placeholder_text_single: "Select an Option", // Placeholder for single select when no options selected
        search_contains: false, // Search matches starting at the beginning of a word
        group_search: true, // Search includes group labels as well as options
        single_backstroke_delete: true, // Pressing delete/backspace on multiple selects removes selected choice
        width: "95%", // Width of the Chosen select box
        display_disabled_options: true, // Includes disabled options in search results
        display_selected_options: true, // Includes selected options in search results for multiple selects
        include_group_label_in_selected: false, // Shows both text and group (if any) of the selected option
        max_shown_results: Infinity, // Shows only the first (n) matching options in the results
        case_sensitive_search: false, // Chosen's search is case-insensitive
        hide_results_on_select: true, // Hides results after an option is selected (for multiple selects)
        rtl: false // Supports right-to-left text in select boxes
    });

    // ! Log Entry
    console.log(`Chosen enabled for ${selectorID}`)

};

// ~ ======================================================================================================
// ~ Function: addEventListener
// ~ ======================================================================================================

function addEventListener(selectorID, containerID, callback) {
    // > Event listener for the 'change' event on the selector element
    
    // ! Add event listener to the element with the specified ID
    $(`#${selectorID}`).on('change', function(evt, params) {

        // ! Pass "this" to the callback
        callback(containerID, $(this));

      });

    // ! Log Entry
    console.log(`Event listener added for ${selectorID} / ${containerID}`)

};

// ~ ======================================================================================================
// ~ Function: filterItems
// ~ ======================================================================================================

function filterItems(containerID, object) {
    // > Function to show/hide items in a container if their data-tags match items in the textArray

    // ! Log Entry
    console.log(`Filter items started inside ${containerID}`)

    // ! Get text array from the jQuery object via map method
    var textArray = object.find("option:selected").map(function() {
        return $(this).text();
    }).get();

    // ! Log Entry
    console.log(`Active filters: ${textArray}`)

    // ! Get Children of the HTML containerID Element
    var itemsToFilter = $(`#${containerID}`).children();

    // ! Loop through each item and check if it contains any of the tags
    itemsToFilter.each(function() {

        // ! Get HTML Element in the format: data-tags="one,two,three"
        var itemTags = $(this).data('tags').split(',');

        // ! Log Entry
        // console.log(`Item Tags: ${itemTags}`);

        // ! Check if any or all of the tags in textArray are present in the current item's tags
        var containsTag = textArray.some(function(tag) {
            return itemTags.includes(tag);
        });

        // ! Show or hide the item based on the tag matching
        if (containsTag) {
            $(this).show();
        } else {
            $(this).hide();
        }

    });

    // ! Log Entry
    console.log(`Filter items inside for ${containerID}`)
    
};

// ~ ======================================================================================================
// ~ Function: initialiseChosen
// ~ ======================================================================================================

function initialiseChosen(selectorID, containerID) {
    // > Initialise a given selectorID as a Chosen object

    enableChosen(selectorID);
    addEventListener(selectorID, containerID, filterItems);

};

// ! ======================================================================================================
// ! Exports
// ! ======================================================================================================

// export { initialiseChosen };
