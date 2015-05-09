from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, json, jsonify

from urlparse import urlparse, parse_qs

import urllib2
import subprocess

app = Flask(__name__)

nowplaying = []
queue = []


def getYouTubeID(videoURL):
	app.logger.debug('getting videoID: ' + videoURL)
	return parse_qs(urlparse(videoURL).query)['v'][0]


def getYouTubeTitle(videoId):
	app.logger.debug('getting title for videoId: ' + videoId)
	response = urllib2.urlopen("http://youtube.com/get_video_info?video_id=" + str(videoId))

	query = urlparse("/?" + response.read()).query
	 
	return parse_qs(query)['title'][0]


def appendToQueue(record):
	if len(nowplaying) == 0:
		nowplaying.append(record)
	else:
		queue.append(record)


@app.route("/")
def main():
	#flash('Hi')
	return render_template('main.html')


@app.route('/queue', methods=['GET'])
def getQueue():
	return jsonify(queue=queue)


@app.route('/np', methods=['GET'])
def np():
	return jsonify(np=nowplaying)


@app.route('/enqueue/youtube', methods=['POST'])
def enqueue():

	app.logger.debug('/enqueue/youtube ...')

	# this is experimental, replace with mpv.py or ipc something:
	#os.system("sudo -u realraum mpv --no-video  %s" % request.form['url'])
	#ret = subprocess.call(["sudo", "-u", "realraum", "mpv", "--no-video", request.form['url']])
	
	# ret = subprocess.call(["mpv", "--no-video", request.form['url']])

	videoID = getYouTubeID(request.form['url'])

	title = getYouTubeTitle(videoID)

	appendToQueue({    'type': 'YT',
					 'title': title,
					'artist': 'YouTube'})

	return "OK: %d" % len(queue)


if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')
