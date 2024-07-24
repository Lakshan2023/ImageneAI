from flask import Flask
from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    print("Lakshan Cooray 123")
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/why')
def why():
    return render_template('why.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/service')
def sevice():
    return render_template('service.html')



if __name__ == '__main__':
    print("Hello")
    app.run()
