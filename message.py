from datetime import datetime
class Message:
	
	@staticmethod
	def getAllMessages(conn, jobid):

		cursor = conn.cursor()

		query = 'SELECT * FROM Message WHERE jobid=%s ORDER BY messagetime;'
		cursor.execute(query, (jobid))


		data = cursor.fetchall()

		cursor.close()

		return data


	@staticmethod
	def addMessage(conn, jobid, email, quote):

		#cursor used to send queries
		cursor = conn.cursor()
		#executes quer
		messageTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

		query = 'INSERT INTO Message (jobid, email, messagetime,quote ) VALUES(%s, %s, %s, %s)'
		cursor.execute(query, (jobid, email, messageTime, quote))
		conn.commit()
		cursor.close()
