import json
import re

with open('review.json', encoding='utf-8') as f:
    review = json.load(f)
    
with open('keywords.json', encoding='utf-8') as f:
    keywords = json.load(f)
        
# source
# text
# created_at
# retweet_count
# favorite_count
# is_retweet
# id_str
data = []
for t in review:
    data.append(t['text'].lower())
    
for d in data:
    splitD = d.split(" ")
    dataIntersection = set(splitD) & set(keywords)
    print (dataIntersection)