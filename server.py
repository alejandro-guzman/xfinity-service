from flask import Flask, request, jsonify
from xfinity_service import expose

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "OK"


@app.route("/service", methods=["POST"])
def expose_service():
    data = request.get_json()
    service_name = data["service_name"]
    host = data["host"]
    port = data["port"]
    ok = expose(service_name, host, port)
    if ok:
        return jsonify(
            {
                "status": "OK",
                "message": f"Create exposed service {service_name} on {host}:{port}",
            }
        )
    else:
        return jsonify({"status": "ERR"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
