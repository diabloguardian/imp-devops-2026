
from datetime import datetime
from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    current_datetime = datetime.now()
    formated_datetime = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
    return f'<h1>Hello Dennys!</h1><br><h2>Time is: {formated_datetime}</h2>'

if __name__ == '__main__':
    # Run the app server
    app.run(host='0.0.0.0', port=5000, debug=True)
