from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home_shake():
    return render_template("shake.html")

@app.route('/apc')
def home_apc():
    return render_template("apc.html")

@app.route('/results/2019')
def result():
	return render_template("result_2019.html")

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=8888, debug=True)
    # app.run(host='0.0.0.0', port='80')
