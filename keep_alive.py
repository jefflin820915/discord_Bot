from flask import Flask
from gevent import pywsgi
from threading import Thread

app = Flask('')

@app.route('/')
def main():
	return 'Bot is aLive!'

def run():
  server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
  server.serve_forever()


def keep_alive():
  server = Thread(target=run)
  server.start()