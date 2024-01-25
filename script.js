
// Function to filter items by tag
function filterItems(tag) {

  console.log("Function called")

  // Select all elements with the class "injection"
  var items = document.querySelectorAll(".injection");

  // Iterate through each item
  items.forEach((item) => {
    // Extract tags from the item's dataset, which is a comma-separated list
    const tags = item.dataset.tags.split(",");
    console.log("Tags:", tags);

    // Check if the specified tag is present in the item's tags
    const isVisible = tags.includes(tag);
    console.log("Is Visible:", isVisible);

    // Update Chosen state based on visibility
    const chosen = item.nextElementSibling.chosen;
    const selectedIndex = chosen.results_data.findIndex(result => result.value === tag);

    if (isVisible && selectedIndex === -1) {
      // Add the tag to Chosen results
      chosen.results_data.push({
        value: tag,
        text: tag,
        selected: true
      });

      // Update Chosen display
      chosen.result_highlight = null;
      chosen.winnow_results();
    } else if (!isVisible && selectedIndex !== -1) {
      // Remove the tag from Chosen results
      chosen.results_data.splice(selectedIndex, 1);

      // Update Chosen display
      chosen.result_clear_highlight();
      chosen.winnow_results();
    }

    // Update item display
    item.style.display = isVisible ? "inline-block" : "none";
  });
}


// Function to show all items
function showAllItems() {
  // Select all elements with the class "injection"
  var items = document.querySelectorAll(".injection");

  // Iterate through each item and display it
  items.forEach((item) => {
    item.style.display = "inline-block";
  });

  // Reset Chosen state
  var chosen = document.querySelector(".chosen-select").chosen;
  chosen.results_data = [];
  chosen.result_clear_highlight();
  chosen.winnow_results();
}

// Function to filter items by date range
function filterByDate() {
  // Retrieve start and end dates from input fields
  const startDate = document.getElementById("startDate").value;
  const endDate = document.getElementById("endDate").value;

  // Select all elements with the class "injection"
  var items = document.querySelectorAll(".injection");

  // Iterate through each item
  items.forEach((item) => {
    // Extract date from the item's dataset and convert it to a Date object
    const itemDate = new Date(item.dataset.date);

    // Check if the item's date is within the specified range
    const isWithinRange =
      (!startDate || itemDate >= new Date(startDate)) &&
      (!endDate || itemDate <= new Date(endDate));

    // Set the display style based on whether the item is within the range or not
    item.style.display = isWithinRange ? "inline-block" : "none";
  });
}

// Function to filter items by search term
function filterBySearch() {
  // Retrieve search term from the search bar
  const searchTerm = document.getElementById("searchBar").value.toLowerCase();

  // Select all elements with the class "injection"
  var items = document.querySelectorAll(".injection");

  // Iterate through each item
  items.forEach((item) => {
    // Find the first H1 element within the item
    const h1Element = item.querySelector("h1");

    // Check if the H1 element exists and contains the search term
    const isMatch = h1Element && h1Element.textContent.toLowerCase().includes(searchTerm);

    // Set the display style based on whether the item matches the search term or not
    item.style.display = isMatch ? "inline-block" : "none";
  });
}

// Function to toggle outlines between solid green and none
function toggleOutlines() {

  // Select all elements
  const allElements = document.querySelectorAll('*');

  // Check the state by looking at the outline of the first element
  const currentState = allElements[0].style.outline;

  // If outlines are currently set, remove them (toggle off)
  if (currentState && currentState !== 'none') {
    allElements.forEach((element) => {
      element.style.outline = 'none';
    });
  } else {
    // If outlines are not set, add them with solid green (toggle on)
    allElements.forEach((element) => {
      element.style.outline = '1px solid green';
    });
  }
}

document.addEventListener('DOMContentLoaded', function () {
  // Assuming this is where you're adding an event listener to your tag selector
  document.getElementById('tagSelector').addEventListener('change', function (event) {
      const selectedTag = event.target.value;
      console.log("Selected tag:", selectedTag);

      // Call the filterItems function with the selected tag
      filterItems(selectedTag);
  });
});
