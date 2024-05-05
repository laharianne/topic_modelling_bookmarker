# Import necessary libraries
import requests
from bs4 import BeautifulSoup
from gensim.parsing.preprocessing import preprocess_string

# Function to fetch and extract text content from a web page
def extract_text_from_url(url):
    # Fetch content from URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Define the HTML tags to extract
    tags_to_extract = ["p", "h1", "h2", "h3", "h4", "h5", "h6", "li", "span", "strong", "em", "a"]
    
    # Gather text from specified tags
    extracted_text = " ".join(element.get_text() for element in soup.find_all(tags_to_extract))
    
    # Return the consolidated text
    return extracted_text

# Function to clean and preprocess text
def preprocess_string(text):
    # Apply gensim's preprocess_string function without any custom filters
    return preprocess_string(text, filters=None)
