// Function to filter items by tag
function filterItems(tag) {
  // Select all elements with the class "item"
  const items = document.querySelectorAll(".item");

  // Iterate through each item
  items.forEach((item) => {
    // Extract tags from the item's dataset which is a space separated list
    const tags = item.dataset.tags.split(" ");

    // Check if the specified tag is present in the item's tags
    if (tags.includes(tag)) {
      // If yes, display the item
      item.style.display = "inline-block";
    } else {
      // If not, hide the item
      item.style.display = "none";
    }
  });
}

// Function to show all items
function showAllItems() {
  // Select all elements with the class "item"
  const items = document.querySelectorAll(".item");

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

  // Select all elements with the class "item"
  const items = document.querySelectorAll(".item");

  // Iterate through each item
  items.forEach((item) => {
    // Extract date from the item's dataset and convert it to Date object
    const itemDate = new Date(item.dataset.date);

    // Check if the item's date is within the specified range
    const isWithinRange =
      (!startDate || itemDate >= new Date(startDate)) &&
      (!endDate || itemDate <= new Date(endDate));

    // Set the display style based on whether the item is within the range or not
    if (isWithinRange) {
      item.style.display = "inline-block";
    } else {
      item.style.display = "none";
    }
  });
}

// Function to show a tooltip with item information
function showTooltip(element) {
  // Generate tooltip text using item's tags and date from the dataset
  const tooltipText = `Tags: ${element.dataset.tags}, Date: ${element.dataset.date}`;
  
  // Set the tooltip text as the title attribute of the element
  element.title = tooltipText;
}

// Function to hide the tooltip
function hideTooltip(element) {
  // Remove the title attribute to hide the tooltip
  element.title = "";
}

// Function to convert Markdown to HTML
function convertMarkdownToHTML() {
  // Get the Markdown content
  var markdownContent = document.getElementById('markdownContent').innerText;

  // Create a Showdown converter instance
  var converter = new showdown.Converter();

  // Convert Markdown to HTML
  var htmlContent = converter.makeHtml(markdownContent);

  // Display the HTML content
  document.getElementById('htmlContent').innerHTML = htmlContent;
}

// Wait for the DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function () {
  // Call the function when the DOM is ready
  convertMarkdownToHTML();
});
