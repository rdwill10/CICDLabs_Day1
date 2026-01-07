from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return f'<h1>Hello from Docker!</h1><p>Environment: {os.getenv("ENV", "development")}</p>'


@app.route('/health')
def health():
    return {'status': 'healthy', 'app': 'flask-docker-demo'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
