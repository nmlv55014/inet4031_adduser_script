# inet4031_adduser_script

## Program Description
This program automates the process of creating multiple users and groups on an Ubuntu system. Normally, a system administrator would need to manually type several commands such as `sudo adduser`, `sudo groupadd`, and `sudo usermod -aG` for each account. This script simplifies that process by reading an input file that lists all the users to be created and automatically runs those same Linux commands through Python’s `os.system()` function.

By using this automated method, administrators can quickly and accurately deploy multiple accounts, reduce errors from manual entry, and ensure consistency across multiple servers.

---

## Program User Operation
This program reads user information from an input file and creates each user and their associated groups automatically. After setting up the script and input file, the user can perform a “dry run” to preview the commands that would execute or run the script in normal mode to actually create the users.

Before running the script, make sure:
1. You are in the same directory as `create-users.py` and `create-users.input`.
2. The Python file has executable permissions using:
   ```bash
   chmod +x create-users.py
