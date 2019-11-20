
CREATE TABLE IF NOT EXISTS Account(
    email VARCHAR(50), 
    password CHAR(64), 
    firstname VARCHAR(20),
    lastname VARCHAR(20),
    accounttype VARCHAR(20),
    motto VARCHAR(500), 
    PRIMARY KEY (email)
);

CREATE TABLE IF NOT EXISTS Address(
    email VARCHAR(50),  
    alias VARCHAR(50),    
    address VARCHAR(200),
    city VARCHAR(20),
    state VARCHAR(20),
    PRIMARY KEY (email, alias),
    FOREIGN KEY (email) REFERENCES Account(email)
);


CREATE TABLE IF NOT EXISTS Job(
    jobid INT AUTO_INCREMENT,
    requestoremail VARCHAR(50),
    jobname VARCHAR(20), 
    jobtype VARCHAR(20), 
    jobcity VARCHAR(20),
    jobstate VARCHAR(20), 
    jobdescription VARCHAR(256),
    jobstatus VARCHAR(20),
    jobtime Timestamp, 
    jobaddress VARCHAR(50),    
    PRIMARY KEY (jobid),
    FOREIGN KEY (requestoremail) REFERENCES Account(email)
);


CREATE TABLE IF NOT EXISTS Transaction(
    jobid INT,
    acceptoremail VARCHAR(50),
    status VARCHAR(20),
    amount DOUBLE,
    note VARCHAR(200),
    transactiontime Timestamp,
    PRIMARY KEY (jobid, acceptoremail),
    FOREIGN KEY (jobid) REFERENCES Job(jobid),
    FOREIGN KEY (acceptoremail) REFERENCES Account(email)
);


CREATE TABLE IF NOT EXISTS Rate(
    jobid INT,
    requestoremail VARCHAR(50),
    rating INT,
    ratingtime Timestamp,
    comment VARCHAR(200),
    PRIMARY KEY (jobid, requestoremail),
    FOREIGN KEY (jobid) REFERENCES Job(jobid),
    FOREIGN KEY (requestoremail) REFERENCES Account(email)
);


CREATE TABLE IF NOT EXISTS Skill(
    email VARCHAR(50), 
    skillname CHAR(64), 
    status CHAR(64), 
    PRIMARY KEY (email, skillname),
    FOREIGN KEY (email) REFERENCES Account(email)
);

CREATE TABLE IF NOT EXISTS Message(
    messageid INT AUTO_INCREMENT,
    jobid INT,
    email VARCHAR(50), 
    messagetime Timestamp,
    quote VARCHAR(500),
    PRIMARY KEY (messageid),
    FOREIGN KEY (email) REFERENCES Account(email),
    FOREIGN KEY (jobid) REFERENCES Job(jobid)
);

