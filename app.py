from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

# 1. python3 -m venv myenv , 2. source myenv/bin/activate , 3. pip install flask , 4. flask --app app run