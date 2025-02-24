from flask import Flask # importing the FLask class.

app = Flask(__name__) # An instance of the class

@app.route("/") # telling FLask what URL should trigger our function
def hello_world():
    return "<h1>Hello, World!</h1> <p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum lies.</p>"

# 1. python3 -m venv myenv , 2. source myenv/bin/activate , 3. pip install flask , 4. flask --app app run