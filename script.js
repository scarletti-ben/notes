
// Function to filter items by tag
function filterItems(tag) {
  // Select all elements with the class "injection"
  var items = document.querySelectorAll(".injection");

  // Iterate through each item
  items.forEach((item) => {
    // Extract tags from the item's dataset, which is a space-separated list
    const tags = item.dataset.tags.split(" ");

    // Check if the specified tag is present in the item's tags
    item.style.display = tags.includes(tag) ? "inline-block" : "none";
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
