from warnings import filterwarnings
filterwarnings('ignore')
import gensim
from utils import extract_text_from_url, preprocess_string
import nltk; 
import re
import spacy
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk import FreqDist
import string

# import numpy for matrix operation
import numpy as np

# Importing Gensim
import gensim
from gensim import corpora

from utils import extract_text_from_url
import json
import pandas as pd
from collections import Counter
import nltk

lemma = WordNetLemmatizer() 
porter = PorterStemmer()
stop = set(stopwords.words('english'))

stopwords_json = {"en":["a","a's","able","about","above","according","accordingly","across","actually","after","afterwards","again","against","ain't","all","allow","allows","almost","alone","along","already","also","although","always","am","among","amongst","an","and","another","any","anybody","anyhow","anyone","anything","anyway","anyways","anywhere","apart","appear","appreciate","appropriate","are","aren't","around","as","aside","ask","asking","associated","at","available","away","awfully","b","be","became","because","become","becomes","becoming","been","before","beforehand","behind","being","believe","below","beside","besides","best","better","between","beyond","both","brief","but","by","c","c'mon","c's","came","can","can't","cannot","cant","cause","causes","certain","certainly","changes","clearly","co","com","come","comes","concerning","consequently","consider","considering","contain","containing","contains","corresponding","could","couldn't","course","currently","d","definitely","described","despite","did","didn't","different","do","does","doesn't","doing","don't","done","down","downwards","during","e","each","edu","eg","eight","either","else","elsewhere","enough","entirely","especially","et","etc","even","ever","every","everybody","everyone","everything","everywhere","ex","exactly","example","except","f","far","few","fifth","first","five","followed","following","follows","for","former","formerly","forth","four","from","further","furthermore","g","get","gets","getting","given","gives","go","goes","going","gone","got","gotten","greetings","h","had","hadn't","happens","hardly","has","hasn't","have","haven't","having","he","he's","hello","help","hence","her","here","here's","hereafter","hereby","herein","hereupon","hers","herself","hi","him","himself","his","hither","hopefully","how","howbeit","however","i","i'd","i'll","i'm","i've","ie","if","ignored","immediate","in","inasmuch","inc","indeed","indicate","indicated","indicates","inner","insofar","instead","into","inward","is","isn't","it","it'd","it'll","it's","its","itself","j","just","k","keep","keeps","kept","know","known","knows","l","last","lately","later","latter","latterly","least","less","lest","let","let's","like","liked","likely","little","look","looking","looks","ltd","m","mainly","many","may","maybe","me","mean","meanwhile","merely","might","more","moreover","most","mostly","much","must","my","myself","n","name","namely","nd","near","nearly","necessary","need","needs","neither","never","nevertheless","new","next","nine","no","nobody","non","none","noone","nor","normally","not","nothing","novel","now","nowhere","o","obviously","of","off","often","oh","ok","okay","old","on","once","one","ones","only","onto","or","other","others","otherwise","ought","our","ours","ourselves","out","outside","over","overall","own","p","particular","particularly","per","perhaps","placed","please","plus","possible","presumably","probably","provides","q","que","quite","qv","r","rather","rd","re","really","reasonably","regarding","regardless","regards","relatively","respectively","right","s","said","same","saw","say","saying","says","second","secondly","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sensible","sent","serious","seriously","seven","several","shall","she","should","shouldn't","since","six","so","some","somebody","somehow","someone","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specified","specify","specifying","still","sub","such","sup","sure","t","t's","take","taken","tell","tends","th","than","thank","thanks","thanx","that","that's","thats","the","their","theirs","them","themselves","then","thence","there","there's","thereafter","thereby","therefore","therein","theres","thereupon","these","they","they'd","they'll","they're","they've","think","third","this","thorough","thoroughly","those","though","three","through","throughout","thru","thus","to","together","too","took","toward","towards","tried","tries","truly","try","trying","twice","two","u","un","under","unfortunately","unless","unlikely","until","unto","up","upon","us","use","used","useful","uses","using","usually","uucp","v","value","various","very","via","viz","vs","w","want","wants","was","wasn't","way","we","we'd","we'll","we're","we've","welcome","well","went","were","weren't","what","what's","whatever","when","whence","whenever","where","where's","whereafter","whereas","whereby","wherein","whereupon","wherever","whether","which","while","whither","who","who's","whoever","whole","whom","whose","why","will","willing","wish","with","within","without","won't","wonder","would","wouldn't","x","y","yes","yet","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves","z","zero"]}
stop = stop.union(set(stopwords_json['en']))

exclude = set(string.punctuation)

def clean(doc):
    
    # convert text into lower case + split into words
    pattern = r'[^a-zA-Z0-9\s]'
    stop_free = " ".join([re.sub(pattern, '', i) for i in doc.lower().split() if i not in stop])
    
    # remove any stop words present
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    
    # remove punctuations + normalize the text
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())  

    #stemming
    stemmed = " ".join(porter.stem(word) for word in normalized.split())

    return stemmed

def categorize_website(url):

    # Extract text content from the given URL
    content = extract_text_from_url(url)

    # Preprocess the text by applying some filters and tokenizing it
    #tokens = preprocess_string(content)
    model =  gensim.models.LdaModel.load('./model/lda_model_20.model')

    dictionary = gensim.corpora.Dictionary.load_from_text("./model/dict_20.txt")

    test_corpus = [content]
    test_clean_corpus = [clean(doc).split() for doc in test_corpus]  
    doc_term_matrix_20 = [dictionary.doc2bow(i) for i in test_clean_corpus]
    count = 0
    for i in model[doc_term_matrix_20]:
        count += 1

    topic_mapping = {}
    mapping = [['T1'],['T2', 'T1', 'T3'],['T2', 'T1'],['T2','T3'],['T3'],['T1', 'T3'],['T3'],
        ['T1', 'T3'],['T1', 'T3'],['T3'],['T1','T3'],['T1', 'T3'],['T2', 'T3'],['T3'],
        ['T2'],['T2', 'T1'],['T1'],['T1', 'T2', 'T3'],['T1', 'T2'],['T2', 'T3']
    ]
    for index, topics in enumerate(mapping):
        topic_mapping[index] = topics

    results = []
    topic_label = ''
    for i in model[doc_term_matrix_20]:
        results.append(i)
    for result in results:
        sorted_result = sorted(result, key=lambda x: x[1], reverse=True)
        top_5_probabilities = sorted_result[:5]
        mapped_topics = []
        for topic_index, probability in top_5_probabilities:
            # print(f"Topic index: {topic_index}, Probability: {probability}")
            mapped_topics.extend(topic_mapping.get(topic_index))
        topic_counts = Counter(mapped_topics)
        topic_label = topic_counts.most_common(1)[0][0]

    dict_topics = {"T1":"Business & Politics", "T2":"Entertainment & lifestyle",
                    "T3": "Technology & Science & Education & Literature"}
    

    return dict_topics[topic_label]

def sentiment_analysis(url):
    sent_data = extract_text_from_url(url)
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(sent_data)
    if(scores['compound']<0):
        return "Negative"
    else:
        return "Positive"