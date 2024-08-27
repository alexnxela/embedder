from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

print('starting app')
model = SentenceTransformer('./data')
print('model loaded')

@app.route('/embedding', methods=['POST'])
def process_text():
    try:
        sentence = request.json.get('sentence')

        if not sentence:
            return jsonify({'error': 'sentence is empty'})

        embeddings = model.encode(sentence)

        data = {}
        data['title'] = sentence
        data['embedding'] = embeddings.tolist()

        return jsonify({'data': data})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)