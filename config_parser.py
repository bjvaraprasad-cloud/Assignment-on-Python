import configparser
import json
import sqlite3
import os

def parse_config(file_path):
    config = configparser.ConfigParser()

    if not os.path.exists(file_path):
        raise FileNotFoundError("Configuration file not found!")

    config.read(file_path)

    result = {
        "Database": {
            "host": config.get("Database", "host"),
            "port": config.get("Database", "port"),
            "username": config.get("Database", "username"),
            "password": config.get("Database", "password")
        },
        "Server": {
            "address": config.get("Server", "address"),
            "port": config.get("Server", "port")
        }
    }
    return result


# -------- SAVE TO DATABASE (SQLite Example) --------
def save_to_db(data):
    conn = sqlite3.connect("config_data.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS config (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            json_data TEXT
        )
    """)

    cursor.execute("INSERT INTO config (json_data) VALUES (?)", (json.dumps(data),))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    file_path = "config.ini"  # make sure config.ini is in same folder
    try:
        parsed_data = parse_config(file_path)
        print("\nParsed Configuration:\n", parsed_data)

        save_to_db(parsed_data)
        print("\nData saved to SQLite database successfully!")

    except Exception as e:
        print("Error:", e)

