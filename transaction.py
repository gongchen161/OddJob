from datetime import datetime
class Transaction:
    def __init__(self):
        self.jobId = None
        self.acceptorEmail = None
        self.rating = None
        self.status = None
        self.amount = None
        self.note = None

    def postTransaction(self, conn):
      	#cursor used to send queries
        cursor = conn.cursor()
        #executes quer
        jobTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        ins = 'INSERT INTO Transaction (jobid, acceptoremail, status,amount, note, transactiontime ) VALUES(%s, %s, %s, %s, %s, %s)'
        cursor.execute(ins, (self.jobId, self.acceptorEmail, "PENDING", self.amount, self.note, jobTime))
        conn.commit()
        cursor.close()

        return self

    @staticmethod
    def confirmTransaction(conn, jobId, acceptorEmail):
        #cursor used to send queries
        cursor = conn.cursor()
        #executes quer
        jobTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Update the selected transaction to be CONFIRMED
        ins = 'UPDATE Transaction SET status = %s WHERE jobid = %s AND acceptorEmail = %s'
        cursor.execute(ins, ('CONFIRMED', jobId, acceptorEmail))
        conn.commit()

        # Update all the others to be REJECTED
        ins = 'UPDATE Transaction SET status = %s WHERE jobid = %s AND acceptorEmail != %s'
        cursor.execute(ins, ('REJECTED', jobId, acceptorEmail))
        conn.commit()


        # Update Job Status
        ins = 'UPDATE Job SET jobstatus = %s WHERE jobid = %s'
        cursor.execute(ins, ('CONFIRMED', jobId))
        conn.commit()


        cursor.close()


    @staticmethod
    def rateTransaction(conn, jobId, rating, comment):
        #cursor used to send queries
        cursor = conn.cursor()
        #executes quer
        jobTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        ins = 'UPDATE Rate SET rating = %s, comment = %s WHERE jobid = %s'
        cursor.execute(ins, (rating, comment, jobId))
        conn.commit()

        cursor.close()

    @staticmethod
    def completeTransaction(conn, jobId,requestorEmail) :
        #cursor used to send queries
        cursor = conn.cursor()
        #executes quer
        jobTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        ins = 'UPDATE Transaction SET status = %s WHERE jobid = %s AND status = %s'
        cursor.execute(ins, ('COMPLETED', jobId, 'CONFIRMED'))
        conn.commit()



        ins = 'UPDATE Job SET jobstatus = %s WHERE jobid = %s'
        cursor.execute(ins, ('COMPLETED', jobId))
        conn.commit()

        ins = 'INSERT INTO Rate VALUES(%s, %s, %s, %s, %s)'
        cursor.execute(ins, (jobId, requestorEmail, None, jobTime, None))
        conn.commit()

        cursor.close()

    @staticmethod
    def getConfirmedTransaction(conn, jobId):
        #cursor used to send queries
        cursor = conn.cursor()
    
        ins = 'SELECT * FROM Transaction JOIN Job USING (jobid) WHERE jobid = %s AND status = %s'
        cursor.execute(ins, (jobId, 'CONFIRMED'))
        conn.commit()

        data = cursor.fetchone()
        cursor.close()

        return data
