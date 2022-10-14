from flask import Flask, Response
import prometheus_client

from src import middleware

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')


app = Flask(__name__)
middleware.setup_metrics(app)

@app.route('/test/')
def test():
    return 'rest'

@app.route('/test1/')
def test1():
    1/0
    return 'rest'

@app.errorhandler(500)
def handle_500(error):
    return str(error), 500

@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run()
