adduser = ('adduser {username} --gecos '
	'"First Last,RoomNumber,WorkPhone,HomePhone"'
	' --disabled-password')

chpasswd = 'echo "{username}:{password}" | sudo chpasswd'
