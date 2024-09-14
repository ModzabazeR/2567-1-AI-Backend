from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	return jsonify({'message': 'API is working!'})

@app.route('/books', methods=['GET'])
def get_books():
    books = [{'id': 1, 'title': 'Python Essentials', 'author': 'Jane Doe'}]
    return jsonify({'books': books})

if __name__ == '__main__':
    app.run(debug=True)