from flask import Flask, request
from dummy_submodule import greeting
app = Flask(__name__)

@app.route('/')
def hello_world():
    """Handles the root URL and returns 'Hello, World!'."""
    return greeting(request.args.get('name'))

if __name__ == '__main__':
    app.run(debug=True)

