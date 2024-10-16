from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to your API!"})

@app.route('/test')
def test():
    return jsonify({"message": "This is a test endpoint."})

@app.route('/test_post', methods=['POST'])
def test_post():
    data = request.json  # Get JSON data from the request
    if data is None or 'content' not in data:
        return jsonify({"error": "Invalid JSON or missing 'content' key"}), 400  # Handle invalid JSON or missing key

    content = data['content']  # Extract the content variable
    return jsonify({"received": content, "message": "Data received successfully."})

if __name__ == '__main__':
    app.run(debug=True)
