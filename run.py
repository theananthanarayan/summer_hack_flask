from flask import Flask, render_template, session, request
app = Flask(__name__)

app.secret_key = "Flask123"

@app.route('/')
def hello_world():
    return render_template('template1.html')

@app.route('/offerings')
def offerings():

    return render_template("offerings.html")

@app.route('/post')
def post():
    return render_template("post.html")


@app.route('/filters')
def filters():  
    return 'help'

@app.route('/community')
def community():
    return 'help'


if __name__ == '__main__':
    app.run(debug=True)
