from flask import Flask
import os

app = Flask(__name__)


@app.route('/<random_string>')
def return_backwards_string(random_string):
    return "".join(reversed(random_string))

@app.route('/get-project')
def get_project():
    return os.environ.get('PROJECT_NAME')

if (__name__ == "__main__"):
    app.run()