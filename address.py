from datetime import datetime
class Address:
	
	@staticmethod
	def addAddress(conn, email, alias, address, city, state):

		cursor = conn.cursor()

		query = 'INSERT INTO Address (email, alias, address, city, state ) VALUES(%s,%s, %s, %s, %s)'
		cursor.execute(query, (email, alias, address, city, state))
		conn.commit()
		cursor.close()




	@staticmethod
	def getAllAddress(conn, email):

		cursor = conn.cursor()

		query = 'SELECT * FROM Address WHERE email=%s'
		cursor.execute(query, (email))

		data = cursor.fetchall()
		conn.commit()
		cursor.close()

		return data


	@staticmethod
	def getAllAddressInCityState(conn, email, city, state):

		cursor = conn.cursor()

		query = 'SELECT * FROM Address WHERE email=%s AND city=%s AND state=%s'
		cursor.execute(query, (email, city, state))

		data = cursor.fetchall()
		conn.commit()
		cursor.close()

		return data


	@staticmethod
	def editAddress(conn, email, alias, address):

		cursor = conn.cursor()

		query = 'UPDATE Address SET address = %s WHERE email = %s AND alias = %s'
		cursor.execute(query, (address, email, alias))

		conn.commit()
		cursor.close()
