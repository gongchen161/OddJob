-- MySQL dump 10.17  Distrib 10.3.20-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: OddJob
-- ------------------------------------------------------
-- Server version	10.3.20-MariaDB-1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Account`
--

DROP TABLE IF EXISTS `Account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Account` (
  `email` varchar(50) NOT NULL,
  `password` char(64) DEFAULT NULL,
  `firstname` varchar(20) DEFAULT NULL,
  `lastname` varchar(20) DEFAULT NULL,
  `accounttype` varchar(20) DEFAULT NULL,
  `motto` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Account`
--

LOCK TABLES `Account` WRITE;
/*!40000 ALTER TABLE `Account` DISABLE KEYS */;
INSERT INTO `Account` VALUES ('dp2387@nyu.edu','cfa2a433da95914e214d2e5cb4ad49e8b5efedb7ddb5011407d146afed356a4b','Daniel','Palacios','CUSTOMER',''),('jazz.hands@gmail.com','dbd0f5ab02c8c5ca35885057524126d3e06c1303440335e4632aef385c18d83e','Miles','Davis','WORKER',''),('rob.boss@gmail.com','48b22e3a0ca4a4cddf5809ba18c200a2a3019d35a5fa76137cd7126a1075e852','Bob','Ross','WORKER',''),('scarface@gmail.com','9231979ce48ffb7791ca01e0d5e23f894c369ce4e2169a7c7b8fe90b1ef19502','Tony','Montana','CUSTOMER','');
/*!40000 ALTER TABLE `Account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Address`
--

DROP TABLE IF EXISTS `Address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Address` (
  `email` varchar(50) NOT NULL,
  `alias` varchar(50) NOT NULL,
  `address` varchar(200) DEFAULT NULL,
  `city` varchar(20) DEFAULT NULL,
  `state` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`email`,`alias`),
  CONSTRAINT `Address_ibfk_1` FOREIGN KEY (`email`) REFERENCES `Account` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Address`
--

LOCK TABLES `Address` WRITE;
/*!40000 ALTER TABLE `Address` DISABLE KEYS */;
/*!40000 ALTER TABLE `Address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Job`
--

DROP TABLE IF EXISTS `Job`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Job` (
  `jobid` int(11) NOT NULL AUTO_INCREMENT,
  `requestoremail` varchar(50) DEFAULT NULL,
  `jobname` varchar(20) DEFAULT NULL,
  `jobtype` varchar(20) DEFAULT NULL,
  `jobcity` varchar(20) DEFAULT NULL,
  `jobstate` varchar(20) DEFAULT NULL,
  `jobdescription` varchar(256) DEFAULT NULL,
  `jobstatus` varchar(20) DEFAULT NULL,
  `jobtime` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `jobaddress` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`jobid`),
  KEY `requestoremail` (`requestoremail`),
  CONSTRAINT `Job_ibfk_1` FOREIGN KEY (`requestoremail`) REFERENCES `Account` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Job`
--

LOCK TABLES `Job` WRITE;
/*!40000 ALTER TABLE `Job` DISABLE KEYS */;
INSERT INTO `Job` VALUES (1,'scarface@gmail.com','House Cleaner','House keeping','Miami','FL','Need heavy duty cleaning','COMPLETED','2019-11-21 02:11:00',NULL),(2,'dp2387@nyu.edu','Dog Walker','Baby Sitting','New York City','NY','Need someone to baby sit my dog','POSTED','2019-11-21 01:50:33',NULL),(3,'dp2387@nyu.edu','House painting','Home Improvement','New York City','NY','Need painter to paint my house','CONFIRMED','2019-11-21 02:09:58',NULL);
/*!40000 ALTER TABLE `Job` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Message`
--

DROP TABLE IF EXISTS `Message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Message` (
  `messageid` int(11) NOT NULL AUTO_INCREMENT,
  `jobid` int(11) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `messagetime` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `quote` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`messageid`),
  KEY `email` (`email`),
  KEY `jobid` (`jobid`),
  CONSTRAINT `Message_ibfk_1` FOREIGN KEY (`email`) REFERENCES `Account` (`email`),
  CONSTRAINT `Message_ibfk_2` FOREIGN KEY (`jobid`) REFERENCES `Job` (`jobid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Message`
--

LOCK TABLES `Message` WRITE;
/*!40000 ALTER TABLE `Message` DISABLE KEYS */;
INSERT INTO `Message` VALUES (1,3,'rob.boss@gmail.com','2019-11-21 02:12:57','Would you like a happy tree?');
/*!40000 ALTER TABLE `Message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Rate`
--

DROP TABLE IF EXISTS `Rate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Rate` (
  `jobid` int(11) NOT NULL,
  `requestoremail` varchar(50) NOT NULL,
  `rating` int(11) DEFAULT NULL,
  `ratingtime` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `comment` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`jobid`,`requestoremail`),
  KEY `requestoremail` (`requestoremail`),
  CONSTRAINT `Rate_ibfk_1` FOREIGN KEY (`jobid`) REFERENCES `Job` (`jobid`),
  CONSTRAINT `Rate_ibfk_2` FOREIGN KEY (`requestoremail`) REFERENCES `Account` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Rate`
--

LOCK TABLES `Rate` WRITE;
/*!40000 ALTER TABLE `Rate` DISABLE KEYS */;
INSERT INTO `Rate` VALUES (1,'scarface@gmail.com',4,'2019-11-21 02:11:53','He played very nice music');
/*!40000 ALTER TABLE `Rate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Skill`
--

DROP TABLE IF EXISTS `Skill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Skill` (
  `email` varchar(50) NOT NULL,
  `skillname` char(64) NOT NULL,
  `status` char(64) DEFAULT NULL,
  PRIMARY KEY (`email`,`skillname`),
  CONSTRAINT `Skill_ibfk_1` FOREIGN KEY (`email`) REFERENCES `Account` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Skill`
--

LOCK TABLES `Skill` WRITE;
/*!40000 ALTER TABLE `Skill` DISABLE KEYS */;
INSERT INTO `Skill` VALUES ('jazz.hands@gmail.com','Home Improvement','APPROVED'),('jazz.hands@gmail.com','House keeping','APPROVED'),('jazz.hands@gmail.com','Plumbing','APPROVED'),('rob.boss@gmail.com','Baby Sitting','APPROVED'),('rob.boss@gmail.com','Home Improvement','APPROVED'),('rob.boss@gmail.com','House keeping','APPROVED'),('rob.boss@gmail.com','Landscaping','APPROVED');
/*!40000 ALTER TABLE `Skill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Support`
--

DROP TABLE IF EXISTS `Support`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Support` (
  `supportid` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(50) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `message` varchar(200) DEFAULT NULL,
  `reply` varchar(200) DEFAULT NULL,
  `messagetime` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`supportid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Support`
--

LOCK TABLES `Support` WRITE;
/*!40000 ALTER TABLE `Support` DISABLE KEYS */;
INSERT INTO `Support` VALUES (1,'jazz.hands@gmail.com','Customer was a criminal','There was a lot to clean at Tony Montana\'s house',NULL,'2019-11-21 01:56:04','NEW');
/*!40000 ALTER TABLE `Support` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Transaction`
--

DROP TABLE IF EXISTS `Transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Transaction` (
  `jobid` int(11) NOT NULL,
  `acceptoremail` varchar(50) NOT NULL,
  `status` varchar(20) DEFAULT NULL,
  `amount` double DEFAULT NULL,
  `note` varchar(200) DEFAULT NULL,
  `transactiontime` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`jobid`,`acceptoremail`),
  KEY `acceptoremail` (`acceptoremail`),
  CONSTRAINT `Transaction_ibfk_1` FOREIGN KEY (`jobid`) REFERENCES `Job` (`jobid`),
  CONSTRAINT `Transaction_ibfk_2` FOREIGN KEY (`acceptoremail`) REFERENCES `Account` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Transaction`
--

LOCK TABLES `Transaction` WRITE;
/*!40000 ALTER TABLE `Transaction` DISABLE KEYS */;
INSERT INTO `Transaction` VALUES (1,'jazz.hands@gmail.com','COMPLETED',500,'Ya like jazz?','2019-11-21 02:11:00'),(3,'jazz.hands@gmail.com','REJECTED',100,'Jazzzz','2019-11-21 02:09:58'),(3,'rob.boss@gmail.com','CONFIRMED',150,'I can paint happy trees','2019-11-21 02:09:58');
/*!40000 ALTER TABLE `Transaction` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-20 21:14:19
