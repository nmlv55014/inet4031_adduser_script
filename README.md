# inet4031_adduser_script

## Program Description
This program automates creating multiple Linux user accounts on Ubuntu using Python. Instead of manually running commands like `adduser`, `passwd`, and adding users to groups, the script reads a structured input file and executes **those same commands** for each user:

- `/usr/sbin/adduser --disabled-password --gecos ... <username>`
- `echo -ne '<pw>\n<pw>' | sudo passwd <username>`
- `/usr/sbin/adduser <username> <group>` (adds existing user to a supplementary group)

It builds each user’s **GECOS** field as `First Last,,,'` (matches what you’ll see in `/etc/passwd`), sets the password, and assigns any listed groups.

---

## Program User Operation
At a high level, the program:

1. **Reads lines from STDIN** (the input file is redirected with `<`).
2. **Skips** any line that starts with `#` (comment) or that doesn’t have the required 5 fields.
3. **Parses** fields into: `username`, `password`, `last_name`, `first_name`, and `groups`.
4. **Creates** the user with a proper GECOS string (`First Last,,,`), **sets the password**, and **adds group memberships**.
5. Prints status messages as it goes so you can see what’s happening.

### Input File Format
Each line represents one user and must have **five** colon-separated fields:

### Command Execution
To run the script, open your terminal in the same directory that contains both `create-users.py` and `create-users.input`.
**1. Make the script executable:**
```bash
chmod +x create-users.py
```
#2. Perform a dry run (safe test):
#Copy code
```bash
./create-users.py < create-users.input
#This prints the commands that would run without actually creating users.
#3. Run for real (apply changes):
#Copy code
sudo ./create-users.py < create-users.input
#Before doing this, make sure you’ve uncommented all os.system(cmd) lines in the script so it can actually execute the user and group creation commands.



