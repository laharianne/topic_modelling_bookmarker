# Topic Modelling Bookmarker Extension

## Overview
The Topic Modelling Bookmarker is a Google Chrome extension designed to enhance the efficiency of bookmarking web pages by providing automatic topic suggestions and sentiment analysis. It is especially useful for students, researchers, and professionals who frequently bookmark web pages for reference or research purposes.

## Features
- **Topic Suggestions**: Automatically scans the web page content to suggest relevant topics for efficient organization.
- **Sentiment Analysis**: Analyzes the tone of the web page, helping users understand the emotional context of their bookmarks.

## Technologies Used
- **Frontend**: JavaScript, HTML, CSS
- **Backend**: Python with Flask
- **NLP Processing**: Gensim for LDA, NLTK for preprocessing and sentiment analysis

## Implementation Details

### Topic Modeling
- **LDA (Latent Dirichlet Allocation)**: We utilize Gensim's LDA model to analyze the textual content of web pages. The model is trained on a diverse dataset to recognize a variety of topics.
- **Preprocessing**: Text data is cleaned and preprocessed using NLTK, involving steps like tokenization, stopword removal, and lemmatization to prepare data for the LDA model.

### Sentiment Analysis
- **VADER Sentiment Analyzer**: Employed for sentiment analysis, providing a compound score that helps ascertain the overall sentiment of the content (positive, negative, neutral).
- **Integration**: This analysis is performed in real-time as the user browses, with results displayed immediately to provide instant feedback on the content's sentiment.
- 
### Backend
- **Flask Application**: Serves as the backend framework to handle requests from the Chrome extension, processing data, and returning results.
## Flow Diagram
![flow_diagram](https://github.com/laharianne/topic_modelling_bookmarker/assets/143364981/14c3ea29-d63d-4345-9efc-8737f07c9e0d)

## Setup and Installation
1. **Clone the repository**:
git clone https://github.com/yourgithubusername/topic-modelling-bookmarker.git
2. **Navigate to the directory**:
cd topic-modelling-bookmarker

3. **Install dependencies** : 
* pip install flask flask-cors scikit-learn bs4 transformers requests
* pip install gensim torch
4. **Run the application**:
python app.py

Wait until you receive,  

 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with watchdog (windowsapi)
 * Debugger is active!
 * Debugger PIN: xxx-yyy-zzz

5. **Extension Set Up**
* Download and extract the zip file or clone the project to your local.
* /yourpath/topic_modelling_bookmarker/ is our root folder

* Go to chrome://extensions/ and turn on the developer mode in the top right corner of the page.
* Remove the generated __pycache__ folder from the project after running the "python app.py"
* Click on "Load unpacked" on the top left and select the /yourpath/topic_modelling_nookmarker/ folder.
* Open a new tab and you should now be able to see the Topic Modelling Bookmarker extension among your other browser extensions.

## Usage
After uploading the extension to chrome, users can click the extension icon while browsing a webpage to see topic suggestions and sentiment analysis.

## Developers
- **Lahari Anne** - [lanne2@illinois.edu](mailto:lanne2@illinois.edu)
- **Sanjay Raj Aerra** - [saerra2@illinois.edu](mailto:saerra2@illinois.edu)
- **Sasi Pavan Surapaneni** - [ss257@illinois.edu](mailto:ss257@illinois.edu)

## Resource Links
- **Video Presentation** - https://drive.google.com/file/d/1ay-p4yosUsFsk5UCWsPLhQ6kXbdPIA-y/view?usp=sharing
- **Slides Presentation** - https://docs.google.com/presentation/d/1zvj3T7741Ytub2UjWXFcNXhVfNRWmIh8nMOR46wf4yU/edit?usp=sharing
- **Report Link** - https://github.com/laharianne/topic_modelling_bookmarker/blob/main/CS%20510%20Final%20Project%20Report.pdf
      

