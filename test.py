print('starting app')
model = SentenceTransformer('./data')
print('model loaded')

sentence = "winter"
embeddings = model.encode(sentence)

d = {}
d['title'] = sentence
d['embedding'] = embeddings.tolist()

import json
print(json.dumps(d, ensure_ascii=False))