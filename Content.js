chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
  // Send the URL to the background script for further processing
  if (message.action === 'detect') {
    // Perform any necessary preprocessing on the URL before sending it to your Python code

    // Call your Python code or API endpoint to detect malicious URLs
    // Example: Use fetch to make an HTTP POST request to your API
    fetch('http://your-api-endpoint.com/detect', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ url: message.url })
    })
      .then(response => response.json())
      .then(result => {
        // Process the detection result here
        if (result.isMalicious) {
          alert('Malicious URL detected!');
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
  }
});
