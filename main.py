from flask import Flask
from flask.templating import render_template

app= Flask(__name__)
app.secret_key = "SOME KEY"

@app.route('/', method=['GET'])
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()