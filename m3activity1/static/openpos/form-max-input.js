function checkInputValue(input) {
  // Get the maximum allowed value from the 'max' attribute of the input
  var maxAllowed = parseInt(input.getAttribute("max"));

  // Get the current value of the input
  var currentValue = parseInt(input.value);

  // If the current value is greater than the maximum allowed
  if (currentValue > maxAllowed) {
    // Set the value of the input to the maximum allowed
    input.value = maxAllowed;
  }
  if (currentValue < 1) {
    input.value = 0;
  }
}
