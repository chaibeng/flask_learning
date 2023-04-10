from flask import Flask, request,redirect,url_for,render_template
app = Flask (__name__)

@app.route('/',methods=["GET"])
def index():
    return "Hello, world!!"

@app.route('/dashboard')
def static_method():
    return render_template('html.html')

@app.route('/dashboard/<name>', methods=['GET'])
def dashboard(name):
    return render_template('dashboard.html', username=name)

@app.route('/error')
def error_devision_error():
    # try:
        55/0
    # except ZeroDivisionError as error:
    #     return "The error is " + str(error)
    # except:
    #     return "ddaijoubu"

@app.errorhandler(500)
def error_page(error):
    return render_template("error.html")


@app.route("/submit",methods = ["POST"])
def get_data():
    if request.data:
        data = request.get_json()  # parse JSON data from the request body
        return data
    
@app.route('/redirect', methods=['GET'])
def redirect_example():
    return redirect('https://www.google.com')

@app.route('/<name>/<password>')
def read_data(name,password):
    if (name == 'admin' and password == '123456'):
        return redirect (url_for('admin'))  
    
@app.route('/admin')
def admin():
    return "you have insert correct password."

if __name__ == '__main__':
    app.run(port=5005)