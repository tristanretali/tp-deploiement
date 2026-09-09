from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/items")
def get_items():
    return jsonify(items=["premier item", "deuxieme item"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
