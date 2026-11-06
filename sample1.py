
import os

from flask import Flask, jsonify, request

app = Flask(__name__)

SAMPLE_API_KEY = "demo_fake_key_12345"

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