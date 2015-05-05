from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)


@app.route("/")
def hello():
	#flash('Hi')
	return render_template('main.html')


if __name__ == "__main__":
	app.debug = True
	app.run()
	