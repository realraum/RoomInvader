from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

import sh

app = Flask(__name__)


@app.route("/")
def main():
	#flash('Hi')
	return render_template('main.html')

@app.route('/enqueue/youtube', methods=['POST'])
def enqueue():

	# this is experimental, replace with mpv.py or ipc something:
	param = "--no-video %s" % request.form['url']
	sh.mpv(param)

	return "OK: %s" % request.form['url']


if __name__ == "__main__":
	app.debug = True
	app.run()
