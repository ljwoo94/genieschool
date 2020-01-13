from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def start():
    return render_template("start.html")

@app.route('/greet')
def greeting():
	return render_template('greet.html')

@app.route('/select')
def selection():
	return render_template('select.html')

@app.route('/polite_theme')
def polite():
	return render_template('polite.html')
@app.route('/polite_stream')
def politeStream():
	return render_template('polite_stream.html');

@app.route('/career_theme')
def career():
	return render_template('career.html')

@app.route('/career_stream')
def careerStream():
	return render_template('career_stream.html')

@app.route('/security_theme')
def security():
	return render_template('security.html')
@app.route('/security_stream')
def securityStream():
	return render_template('security_stream.html')

#값을 받아와서 여기서 OK로 갈지, No로 갈지 판단.
@app.route('/result')
def result():
	return render_template('result_ok.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
