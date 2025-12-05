# Git Assignment - HeroVired

This repository contains Python scripts for various DevOps tasks, including password strength checking, CPU monitoring, configuration file parsing, and backup automation.  

Q1: Password Strength Checker**

**File:** 'Pass_Check.py'

**Description:**  
Checks if a user-provided password is strong based on the following criteria:
- Minimum length of 8 characters
- Contains both uppercase and lowercase letters
- Contains at least one digit (0-9)
- Contains at least one special character (e.g., !, @, #, $)

**Usage:**
```bash
python Pass_Check.py


===========Q2: CPU Usage Monitor========

File: CPU_monitor.py

Description:
Continuously monitors the CPU usage of the local machine and alerts if
usage exceeds a predefined threshold (default 80%).

Dependencies:
pip install psutil
Usage:
python cpu_monitor.py
Sample Output:

Monitoring CPU usage...
Current CPU Usage: 45%
Current CPU Usage: 87%
Alert! CPU usage exceeds threshold: 87%


Press Ctrl+C to stop monitoring.

=============Q3: Configuration File Parser & API

File: config_parser.py
Configuration File: config.ini

Description:
Reads a configuration file (config.ini)

Extracts key-value pairs and saves them as JSON (config.json)
Provides a GET API endpoint to fetch configuration data using Flask

Dependencies:
pip install flask

Usage:
Ensure config.ini exists in the same directory.
Run the script:
python config_parser.py
Access API:

http://127.0.0.1:5000/config
Sample config.ini:
[Database]
host = localhost
port = 3306
username = admin
password = secret

[Server]
address = 192.168.0.1
port = 8080


Sample JSON Output:

{
    "Database": {
        "host": "localhost",
        "port": "3306",
        "username": "admin",
        "password": "secret"
    },
    "Server": {
        "address": "192.168.0.1",
        "port": "8080"
    }
}

============Q4: Backup Script
File: backup.py

Description:

Backs up all files from a source directory to a destination directory
Appends a timestamp to file names if duplicates exist
Handles non-existent directories gracefully

Usage:

python backup.py /path/to/source /path/to/destination
