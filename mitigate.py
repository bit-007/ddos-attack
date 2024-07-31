from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging

app = Flask(__name__)

# Configure Flask-Limiter
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/')
@limiter.limit("5 per minute")
def index():
    return "Welcome to the rate-limited Flask app!"

@app.route('/api')
@limiter.limit("10 per minute")
def api():
    return "This is the rate-limited API endpoint."

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(host='0.0.0.0', port=8000)
