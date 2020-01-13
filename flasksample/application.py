from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def start():
    return render_template("start.html")

@app.route('/greeting')
def greeting():
	return render_template('greet.html')

@app.route('/select')
def selection():
	return render_template('select.html')

@app.route('/polite_theme')
def polite():
	return render_template('polite.html')

@app.route('/career_theme')
def career():
	return render_template('career.html')

@app.route('/sec_theme')
def security():
	return render_template('security.html')

@app.route('/result')
def result():
	return render_template('result.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
