"""
PROGRAM NAME: WifiAppOne
PROGRAMMER: James Hill, Stable Kernel
SYSTEM: Coded in Python,  Running on a Raspberry Pi. Accessible at 192.168.1.154:5000
DESCRIPTION: This headless API provides endpoints to retrieve signal information and
 available wifi networks. It receives a password from the user and confirms or denies access.


"""

from flask import Flask, request, jsonify

app = Flask(__name__)  # initialize a flask app

# Sample Data: Signal Info and Quality
signal_info = {
    "strength": 75,
    "quality": "good"
}

# Map of SSIDs to passwords
wifi_passwords = {
    "MyWifiNetwork1": "MercuryMA6",
    "MyWifiNetwork2": "Gemini4GLV3",
    "MyWifiNetwork3": "Apollo11CSM107"
}

# List of SSIDs
wifi_networks = {
    "MyWifiNetwork1",
    "MyWifiNetwork2",
    "MyWifiNetwork3"
}


# This route is used to provide signal information
@app.route('/api/signal', methods=["GET"])
def get_signal_info():
    return jsonify(signal_info)


# This route is used to provide a list of SSIDs
@app.route('/api/networks', methods=["GET"])
def get_wifi_networks():
    return jsonify(wifi_networks)


# This route is used to receive a password from the user
@app.route('/api/password', methods=["POST"])
def receive_password():
    data = request.json
    network_name = data['network_name']
    received_password = data['password']

    if network_name in wifi_passwords and wifi_passwords[network_name] == received_password:
        response = {"message": "Password accepted for Wifi Network: " + network_name}
    else:
        response = {"message": "Password rejected for Wifi Network: " + network_name}

        return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
