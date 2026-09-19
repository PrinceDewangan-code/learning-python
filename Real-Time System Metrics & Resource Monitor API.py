import socket
import platform
import sys
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/system/matrics" , methods = ["GET"])
def get_system_matrics():
    try:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        os_name = platform.system()
        os_release = platform.release()
        architecture = platform.machine()
        python_version = sys.version.split()[0]

        matrics_data = {
            "status" : "success",
            "system_info" : {
                "hostname" : hostname,
                "ip_address" : ip_address,
                "oprating_system" : f"{os_name} {os_release}",
                "architecture" : architecture,
                "python_version" : python_version
            }
        }
        return jsonify(matrics_data), 200

    except Exception as e:
        return jsonify({"status":"Error" , "message":str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=8001)