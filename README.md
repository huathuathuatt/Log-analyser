Log Analyzer (auth.log)

This Python script parses /var/log/auth.log to monitor and extract key system events related to user activity. It tracks commands, user creation, deletion, password changes, and sudo usage.

Features:
    Command Execution Tracking – Logs commands executed by users with timestamps.
    User Management Monitoring – Detects when users are added, deleted, or change their passwords.
    su Command Logs – Tracks when users switch with the su command.
    sudo Success/Fail Alerts – Identifies both successful and failed sudo commands.

Example Output:
```bash
Timestamp: Jan 31 15:12:45, User: alice, Command executed: apt-get
Timestamp: Jan 31 15:14:10, newuser is added into the system
Timestamp: Jan 31 15:20:00, olduser is deleted from the system
Timestamp: Jan 31 15:35:00, bob changed password successfully
Timestamp: Jan 31 15:50:00, ALERT[*] User alice failed to execute sudo ls
```
# How to Use:
1. Clone the Repositor
```bash
git clone https://github.com/huathuathuatt/Log-analyser.git
```
2. Run the Script
```bash
python3 loganalyser.py
```
# Check Output: Ensure your auth.log file is located at /var/log/auth.log.
The script will parse the log file and print each relevant event in a readable format.

# Tools/Tech:
- Python 3
- Linux auth.log
