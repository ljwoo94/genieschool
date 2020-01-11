from flask import Flask, request, render_template

application = Flask(__name__)

@application.route("/")
def index():
    return render_template("index.html")

@application.route('/polite_theme')
def polite():
	return render_template('polite.html')

if __name__ == "__main__":
    application.run(host='0.0.0.0')
