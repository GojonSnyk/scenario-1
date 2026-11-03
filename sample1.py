"""A tiny Flask app with a fictional API key for demonstration only.

Install the open-source dependency with ``python -m pip install Flask``.
Run with ``python sample1.py`` and visit http://127.0.0.1:5000.
"""

import os

from flask import Flask, jsonify, request

app = Flask(__name__)

# Deliberately fake example key; never store real credentials in source code.
SAMPLE_API_KEY = os.getenv("SAMPLE_API_KEY")


@app.get("/")
def index():
	return jsonify({"message": "Sample app is running"})


@app.get("/hello")
def hello():
	# Environment variable can override the demo key for local testing.
	expected_key = os.getenv("SAMPLE_API_KEY", SAMPLE_API_KEY)
	if request.headers.get("X-API-Key") != expected_key:
		return jsonify({"error": "Unauthorized"}), 401
	return jsonify({"message": "Hello from the protected endpoint!"})


if __name__ == "__main__":
	app.run()
