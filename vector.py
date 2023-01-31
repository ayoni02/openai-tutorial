import openai 
import numpy as np
from pprint import pprint as ppt

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()
    
def gpt3_embedding(content, engine='text-similarity-ada-001'):
    content = content.encode(encoding='ASCII', errors='ignore').decode()
    responce = openai.Embedding.create(input=content, engine=engine)
    vector = responce['data'][0]['embedding'] #this is a normal list
    return vector

def similarity(v1, v2): #return dot product of two vectors
    return np.dot(v1, v2)

openai.api_key = open_file('openaikey.txt')

def match_class(vector, categories):
    results = list()
    for _ in classes:
        score = similarity(vector, _['vector'])
        info = {'category': _['category'], 'score': score}
        results.append(info)
    return results

if __name__ == '__main__':
    categories = ['plant', 'reptile', 'mammal','bird', 'fish']
    classes = list()
    for _ in categories:
        vector = gpt3_embedding(_)
        info = {'category': _, 'vector': vector}
        classes.append(info)
    # print(classes)
    # exit(0)
    while True:
        a = input('Enter a lifeform here: ')
        vector = gpt3_embedding(a)
        # print('Vector:', vector)
        result = match_class(vector, categories)
        ppt(result)