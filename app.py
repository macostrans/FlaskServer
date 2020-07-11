from flask import Flask

app = Flask(__name__)

@app.route('/')
def HelloWorld():
    return "My First Flask Hello World2"

@app.route('/test')
def ByeWorld():
    return "Bye Bye Cruel World2"

if __name__ == '__main__':
    app.run(port=5000, debug= True)