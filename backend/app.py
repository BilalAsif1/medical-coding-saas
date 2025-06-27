from flask import Flask, jsonify
import sqlite3
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route("/health", methods=["GET"])
def health():
    app.logger.info('Health check requested')
    return jsonify({"status": "healthy", "python": "3.10", "system": "Pop!_OS"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
