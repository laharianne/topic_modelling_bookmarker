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

### Backend
- **Flask Application**: Serves as the backend framework to handle requests from the Chrome extension, processing data, and returning results.

## Setup and Installation
1. **Clone the repository**:
git clone https://github.com/yourgithubusername/topic-modelling-bookmarker.git
2. **Navigate to the directory**:
cd topic-modelling-bookmarker
3. **Install dependencies**
4. **Run the application**:
python app.py

## Usage
After uploading the extension to chrome, users can click the extension icon while browsing a webpage to see topic suggestions and sentiment analysis.

## Developers
- **Lahari Anne** - [lanne2@illinois.edu](mailto:lanne2@illinois.edu)
- **Sanjay Raj Aerra** - [saerra2@illinois.edu](mailto:saerra2@illinois.edu)
- **Sasi Pavan Surapaneni** - [ss257@illinois.edu](mailto:ss257@illinois.edu)


