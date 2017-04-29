from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
	url = 'https://cloud.githubusercontent.com/assets/2317815/24526433/b0cf65ac-158d-11e7-9c87-75a2f4c929d9.gif'
	alt = "It's alive!!!"
	return '<img src="%s" alt="%s">' % (url, alt)


if __name__ == '__main__':
	app.run()
