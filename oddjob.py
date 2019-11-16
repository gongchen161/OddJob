#Import Flask Library
from flask import Flask, render_template, request, session, url_for, redirect
import pymysql.cursors
from account import Account
from job import Job
from transaction import Transaction
from skill import Skill
#Initialize the app from Flask
app = Flask(__name__)


#Configure MySQL

conn = pymysql.connect(host='localhost',
                       port = 3306,
                       user='root',
                       password='',
                       db='OddJob',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)


# CUSTOMER Index
@app.route('/')
def index():
    return render_template('index.html', type='CUSTOMER')


#WORKER Index
@app.route('/worker')
def indexWorker():
    return render_template('worker.html', type='WORKER')

#CUSTOMER Home
@app.route('/home')
def home():

    #Only CUSTOMER can access this page
    if (session['account'] == None or session['account']['accounttype'] != "CUSTOMER"):
        return render_template('error.html')

    email = session['account']['email']

    # Get all related jobs for this email acount
    postedJobs = Job.getPostedJobs(conn, email);
    confirmedJobs = Job.getConfirmedJobs(conn, email);
    completedJobs = Job.getCompletedJobs(conn, email);
    return render_template('home.html', postedJobs=postedJobs, confirmedJobs=confirmedJobs, completedJobs=completedJobs )



#WORKER Home
@app.route('/homeworker')
def homeWorker():

    #Only WORKER can access this page
    if (session['account'] == None or session['account']['accounttype'] != "WORKER"):
        return render_template('error.html')

    email = session['account']['email']
    acceptedJobs = Job.getWorkerJobs(conn, email, "PENDING");
    confirmedJobs = Job.getWorkerJobs(conn, email, "CONFIRMED");
    completedJobs = Job.getWorkerJobs(conn, email, "COMPLETED");
    print(acceptedJobs)
    return render_template('homeworker.html', acceptedJobs=acceptedJobs, confirmedJobs=confirmedJobs, completedJobs=completedJobs )

#Define a route to hello function
@app.route('/profile')
def profile():
     #Only WORKER can access this page
    if (session['account'] == None):
        return render_template('error.html')

    return render_template('profile.html')


#Define a route to hello function
@app.route('/jobboard')
def jobBoard():
     #Only WORKER can access the job board
    if (session['account'] == None or session['account']['accounttype'] != "WORKER"):
        return render_template('error.html')

    email = session['account']['email']
    jobs = Job.getAllOpenJobs(conn, email)
    approvedSkills = Skill.getApprovedSkills(conn, email)
    return render_template('jobboard.html', jobs=jobs,approvedSkills=approvedSkills)



#Define route for register
@app.route('/register/<type>')
def register(type):
	#redirect to user's home
    if (session.get('account')):
        return redirect(url_for('index'))
    return render_template('register.html', type=type)


#Define route for login
@app.route('/login/<type>')
def login(type):
	#redirect to user's home
    if (session.get('account')):
        return redirect(url_for('home'))
    return render_template('login.html', type=type)


#Authenticates the register
@app.route('/registerAuth', methods=['GET', 'POST'])
def registerAuth():
    session['message'] = None

    #grabs information from the forms
    firstName = str(request.form['firstName'])
    lastName = str(request.form['lastName'])
    email = str(request.form['email'])
    password = str(request.form['password1'])
    accountType = str(request.form['accountType'])

    password2 = str(request.form['password2'])
    if (password != password2) :
        session['message'] = "Password does not match"
        return redirect(url_for('register', type=accountType))
    
    acc = Account(email, password, firstName, lastName, accountType);

    try:
        session['account'] = acc.register(conn)
        if (accountType == 'CUSTOMER'):
            return redirect(url_for('home'))
        elif (accountType == 'WORKER'):
            return redirect(url_for('homeWorker'))
    except Exception as e:
        session['message'] = str(e)
        return redirect(url_for('register',type=accountType))

#Authenticates the login
@app.route('/loginAuth', methods=['GET', 'POST'])
def loginAuth():
    session['message'] = None
    #grabs information from the forms
    email = request.form['email']
    password = request.form['password']
    accountType = request.form['accountType']
    data = Account.checkLogIn(conn, email, password, accountType)
    
    if(data):
        #creates a session for the the user
        #session is a built in
        session['account'] = data
        if (accountType == 'CUSTOMER'):
            return redirect(url_for('home'))
        elif (accountType == 'WORKER'):
            return redirect(url_for('homeWorker'))
    else:
        #returns an error message to the html page
        session['message'] = 'Invalid login'
        return redirect(url_for('login', type=accountType))

@app.route('/logout')
def logout():
    session.pop('account')
    session.pop('message')
    return redirect('/')


#Define route for login
@app.route('/jobpost')
def jobPost():
     #Only CUSTOMER can post a job
    if (session['account'] == None or session['account']['accounttype'] != "CUSTOMER"):
        return render_template('error.html')

    allSkills = Skill.validSkills
    return render_template('jobpost.html', allSkills=allSkills)

#Define route for login
@app.route('/jobPostAuth', methods=['GET', 'POST'])
def jobPostAuth():

    job = Job()
    job.jobName = str(request.form['jobName'])
    job.jobType = str(request.form['jobType'])
    job.jobCity = str(request.form['jobCity'])
    job.jobState = str(request.form['jobState'])
    job.jobDescription = str(request.form['jobDescription'])
    job.requestorEmail = session.get('account').get('email')

    job.postJob(conn)
    
    return redirect(url_for('home'))

