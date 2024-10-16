from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to your API!"})

@app.route('/test')
def test():
    return jsonify({"message": "This is a test endpoint."})

if __name__ == '__main__':
    app.run(debug=True)
