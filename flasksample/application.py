from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/polite_theme')
def polite():
	return render_template('polite.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
