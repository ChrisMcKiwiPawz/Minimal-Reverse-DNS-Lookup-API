import socket
from flask import Flask, jsonify, request

a = Flask(__name__)

@a.route("/reverse-dns", methods=["GET"])
def reverse_dns():
    ip = request.args.get("ip")
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
        return jsonify({"hostname": hostname}), 200
    except socket.herror:
        return jsonify({"error": "No hostname found"}), 404

a.run()
