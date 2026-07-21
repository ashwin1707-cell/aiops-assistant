from flask import Flask, jsonify, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from datetime import datetime

app = Flask(__name__)

REQUEST_COUNTER = Counter(
    "aiops_requests_total",
    "Total HTTP Requests"
)

@app.route("/")
def home():
    REQUEST_COUNTER.inc()
    return jsonify({
        "application": "AIOps Assistant",
        "status": "Running",
        "version": "1.0"
    })

@app.route("/health")
def health():
    REQUEST_COUNTER.inc()
    return jsonify({
        "status": "healthy",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )