
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello Dennys Medina!</h1>"

if __name__ == '__main__':
    # Run the app server
    app.run(host='0.0.0.0', port=5000, debug=True)
