// Defining categories and their associated websites
const categories = {
    'technology': ['techcrunch.com', 'theverge.com'],
    'news': ['cnn.com', 'bbc.com'],
  };

  async function fetchWebContent(url) {
    try {

      // Send a GET request to the specified URL
      const response = await fetch(url);

      // Get the response body as text
      const text = await response.text();

      // Return the fetched text content
      return text;
    } catch (error) {
      // Log an error if something went wrong
      console.error('Failed to fetch content:', error);

      // Return an empty string
      return '';
    }
  }

async function getTopicLabel(url) {
    
    // API endpoint URL
    const api_url = 'http://127.0.0.1:5000/categorize';

    // Send a POST request to the API endpoint
    const response = await fetch(api_url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      
      // Send the URL in the request body as JSON data
      body: JSON.stringify({ url: url }),
    });
    
    // Parse the response body as JSON
    const data = await response.json();

    // Return the category field from the response data
    return data.category;
  }
  
  async function categorizeAndBookmark(tab) {

    // Get the topic label for the current tab's URL
    const category = await getTopicLabel(tab.url);
  
    // Set the folder title to the obtained category label
    const folderTitle = `${category}`;

    // Find or create a folder with the specified title
    let folder = await findOrCreateFolder(folderTitle);

    // Create a bookmark with the tab's title and URL inside the folder
    await createBookmark(tab.title, tab.url, folder.id);
  }
  
  async function findOrCreateFolder(title) {
    return new Promise(async (resolve) => {
      chrome.bookmarks.search({ title }, (results) => {
        const folder = results.find((bookmark) => bookmark.url === undefined && bookmark.title === title);
  
        if (folder) {
          // If folder with the specified title exists, resolve the promise with the folder object
          resolve(folder);
        } else {
          chrome.bookmarks.create({ title }, (newFolder) => {
            // If folder doesn't exist, create a new folder and resolve the promise with the new folder object
            resolve(newFolder);
          });
        }
      });
    });
  }
  
  
  async function createBookmark(title, url, parentId) {
    // Create a bookmark with the specified title, URL, and parent ID
    return await chrome.bookmarks.create({ title, url, parentId });
  }

  async function sentiment_analysis(url) {
    const response = await fetch('http://127.0.0.1:5000/sentiment', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: url }),
    });
    const data = await response.json();
    console.log(data);
    return data.sentiment;
}
function showNotification(sentiment) {
  chrome.notifications.create({
      type: 'basic',
      iconUrl: 'icon.png',
      title: 'Sentiment Analysis Result',
      message: 'The sentiment of the content is: ' + sentiment,
      priority: 2
  });
}
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'categorizeAndBookmark') {
        chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
            categorizeAndBookmark(tabs[0]);
        });
    }
    if (request.action === 'analyzeSentiment') {
      sentiment_analysis(request.url).then(sentiment => {
          sendResponse({sentiment: sentiment});
      }).catch(error => {
          sendResponse({sentiment: 'Error analyzing sentiment'});
          console.error('Sentiment analysis failed:', error);
      });
      return true;  // to indicate you wish to send a response asynchronously
  }
});