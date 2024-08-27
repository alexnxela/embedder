from sentence_transformers import SentenceTransformer
model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v2')
model.save('./data/')

print('model saved to /app/data')

#sentence = "winter"
#embeddings = model.encode(sentence)

#d = {}
#d['title'] = sentence
#d['embedding'] = embeddings.tolist()

#import json
#print(json.dumps(d, ensure_ascii=False))