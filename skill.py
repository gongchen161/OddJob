class Skill:
	validSkills = ['House keeping', 'Landscaping', 'Home Improvement', 'Baby Sitting', 'Plumbing']

	@staticmethod
	def applySkill(conn, email, skill):

		cursor = conn.cursor()

		ins = 'INSERT INTO Skill VALUES(%s, %s, %s)'
		cursor.execute(ins, (email, skill, "PENDING"))
		conn.commit()

		cursor.close()


	@staticmethod
	def getRemainingSkills(conn, email):

		cursor = conn.cursor()
		result = []
		for skill in Skill.validSkills:
			q = 'SELECT * FROM Skill WHERE email=%s AND skillname=%s'
			cursor.execute(q, (email, skill))
			conn.commit()

			if (cursor.rowcount == 0):
				result.append(skill)

		cursor.close()

		return result


	@staticmethod
	def getApprovedSkills(conn, email):

		cursor = conn.cursor()
		result = []
		for skill in Skill.validSkills:
			q = 'SELECT * FROM Skill WHERE email=%s AND skillname=%s AND status=%s'
			cursor.execute(q, (email, skill, 'APPROVED'))
			conn.commit()

			if (cursor.rowcount == 1):
				result.append(skill)

		cursor.close()

		return result


	@staticmethod
	def getPendingSkills(conn, email):

		cursor = conn.cursor()
		result = []
		for skill in Skill.validSkills:
			q = 'SELECT * FROM Skill WHERE email=%s AND skillname=%s AND status=%s'
			cursor.execute(q, (email, skill, 'PENDING'))
			conn.commit()

			if (cursor.rowcount == 1):
				result.append(skill)

		cursor.close()

		return result

	@staticmethod
	def getPendingApplications(conn):

		cursor = conn.cursor()

		q = 'SELECT * FROM Skill WHERE status=%s'

		cursor.execute(q, ('PENDING'))
		
		data = cursor.fetchall()

		return data

	@staticmethod
	def approveSkill(conn, email, skillName):
		cursor = conn.cursor()
		print(email, skillName)
		query = 'UPDATE Skill SET status = %s WHERE email = %s AND skillname = %s'
		cursor.execute(query, ('APPROVED', email, skillName))
		conn.commit()
		cursor.close()



