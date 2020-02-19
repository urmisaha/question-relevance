import sys, os, re
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from nltk.corpus import stopwords


def pre_process(text):    
    # lowercase
    text=text.lower()
    
    #remove tags
    text=re.sub("<!--?.*?-->","",text)
    
    # remove special characters and digits
    text=re.sub("(\\d|\\W)+"," ",text)
    
    return text
 
 
#load a set of stop words
stopwords = stopwords.words('english')

# read srt/text files
filenames = []
docs = []
for file in os.listdir("files"):
    filenames.append(file.split(".")[0].replace('-', " "))
    with open("files/"+file, "r") as f:
        doc = ' '.join([str(line) for line in f.readlines()]) 
        docs.append(doc) 
df_idf = pd.DataFrame()
df_idf['title'] = filenames
print(df_idf['title'])
df_idf['body'] = docs
df_idf['text'] = df_idf['title'] + df_idf['body']
df_idf['text'] = df_idf['text'].apply(lambda x:pre_process(x))

#get the text column 
docs=df_idf['text'].tolist()

#create a vocabulary of words, ignore words that appear in 85% of documents, 
#eliminate stop words
cv=CountVectorizer(max_df=0.85,stop_words=stopwords)
word_count_vector=cv.fit_transform(docs)

print(list(cv.vocabulary_.keys())[:50])


# ##################################################################################


tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
tfidf_transformer.fit(word_count_vector)

# read test docs into a dataframe and concatenate title and body
# df_test=pd.read_json("data/stackoverflow-test.json",lines=True)
# df_test['text'] = df_test['title'] + df_test['body']
# df_test['text'] =df_test['text'].apply(lambda x:pre_process(x))

df_test = df_idf

def sort_coo(coo_matrix):
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)
 
def extract_topn_from_vector(feature_names, sorted_items, topn):
    """get the feature names and tf-idf score of top n items"""
    
    #use only topn items from vector
    sorted_items = sorted_items[:topn]
 
    score_vals = []
    feature_vals = []
    
    # word index and corresponding tf-idf score
    for idx, score in sorted_items:
        
        #keep track of feature name and its corresponding score
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])
 
    #create a tuples of feature,score
    #results = zip(feature_vals,score_vals)
    results= {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]]=score_vals[idx]
    
    return results

# get test docs into a list
docs_test=df_test['text'].tolist()

# you only needs to do this once, this is a mapping of index to 
feature_names=cv.get_feature_names()
 
# extract keywords
for doc in docs_test:

    #generate tf-idf for the given document
    tf_idf_vector=tfidf_transformer.transform(cv.transform([doc]))
    
    #sort the tf-idf vectors by descending order of scores
    sorted_items=sort_coo(tf_idf_vector.tocoo())
    
    #extract only the top n; n here is 10
    keywords=extract_topn_from_vector(feature_names,sorted_items,20)
    
    # now print the results
    # print("\n=====Doc=====")
    # print(doc)
    print("\n===Keywords===")
    for k in keywords:
        print(k,keywords[k])