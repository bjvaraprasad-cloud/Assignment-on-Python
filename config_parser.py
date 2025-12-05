import configparser
import json
from flask import Flask, jsonify

app = Flask(__name__)
config_data = {}

try:
    config = configparser.ConfigParser()
    config.read('config.ini')  # Make sure config.ini exists in the same directory

    for section in config.sections():
        config_data[section] = {}
        for key, value in config.items(section):
            config_data[section][key] = value

    # Save as JSON locally (simulating database storage)
    with open('config.json', 'w') as f:
        json.dump(config_data, f, indent=4)

except FileNotFoundError:
    print("Configuration file not found!")
except Exception as e:
    print(f"An error occurred while reading the configuration: {e}")

@app.route('/config', methods=['GET'])
def get_config():
    return jsonify(config_data)

if __name__ == "__main__":
    print("Starting Flask API on http://127.0.0.1:5000/config")
    app.run(debug=True)