#Define route for login
@app.route('/acceptJobAuth', methods=['GET', 'POST'])
def acceptJobAuth():
    #redirect to user's home
    if not session.get('account'):
        return redirect(url_for('index'))

    trans = Transaction()
    trans.jobId = str(request.form['jobId'])
    trans.amount = str(request.form['jobAmount'])
    trans.acceptorEmail = session['account']['email']

    trans.postTransaction(conn)
    
    return redirect(url_for('jobBoard'))


#Define route for login
@app.route('/confirmJobAuth', methods=['GET', 'POST'])
def confirmJobAuth():
    #redirect to user's home
    if not session.get('account'):
        return redirect(url_for('index'))

    acceptorEmail = str(request.form['acceptorEmail'])
    jobId = str(request.form['jobId'])
    Transaction.confirmTransaction(conn, jobId, acceptorEmail)
    
    return redirect(url_for('home'))


#Define route for login
@app.route('/completeJobAuth', methods=['GET', 'POST'])
def completeJobAuth():
    #redirect to user's home
    
    if not session.get('account'):
        return redirect(url_for('index'))

    jobId = str(request.form['jobId'])
    Transaction.completeTransaction(conn, jobId, session['account']['email'])
    
    return redirect(url_for('home'))


#Define route for login
@app.route('/payJobAuth', methods=['GET', 'POST'])
def payJobAuth():

    jobId = str(request.form['jobId'])
    tran = Transaction.getConfirmedTransaction(conn, jobId)

    return render_template("payment.html", line=tran)


#Define route for login
@app.route('/rateAuth', methods=['GET', 'POST'])
def rateAuth():
    #redirect to user's home
    if not session.get('account'):
        return redirect(url_for('index'))

    jobId = str(request.form['jobId'])
    rating = str(request.form['rating'])
    comment = str(request.form['comment'])
    Transaction.rateTransaction(conn, jobId, rating, comment)
    
    return redirect(url_for('home'))



#Define route for login
@app.route('/updateProfileAuth', methods=['GET', 'POST'])
def updateProfileAuth():
    #redirect to user's home
    if not session.get('account'):
        return redirect(url_for('index'))

    fname = str(request.form['firstName'])
    lname = str(request.form['lastName'])
    email = session['account']['email']
    accType = session['account']['accounttype']
    motto = str(request.form['motto'])

    session['account'] = Account.update(conn, fname, lname, email, motto)
    
    if accType == 'CUSTOMER':
        return redirect(url_for('home'))
    else:
        return redirect(url_for('homeWorker'))

#Define route for login
@app.route('/job/<id>')
def viewJob(id):
     #Only the Customer can access this page
    if (session['account'] == None or session['account']['accounttype'] != "CUSTOMER"):
        return render_template('error.html')

    job = Job.getJobInfo(conn, id)

    # Only the owner of this Job can view the detail of this job
    if (job['requestoremail'] != session['account']['email']):
        return render_template('error.html')

    trans = Job.getAllTransactions(conn, id)

    return render_template('job.html', job=job, trans=trans)

#Define route for login
@app.route('/viewworker/<email>')
def viewWorker(email):
     #Only the Customer can access this page
    if (session['account'] == None or session['account']['accounttype'] != "CUSTOMER"):
        return render_template('error.html')

    worker = Account.getAccountInfo(conn, email)
    rating = Account.getAvgRating(conn, email)
    trans = Account.getAllCompletedTransactions(conn, email)

    total = len(trans)
    rating = rating[0].get('avgRate')

    return render_template('viewworker.html', worker=worker, rating=rating,total=total,trans=trans)

#Define route for login
@app.route('/backgroundcheck')
def backgroundCheck():
     #Only the Customer can access this page
    if (session['account'] == None or session['account']['accounttype'] != "WORKER"):
        return render_template('error.html')
    remainingSkills = Skill.getRemainingSkills(conn, session['account']['email'])
    pendingSkills = Skill.getPendingSkills(conn, session['account']['email'])
    approvedSkills = Skill.getApprovedSkills(conn, session['account']['email'])
    return render_template('backgroundcheck.html', remainingSkills=remainingSkills, pendingSkills=pendingSkills, approvedSkills=approvedSkills)


#Define route for login
@app.route('/backgroundCheckAuth', methods=['GET', 'POST'])
def backgroundCheckAuth():
    #redirect to user's home
    if not session.get('account'):
        return redirect(url_for('index'))


    email = session['account']['email']
    skills = request.form.getlist('skill')

    for skill in skills:
        Skill.applySkill(conn, email, skill)

    return redirect(url_for('homeWorker'))

#Define route for login
@app.route('/cancelJobAuth', methods=['GET', 'POST'])
def cancelJobAuth():
    #redirect to user's home
    if not session.get('account'):
        return redirect(url_for('index'))

    jobid = request.form['jobid']

    Job.cancelJob(conn, jobid)

    return redirect(url_for('home'))

@app.route('/searchJobAuth', methods=['GET', 'POST'])
def searchJobAuth():
    #redirect to user's home
    if not session.get('account'):
        return redirect(url_for('index'))

    jobType = request.form['jobType']
    jobState = request.form['jobState']

    jobs = Job.getJobSearchResult(conn, jobType, jobState)
    approvedSkills = Skill.getApprovedSkills(conn, email)
    return render_template('jobboard.html', jobs=jobs,approvedSkills=approvedSkills)

app.secret_key = 'ODDJOB'

if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug = True)