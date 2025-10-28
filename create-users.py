!/usr/bin/python3

# INET4031
# Nathan Meadows
# October 27th 2025
# October 27th 2025

# os: used to run Linux system commands from inside Python (e.g., adduser, passwd, add to group)
# re: used for regular expression matching to detect comment lines (lines that start with #)
# sys: used to read input from stdin (the create-users.input file is redirected into the script)
import os
import re
import sys


def main():
    for line in sys.stdin:

        # This regular expression checks if a line begins with the "#" character. This is to check if the line is a comment or not
        match = re.match("^#",line)

        # This line removes any extra spaces or newline characters from the line,
	# then splits the remaining text into separate data fields using ":" as the delimiter.
	# This allows the script to extract the username, password, first name, last name, and group information.
        fields = line.strip().split(':')

        # This IF statement checks two conditions:
	# (1) if the current line is a comment line (starts with '#'), or
	# (2) if the line does not contain exactly 5 fields separated by colons.
	# If either is true, the line is skipped because it’s invalid or not meant to create a user.
        if match or len(fields) != 5:
            continue

        # These three lines extract data from the input line.
	# The username and password are stored separately, and a GECOS string
	# is built to hold the user's full name (First Last,,,) for the /etc/passwd entry.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        # This splits the last field (groups) into a list using commas as separators.
	# It allows the program to handle multiple groups for a single user.
        groups = fields[4].split(',')

        # Prints a message to show which user account is being processed.
        print("==> Creating account for %s..." % (username))
        # Builds the Linux command that will be run to create the user account.
	# The variable "cmd" stores the full shell command used by os.system() later.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #Keeping os.system(cmd) commented = dry run (no real users)
	#uncommenting os.system(cmd) = real execution which will add the users to ubuntu.
        print cmd
        #os.system(cmd)

	  #Prints a message to show the password is being set for a specific username
        print("==> Setting the password for %s..." % (username))
        ## This line builds the Linux command used to set the new user's password.
	# It uses 'echo -ne' to send the password twice (as required by 'passwd') through a pipe into 'sudo passwd <username>'.
	# The variable 'cmd' stores the full shell command string that, when executed, will automatically set the user's password.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #Again, if you uncomment the os.system(cmd) it will build this into the ubuntu system and not just simply print the output.
        print cmd
        #os.system(cmd)

        for group in groups:
            # This IF statement checks whether the group value is not equal to '-',
	    # A '-' means the user should not be assigned to any groups
            # IF the condition is true, the script prints a message and runs the command to add the user to the specified group using the 'adduser' command.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                #os.system(cmd)



if __name__ == '__main__':
    main()
