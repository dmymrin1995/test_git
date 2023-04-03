from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def home_name(name):
    return 'Hello ' + name + ' nice to meet you'

@app.route('/')
def home():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=False)