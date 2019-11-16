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
    def getConfirmedJobs(conn, email):

        cursor = conn.cursor()
        # need to join Transaction to get more info about the worker
        query = 'SELECT * FROM Job JOIN Transaction ON (Job.jobid = Transaction.jobid) WHERE requestoremail = %s AND jobstatus= %s AND status = %s'
        cursor.execute(query, (email, 'CONFIRMED', 'CONFIRMED'))
        data = cursor.fetchall()

        cursor.close()

        return data

    @staticmethod
    def getCompletedJobs(conn, email):

        cursor = conn.cursor()
        # need to join Transaction and rating to get more info 
        query = 'SELECT * FROM Job JOIN Transaction ON (Job.jobid = Transaction.jobid) JOIN Rate ON (Job.jobid = Rate.jobid) WHERE Job.requestoremail = %s AND jobstatus= %s AND status = %s'
        cursor.execute(query, (email, 'COMPLETED', 'COMPLETED'))

        data = cursor.fetchall()
        cursor.close()

        return data

    @staticmethod
    def getWorkerJobs(conn, email, status):
        #cursor used to send queries
        cursor = conn.cursor()
        #executes query
        query = 'SELECT * FROM Transaction NATURAL JOIN Job WHERE acceptoremail = %s AND status = %s'
        
        if (status == 'COMPLETED'):
            query = 'SELECT * FROM Transaction NATURAL JOIN Job JOIN Rate ON (Job.jobid=Rate.jobid) WHERE acceptoremail = %s AND status = %s'
        cursor.execute(query, (email, status))
        #stores the results in a variable
        data = cursor.fetchall()
        #use fetchall() if you are expecting more than 1 data row
        cursor.close()

        return data  

    def postJob(self, conn):
      	#cursor used to send queries
        cursor = conn.cursor()
        #executes quer
        jobTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ins = 'INSERT INTO Job (requestoremail, jobname, jobtype, jobcity,jobstate,jobdescription, jobstatus, jobtime) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
        cursor.execute(ins, (self.requestorEmail, self.jobName, self.jobType, self.jobCity, self.jobState, self.jobDescription, 'POSTED', jobTime))
        conn.commit()

        cursor.close()

        return self

    @staticmethod
    def getAllOpenJobs(conn, email):
        #cursor used to send queries
        cursor = conn.cursor()
        #executes query
        query = 'SELECT * FROM Job JOIN Account ON (Job.requestoremail = Account.email) WHERE jobstatus = %s AND jobid NOT IN (SELECT jobid FROM Transaction WHERE acceptoremail=%s)'
        cursor.execute(query, ('POSTED', email))
        #stores the results in a variable
        data = cursor.fetchall()
        #use fetchall() if you are expecting more than 1 data row
        cursor.close()

        return data
    @staticmethod
    def getJobInfo(conn, jobId):
        #cursor used to send queries
        cursor = conn.cursor()
        #executes query
        query = 'SELECT * FROM Job WHERE jobid = %s'
        cursor.execute(query, (jobId))
        #stores the results in a variable
        data = cursor.fetchone()
        #use fetchall() if you are expecting more than 1 data row
        cursor.close()

        return data

    @staticmethod
    def getAllTransactions(conn, jobId):
        #cursor used to send queries
        cursor = conn.cursor()
        #executes query
        query = 'SELECT * FROM Transaction JOIN Account ON (Transaction.acceptoremail = Account.email) WHERE jobid = %s'
        cursor.execute(query, (jobId))
        #stores the results in a variable
        data = cursor.fetchall()
        #use fetchall() if you are expecting more than 1 data row
        cursor.close()

        return data


    @staticmethod
    def getJob(conn, id):
        #cursor used to send queries
        cursor = conn.cursor()
        #executes query
        query = 'SELECT * FROM Transaction NATURAL JOIN Job WHERE jobid = %s'
        cursor.execute(query, (id))
        #stores the results in a variable
        data = cursor.fetchall()
        #use fetchall() if you are expecting more than 1 data row
        cursor.close()

        return data

    @staticmethod
    def getJobSearchResult(conn, jobType, jobState):
        #cursor used to send queries
        cursor = conn.cursor()
        #executes query
        query = 'SELECT * FROM Job WHERE jobType=%s AND jobState=%s'
        cursor.execute(query, (jobType, jobState))
        #stores the results in a variable
        data = cursor.fetchall()
        #use fetchall() if you are expecting more than 1 data row
        cursor.close()

        return data


    @staticmethod
    def cancelJob(conn, id):
        #cursor used to send queries
        cursor = conn.cursor()
        #executes query
        query = 'DELETE FROM Transaction WHERE jobid = %s'
        cursor.execute(query, (id))
        query = 'DELETE FROM Job WHERE jobid = %s'
        cursor.execute(query, (id))

        cursor.close()

    @staticmethod
    def getRating(conn, id):
        #cursor used to send queries
        cursor = conn.cursor()
        #executes query
        query = 'SELECT * FROM Rate WHERE jobid=%s'
        cursor.execute(query, (id))

        data=cursor.fetchone()

        cursor.close()
        return data