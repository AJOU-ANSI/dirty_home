from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home_shake():
    return render_template("info.html")

@app.route('/apc')
def home_apc():
    return render_template("main.html")

@app.route('/registration')
def registration():
	return render_template("registration.html");

if __name__ == '__main__':
    app.run(debug=True)
