#!/usr/bin/python3

#Student name: Muhammad Fuad Bin Zulkifli
#Student code: S13
#Lecturer Name: James
#Class code:CFC060524

#Navigating to Auth.log file 
log_directory='/var/log/auth.log'

#opening the auth.log file using python
#using readlines to store in data as a list
with open(log_directory,'r') as file:
	data=file.readlines()


#Creating for loop to print each line in data
for eachoutput in data:
	
	#filtering the line that contains 'command' in the line 
	if 'COMMAND' in eachoutput:
		#converting eachoutput into a list.
		convertingtolist=eachoutput.split()
		#length checker for the list to avoid for index error
		if len(convertingtolist) > 11:
			command_parts=convertingtolist[11].split('/')
			if len(command_parts) > 3:
				command=command_parts[3]
		print(f'Timestamp: {convertingtolist[0]}, User: {convertingtolist[1]}, Command executed: {command}')

# ~ 2. Log Parse auth.log: Monitor user authentication changes.

	# ~ 2.1. Print details of newly added users, including the Timestamp.
	if 'useradd' in eachoutput:
		convertingtolist=eachoutput.split()
		#Using the split('=') to split the 'name=python,' and strip() to remove any whitespaces or punctuation from the string
		newaddeduser=convertingtolist[5].split('=')[1].strip(',')
		print(f'Timestamp: {convertingtolist[0]}, {newaddeduser} is added into the system')

# ~ 2.2. Print details of deleted users, including the Timestamp.
	if 'userdel' in eachoutput:
		if 'delete user' in eachoutput:
			convertingtolist=eachoutput.split()
			userdelete=convertingtolist[5].strip("'")
			print(f'Timestamp: {convertingtolist[0]}, {userdelete} is deleted from the system')

# ~ 2.3. Print details of changing passwords, including the Timestamp.
	if 'passwd' in eachoutput:
		if 'password change' in eachoutput:
			convertingtolist=eachoutput.split()
		#converting the list to string using join() method - https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
			changepassword=' '.join(convertingtolist[4:])
			print(f'Timestamp: {convertingtolist[0]}, {changepassword}')
		
# ~ 2.4. Print details of when users used the su command.
	if 'su:session' in eachoutput:
		convertingtolist=eachoutput.split()
		switchuser=' '.join(convertingtolist[4:])
		print(f'Timestamp: {convertingtolist[0]}, {switchuser}')
	
# ~ 2.5. Print details of users who used the sudo; include the command.
	if 'sudo' in eachoutput:
		if 'COMMAND' in eachoutput:
			convertingtolist=eachoutput.split()
			if len(convertingtolist) > 11:
				command_parts=convertingtolist[11].split('/')
				if len(command_parts) > 3:
					command=command_parts[3]
					print(f'Timestamp:{convertingtolist[0]}, {convertingtolist[1]} executed sudo {command}')
					
# ~ 2.6. Print ALERT! If users failed to use the sudo command; include the command.
		if 'incorrect' in eachoutput:
			convertingtolist=eachoutput.split(';')
			#separating the data from the list using the method split 
			separatedata=convertingtolist[0].split(':')
			datastrip=separatedata[4].strip()
			if len(convertingtolist) > 11:
				command_parts=convertingtolist[11].split('/')
				if len(command_parts) > 3:
					command=command_parts[3]
			print(f'ALERT[*] User {datastrip} {separatedata[5]} to do {command}')
