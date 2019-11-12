import sys
import os
import pandas
import pymongo
# from scrape.py import *

query = sys.argv[1]

tags = set()

for file in os.listdir("extracted_questions"):
    df = pandas.read_csv("extracted_questions/"+file, header=None, names=['question_id', 'tag', 'link', 'tags', 'accepted_answer'])
    # print(df['tag'].values[1])
    tags.add(df['tag'].values[1])
    # print(tags)
    for tag in df['tags']:
        for t in tag.split(';'):
            tags.add(t)
    # print(tags)
        
rel_tags = set()

for word in query.split():
    if word in tags:
        rel_tags.add(word)

print(rel_tags)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.stackapi
collec_ques = db.questions

# fetch questions
for t in rel_tags:
    print("\nFetching questions for tag: " + t + "\n")
    items = collec_ques.find({"tags": t}).limit(5)

    for item in items:
        print(item['title'])