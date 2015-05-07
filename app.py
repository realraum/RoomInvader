from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

import subprocess

app = Flask(__name__)


@app.route("/")
def main():
	#flash('Hi')
	return render_template('main.html')

@app.route('/enqueue/youtube', methods=['POST'])
def enqueue():

	# this is experimental, replace with mpv.py or ipc something:
	#os.system("sudo -u realraum mpv --no-video  %s" % request.form['url'])
	#ret = subprocess.call(["sudo", "-u", "realraum", "mpv", "--no-video", request.form['url']])
	ret = subprocess.call(["mpv", "--no-video", request.form['url']])

	return "OK: %s (%d)" % (request.form['url'], ret)


if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')
