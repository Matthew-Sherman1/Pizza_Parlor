from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

# base route = '/'
@app.route('/')
def landingPage():
    return ('Hello World')

@app.route('/Dojo!')
def Dojo():
    return ('Hello World')

@app.route('/say/flask')
def flask():
    return ('Hi Flask!')

@app.route('/say/michael')
def michael():
    return ('Hi Michael!')

@app.route('/say/john')
def john():
    return ('Hi John!')


@app.route('/repeat/<int:num>/<string:input>')
def repeat(num, input):
    print(num)
    print(input)
    return input * num
# @app.route('/success')
# def success():
#     return "success"

# @app.route('/dashboard')
# def dashboard():
#     friend = 'jane pancakes'
#     friends = 'Eric', 'Matt', 'craig'
#     return render_template('dashboard.html', friend1 = friend)

# @app.route('/hello/<string:banana>/<int:num>')
# def hello(banana,num):
#     return f"hello {banana * num}"


if __name__ == '__main__':
    app.run(debug=True)
