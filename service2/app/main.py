from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World from Service 2!", 200  # Change to Service 2 for second service

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
