from datetime import datetime
class Job:
    def __init__(self):
        self.requestorEmail = None
        self.jobName = None
        self.jobType = None
        self.jobCity = None
        self.jobState = None
        self.jobdescription = None
        self.jobStatus =None


    @staticmethod
    def getPostedJobs(conn, email):

        cursor = conn.cursor()

        query = 'SELECT * FROM Job WHERE requestoremail = %s AND jobstatus= %s'
        cursor.execute(query, (email, 'POSTED'))

        data = cursor.fetchall()

        cursor.close()

        return data

    @staticmethod
    def getAcceptor(conn, jobid):

        cursor = conn.cursor()

        query = 'SELECT * FROM Transaction WHERE jobid = %s AND (status= %s OR status=%s)'
        cursor.execute(query, (jobid, 'CONFIRMED', 'COMPLETED'))

        data = cursor.fetchone()

        cursor.close()

        return data


    @staticmethod
    def getAcceptedTransaction(conn, jobid):

        cursor = conn.cursor()

        query = 'SELECT * FROM Transaction JOIN Account ON (Transaction.acceptoremail=Account.email) WHERE jobid = %s AND (status= %s OR status=%s)'
        cursor.execute(query, (jobid, 'CONFIRMED', 'COMPLETED'))

        data = cursor.fetchone()

        cursor.close()

        return data

    @staticmethod
    def getConfirmedJobs(conn, email):

        cursor = conn.cursor()
        # need to join Transaction to get more info about the worker
        query = 'SELECT * FROM Job JOIN Transaction ON (Job.jobid = Transaction.jobid) JOIN Account ON(Transaction.acceptoremail=Account.email) WHERE requestoremail = %s AND jobstatus= %s AND status = %s'
        cursor.execute(query, (email, 'CONFIRMED', 'CONFIRMED'))
        data = cursor.fetchall()

        cursor.close()

        return data

    @staticmethod
    def getCompletedJobs(conn, email):

        cursor = conn.cursor()
        # need to join Transaction and rating to get more info 
        query = 'SELECT * FROM Job JOIN Transaction ON (Job.jobid = Transaction.jobid) JOIN Account ON(Transaction.acceptoremail=Account.email) JOIN Rate ON (Job.jobid = Rate.jobid) WHERE Job.requestoremail = %s AND jobstatus= %s AND status = %s'
        cursor.execute(query, (email, 'COMPLETED', 'COMPLETED'))

        data = cursor.fetchall()
        cursor.close()

        return data

    @staticmethod
    def getWorkerJobs(conn, email, status):

        cursor = conn.cursor()

        query = 'SELECT * FROM Transaction NATURAL JOIN Job WHERE acceptoremail = %s AND status = %s'
        
        if (status == 'COMPLETED'):
            query = 'SELECT * FROM Transaction NATURAL JOIN Job JOIN Rate ON (Job.jobid=Rate.jobid) WHERE acceptoremail = %s AND status = %s'
        cursor.execute(query, (email, status))

        data = cursor.fetchall()

        cursor.close()

        return data  

    def postJob(self, conn):

        cursor = conn.cursor()

        jobTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ins = 'INSERT INTO Job (requestoremail, jobname, jobtype, jobcity,jobstate,jobdescription, jobstatus, jobtime) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(ins, (self.requestorEmail, self.jobName, self.jobType, self.jobCity, self.jobState, self.jobDescription, 'POSTED', jobTime))
        conn.commit()

        cursor.close()

        return self

    @staticmethod
    def getAllOpenJobs(conn, email):

        cursor = conn.cursor()

        query = 'SELECT * FROM Job JOIN Account ON (Job.requestoremail = Account.email) WHERE jobstatus = %s AND jobid NOT IN (SELECT jobid FROM Transaction WHERE acceptoremail=%s)'
        cursor.execute(query, ('POSTED', email))

        data = cursor.fetchall()

        cursor.close()

        return data
    @staticmethod
    def getJobInfo(conn, jobId):

        cursor = conn.cursor()

        query = 'SELECT * FROM Job WHERE jobid = %s'
        cursor.execute(query, (jobId))

        data = cursor.fetchone()

        cursor.close()

        return data

    @staticmethod
    def getAllTransactions(conn, jobId):

        cursor = conn.cursor()

        query = 'SELECT * FROM Transaction JOIN Account ON (Transaction.acceptoremail = Account.email) WHERE jobid = %s'
        cursor.execute(query, (jobId))

        data = cursor.fetchall()

        cursor.close()

        return data


    @staticmethod
    def getJob(conn, id):

        cursor = conn.cursor()

        query = 'SELECT * FROM Transaction NATURAL JOIN Job WHERE jobid = %s'
        cursor.execute(query, (id))

        data = cursor.fetchall()

        cursor.close()

        return data

    @staticmethod
    def getJobSearchResult(conn, jobType, jobState, email):

        cursor = conn.cursor()

        query = 'SELECT * FROM Job JOIN Account ON (Job.requestoremail=Account.email) WHERE jobType=%s AND jobState=%s AND jobstatus=%s AND jobid NOT IN (SELECT jobid FROM Transaction WHERE Transaction.acceptoremail=%s)'
        cursor.execute(query, (jobType, jobState, 'POSTED', email))

        data = cursor.fetchall()

        cursor.close()

        return data


    @staticmethod
    def cancelJob(conn, id):

        cursor = conn.cursor()

        query = 'DELETE FROM Transaction WHERE jobid = %s'
        cursor.execute(query, (id))
        query = 'DELETE FROM Job WHERE jobid = %s'
        cursor.execute(query, (id))

        cursor.close()

    @staticmethod
    def getRating(conn, id):

        cursor = conn.cursor()

        query = 'SELECT * FROM Rate WHERE jobid=%s'
        cursor.execute(query, (id))

        data=cursor.fetchone()

        cursor.close()
        return data

    @staticmethod
    def updateJobAddress(conn, alias, id):

        cursor = conn.cursor()

        query = 'UPDATE Job SET jobaddress = %s WHERE jobid = %s'
        cursor.execute(query, (alias, id))

        cursor.close()
