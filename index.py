from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=["GET"])
def index():
    return "Hello, world!!",200

@app.route('/static')
def static_method():
    return render_template('static.html')

if __name__ == '__main__':
    app.run(port=5005)
