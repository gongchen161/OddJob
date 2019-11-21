class Account:
	def __init__(self, email, password, firstName, lastName, accountType):
		self.email = email
		self.firstName = firstName
		self.lastName = lastName
		self.password = password
		self.accountType = accountType

	def register(self, conn):

		cursor = conn.cursor()

		#check if the account already exists in the data base
		query = 'SELECT * FROM Account WHERE email = %s'
		cursor.execute(query, (self.email))

		data = cursor.fetchone()

		if data:
			raise Exception("Account already exists")

		ins = 'INSERT INTO Account VALUES(%s, SHA2(%s, 256), %s, %s, %s, "")'
		cursor.execute(ins, (self.email, self.password, self.firstName, self.lastName, self.accountType))
		conn.commit()

		#return the restered account back to the caller
		query = 'SELECT * FROM Account WHERE email = %s'
		cursor.execute(query, (self.email))
		data = cursor.fetchone()


		cursor.close()

		return data

	@staticmethod
	def getAccountInfo(conn, email):
		cursor = conn.cursor()
		query = 'SELECT * FROM Account WHERE email = %s'
		cursor.execute(query, (email))
		data = cursor.fetchone()
		cursor.close()

		return data



	@staticmethod
	def update(conn, fname, lname, email, motto):
		cursor = conn.cursor()
		query = 'UPDATE Account SET firstname = %s, lastname = %s, motto = %s WHERE email = %s'
		cursor.execute(query, (fname, lname, motto, email))

		query = 'SELECT * FROM Account WHERE email = %s'
		cursor.execute(query, (email))
		data = cursor.fetchone()
		cursor.close()

		return data

	@staticmethod
	def checkLogIn(conn, email, password, accountType):
		cursor = conn.cursor()
		query = 'SELECT * FROM Account WHERE email = %s and password = SHA2(%s, 256) and accounttype = %s'
		cursor.execute(query, (email, password, accountType))
		data = cursor.fetchone()
		cursor.close()

		return data

	@staticmethod
	def getAvgRating(conn, email):
		#cursor used to send queries
		cursor = conn.cursor()

		ins = 'SELECT AVG(rating) AS avgRate FROM Rate JOIN Transaction USING (jobid) WHERE acceptoremail = %s AND status = %s'
		cursor.execute(ins, (email, 'COMPLETED'))
		conn.commit()

		data = cursor.fetchall()
		cursor.close()

		return data
	
	@staticmethod
	def getAllCompletedTransactions(conn, email):
		cursor = conn.cursor()

		ins = 'SELECT * FROM Rate JOIN Transaction USING (jobid) JOIN Job USING (jobid) WHERE acceptoremail = %s AND status = %s'
		cursor.execute(ins, (email, 'COMPLETED'))
		conn.commit()

		data = cursor.fetchall()
		cursor.close()

		return data

	@staticmethod
	def comparePassword(conn, email, password):
		cursor = conn.cursor()

		query = 'SELECT * FROM Account WHERE email=%s AND password=SHA2(%s, 256)'
		cursor.execute(query, (email, password))
		conn.commit()

		data = cursor.fetchone()
		cursor.close()

		return cursor.rowcount==1

	@staticmethod
	def updatePassword(conn, email, password):
		cursor = conn.cursor()

		query = 'UPDATE Account SET password=SHA2(%s, 256) WHERE email=%s'
		cursor.execute(query, (password, email))
		conn.commit()


