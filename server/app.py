# server/app.py
from flask import Flask # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from Phase 4!</h1><p>Your Flask server is running on port 5555.</p>"

@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is a separate route in our application.</p>"

if __name__ == '__main__':
    app.run(port=5555, debug=True)