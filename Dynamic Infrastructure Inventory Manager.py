from flask import Flask, jsonify, request
app= Flask(__name__)


INVENTORY_SERVERS = [
    {"id": 1, "hostname": "app-dev-01", "ip": "10.0.0.1", "env": "development", "status": "active"},
    {"id": 2, "hostname": "db-dev-01", "ip": "10.0.0.2", "env": "development", "status": "active"},
    {"id": 3, "hostname": "app-prod-01", "ip": "10.0.2.1", "env": "production", "status": "active"}
]

@app.route("/api/server",methods = ["GET"])
def get_servers():

    env_filter = request.args.get("env")

    if env_filter:
        filtering = [s for s in INVENTORY_SERVERS if s["env"].lower() == env_filter.lower()]

        return jsonify({
            "status" : "success",
            "filter_applied" : env_filter.lower(),
            "total_logs" : len(filtering),
            "logs" : filtering
        }), 200

    return jsonify({
        "status" : "success",
        "filter_applied" : "NONE (All Logs)",
        "total_logs" : len(INVENTORY_SERVERS),
        "logs" : INVENTORY_SERVERS
    }), 200


@app.route("/api/servers" ,methods = ["POST"])
def add_servers():

    server_data = request.get_json()

    if not server_data or "hostname" not in server_data or "ip" not in server_data:

        return jsonify({
            "status" : "error",
            "message" : "Missing required fields! 'hostname' and 'ip' are required."
        }), 400

    new_id = len(INVENTORY_SERVERS) + 1 if INVENTORY_SERVERS else 1

    new_server = {
        "id": new_id,
        "hostname" :server_data["hostname"],
        "ip": server_data["ip"],
        "env": server_data.get("env", "development"),
        "status": server_data.get("status", "active")  
    }

    INVENTORY_SERVERS.append(new_server)

    return jsonify({
        "status" :"Success",
        "message": "New server added to inventory!",
        "added_server": new_server,
        "total_servers": len(INVENTORY_SERVERS)
    }), 201

if __name__ == "__main__":
    app.run(debug=True, port=8003)
