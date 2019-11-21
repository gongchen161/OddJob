from datetime import datetime
class Support:
	
	@staticmethod
	def getNewSupport(conn):

		cursor = conn.cursor()

		query = 'SELECT * FROM Support WHERE status=%s'
		cursor.execute(query, ('NEW'))


		data = cursor.fetchall()

		cursor.close()

		return data

	@staticmethod
	def getMyMessages(conn, email):

		cursor = conn.cursor()

		query = 'SELECT * FROM Support WHERE email=%s'
		cursor.execute(query, (email))


		data = cursor.fetchall()

		cursor.close()

		return data

	@staticmethod
	def addSupport(conn, email, title, message):

		cursor = conn.cursor()
		messageTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

		query = 'INSERT INTO Support (email, title, message,messagetime, status ) VALUES(%s, %s, %s, %s, %s)'
		cursor.execute(query, (email, title, message, messageTime, 'NEW'))
		conn.commit()
		cursor.close()


	@staticmethod
	def replySupport(conn, supportId, reply):

		cursor = conn.cursor()

		query = 'UPDATE Support SET status=%s, reply=%s WHERE supportid=%s'
		cursor.execute(query, ('OLD', reply, supportId))
		conn.commit()
		cursor.close()
