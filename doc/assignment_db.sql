CREATE DATABASE  IF NOT EXISTS `assignment_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `assignment_db`;
-- MySQL dump 10.13  Distrib 8.0.28, for macos11 (x86_64)
--
-- Host: localhost    Database: assignment_db
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `grade`
--

DROP TABLE IF EXISTS `grade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grade` (
  `grade_id` int DEFAULT NULL,
  `assessment_mark` int DEFAULT NULL,
  `exam_mark` int DEFAULT NULL,
  `final_mark` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grade`
--

LOCK TABLES `grade` WRITE;
/*!40000 ALTER TABLE `grade` DISABLE KEYS */;
INSERT INTO `grade` VALUES (1,21,55,76),(2,17,39,56),(3,15,51,66),(4,21,42,63),(5,16,43,59),(6,18,51,69),(7,19,56,75),(8,20,60,80),(9,15,58,73),(10,19,59,78),(11,19,42,61),(12,19,60,79),(13,21,48,69),(14,16,36,52),(15,18,48,66),(16,14,38,52),(17,15,37,52),(18,14,46,60),(19,20,53,73),(20,19,41,60),(21,17,47,64),(22,19,40,59),(23,16,46,62),(24,17,53,70),(25,17,47,64),(26,18,54,72),(27,17,59,76),(28,17,43,60),(29,15,36,51),(30,16,58,74),(31,19,46,65),(32,20,39,59),(33,15,58,73),(34,19,42,61),(35,18,60,78),(36,15,55,70),(37,18,54,72),(38,17,57,74),(39,19,55,74),(40,16,44,60),(41,14,44,58),(42,20,36,56),(43,20,38,58),(44,17,58,75),(45,17,60,77),(46,20,37,57),(47,18,59,77),(48,20,44,64),(49,19,37,56),(50,20,47,67),(51,17,43,60),(52,18,51,69),(53,17,45,62),(54,15,37,52),(55,20,48,68),(56,20,46,66),(57,19,36,55),(58,16,51,67),(59,17,54,71),(60,18,46,64),(61,16,44,60),(62,20,40,60),(63,15,42,57),(64,18,39,57),(65,18,42,60),(66,14,50,64),(67,16,52,68),(68,14,48,62),(69,18,43,61),(70,17,53,70),(71,17,48,65),(72,16,59,75),(73,15,40,55),(74,14,51,65),(75,19,60,79),(76,17,55,72),(77,15,38,53),(78,20,47,67),(79,15,36,51),(80,14,50,64),(81,17,38,55),(82,18,38,56),(83,17,40,57),(84,19,37,56),(85,17,41,58),(86,14,38,52),(87,14,43,57),(88,15,57,72),(89,16,48,64),(90,16,50,66),(91,20,59,79),(92,15,58,73),(93,17,43,60),(94,15,50,65),(95,14,38,52),(96,16,41,57),(97,15,57,72),(98,15,49,64),(99,19,38,57),(100,18,35,53),(101,17,50,67),(102,19,54,73),(103,18,55,73),(104,17,51,68),(105,19,41,60),(106,20,57,77),(107,15,40,55),(108,19,41,60),(109,15,60,75),(110,20,40,60),(111,14,40,54),(112,17,40,57),(113,17,57,74),(114,19,45,64),(115,15,52,67),(116,17,48,65),(117,19,45,64),(118,14,47,61),(119,16,51,67),(120,15,46,61),(121,18,36,54),(122,14,53,67),(123,18,60,78),(124,20,55,75),(125,16,44,60),(126,16,58,74),(127,15,54,69),(128,18,48,66),(129,14,57,71),(130,15,38,53),(131,16,48,64),(132,20,44,64),(133,14,41,55),(134,17,60,77),(135,19,52,71),(136,20,42,62),(137,16,38,54),(138,15,49,64),(139,19,50,69),(140,20,49,69),(141,15,59,74),(142,14,38,52),(143,20,37,57),(144,16,56,72),(145,17,36,53),(146,14,41,55),(147,20,60,80),(148,20,39,59),(149,19,43,62),(150,15,43,58),(151,14,56,70),(152,18,60,78),(153,20,59,79),(154,20,43,63),(155,17,48,65),(156,18,51,69),(157,15,50,65),(158,14,53,67),(159,17,48,65),(160,17,57,74),(161,16,57,73),(162,16,51,67),(163,15,48,63),(164,16,38,54),(165,20,54,74),(166,14,49,63),(167,16,37,53),(168,17,50,67),(169,19,50,69),(170,17,42,59),(171,16,36,52),(172,19,58,77),(173,16,38,54),(174,18,56,74),(175,14,43,57),(176,19,54,73),(177,16,45,61),(178,17,56,73),(179,20,56,76),(180,19,45,64),(181,18,38,56),(182,15,49,64),(183,17,50,67),(184,18,36,54),(185,15,60,75),(186,20,40,60),(187,17,58,75),(188,19,42,61),(189,18,49,67);
/*!40000 ALTER TABLE `grade` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `updating_grade` BEFORE UPDATE ON `grade` FOR EACH ROW BEGIN
     insert into grade_log (grade_id,assessment_mark,exam_mark,final_mark) values(old.grade_id, old.assessment_mark, old.exam_mark, old.final_mark);
   END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `grade_log`
--

DROP TABLE IF EXISTS `grade_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grade_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `grade_id` int DEFAULT NULL,
  `assessment_mark` int DEFAULT NULL,
  `exam_mark` int DEFAULT NULL,
  `final_mark` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grade_log`
--

LOCK TABLES `grade_log` WRITE;
/*!40000 ALTER TABLE `grade_log` DISABLE KEYS */;
INSERT INTO `grade_log` VALUES (1,1,16,50,66),(2,4,18,40,58),(3,13,16,48,64),(4,4,20,40,60);
/*!40000 ALTER TABLE `grade_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `module`
--

DROP TABLE IF EXISTS `module`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `module` (
  `module_id` int NOT NULL,
  `module_name` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`module_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `module`
--

LOCK TABLES `module` WRITE;
/*!40000 ALTER TABLE `module` DISABLE KEYS */;
INSERT INTO `module` VALUES (1,'Agile Methodologies'),(2,'Computer Networks & Telecom 5'),(3,'Cyber Security'),(4,'Data Visualisation'),(5,'Data Science'),(6,'Rich Internet Applications5'),(7,'Service Oriented Architecture'),(8,'Software Design'),(9,'Database');
/*!40000 ALTER TABLE `module` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permission`
--

DROP TABLE IF EXISTS `permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `permission` (
  `permission_id` int NOT NULL,
  `url` varchar(40) DEFAULT NULL,
  `describe` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permission`
--

LOCK TABLES `permission` WRITE;
/*!40000 ALTER TABLE `permission` DISABLE KEYS */;
INSERT INTO `permission` VALUES (1,'/register','register user'),(2,'/login','login user');
/*!40000 ALTER TABLE `permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role` (
  `role_id` int NOT NULL,
  `role_type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'admin'),(2,'lecturer'),(3,'student');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role_permission`
--

DROP TABLE IF EXISTS `role_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role_permission` (
  `role_permission_id` int NOT NULL,
  `role_id` int DEFAULT NULL,
  `permission_id` int DEFAULT NULL,
  PRIMARY KEY (`role_permission_id`),
  KEY `role_id` (`role_id`),
  KEY `permission_id` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role_permission`
--

LOCK TABLES `role_permission` WRITE;
/*!40000 ALTER TABLE `role_permission` DISABLE KEYS */;
INSERT INTO `role_permission` VALUES (1,1,1),(2,1,2),(3,2,1),(4,2,2),(5,3,1),(6,3,2);
/*!40000 ALTER TABLE `role_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tus_user`
--

DROP TABLE IF EXISTS `tus_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tus_user` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) NOT NULL,
  `first_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(20) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tus_user`
--

LOCK TABLES `tus_user` WRITE;
/*!40000 ALTER TABLE `tus_user` DISABLE KEYS */;
INSERT INTO `tus_user` VALUES (1,'enda','Enda','Fallon','enda@gmail.com','enda'),(2,'jenny','Jenny','Burke','jenny@gmail.com','jenny'),(3,'david','David','Scott','david@gmail.com','david'),(4,'declan','Declan','Byrne','declan@gmail.com','declan'),(5,'mark','Mark','Daly','mark@gmail.com','mark'),(6,'michael','Michael','Russell','michael@gmail.com','michael'),(7,'brian','Brian','Lee','brian@gmail.com','brian'),(8,'jackie','Jackie','Stewart','jackie@gmail.com','jackie'),(9,'niall','Niall','Murray','niall@gmail.com','niall'),(10,'robert','Robert','Stewart','robert@gmail.com','robert'),(11,'wade','Wade','Williams','wade@gmail.com','wade'),(12,'dave','Dave','Harris','dave@gmail.com','dave'),(13,'thomas','Thomas','Robinson','thomas@gmail.com','thomas'),(14,'ivan','Ivan','Walker','ivan@gmail.com','ivan'),(15,'riley','Riley','Scott','rileyt@gmail.com','riley'),(16,'gilbert','Gilbert','Nelson','gilbertt@gmail.com','gilbert'),(17,'daisy','Daisy','Mitchell','daisy@gmail.com','daisy'),(18,'deborah','Deborah','Morgan','deborah@gmail.com','deborah'),(19,'isabel','Isabel','Cooper','isabel@gmail.com','isabel'),(20,'martin','Martin','Howard','martin@gmail.com','martin'),(21,'davis','Davis','Smith','davis@gmail.com','davis'),(22,'eli','Eli','White','eli@gmail.com','eli'),(23,'aaron','Aaron','Perry','aaron@gmail.com','aaron'),(24,'marlin','Marlin','Clark','marlin@gmail.com','marlin'),(25,'paul','Paul','Richards','paul@gmail.com','paul'),(26,'hector','Hector','Wheeler','hector@gmail.com','hector'),(27,'isabel','Isabel','Stanley','isabel@gmail.com','isabel'),(28,'stella','Stella','Holland','stella@gmail.com','stella'),(29,'alexis','Alexis','Warburton','alexis@gmail.com','alexis'),(30,'vera','Vera','Terry','vera@gmail.com','vera'),(31,'lucy','Lucy','Foster','lucy@gmail.com','lucy'),(32,'shrivardhan','Shrivardhan','Limbkar','shrivardhan@gmail.com','shrivardhan'),(35,'1','2','3','4','5');
/*!40000 ALTER TABLE `tus_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_module`
--

DROP TABLE IF EXISTS `user_module`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_module` (
  `user_module_id` int DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `module_id` int DEFAULT NULL,
  `grade_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_module`
--

LOCK TABLES `user_module` WRITE;
/*!40000 ALTER TABLE `user_module` DISABLE KEYS */;
INSERT INTO `user_module` VALUES (1,11,1,1),(2,11,2,2),(3,11,3,3),(4,11,4,4),(5,11,5,5),(6,11,6,6),(7,11,7,7),(8,11,8,8),(9,11,9,9),(10,12,1,10),(11,12,2,11),(12,12,3,12),(13,12,4,13),(14,12,5,14),(15,12,6,15),(16,12,7,16),(17,12,8,17),(18,12,9,18),(19,13,1,19),(20,13,2,20),(21,13,3,21),(22,13,4,22),(23,13,5,23),(24,13,6,24),(25,13,7,25),(26,13,8,26),(27,13,9,27),(28,14,1,28),(29,14,2,29),(30,14,3,30),(31,14,4,31),(32,14,5,32),(33,14,6,33),(34,14,7,34),(35,14,8,35),(36,14,9,36),(37,15,1,37),(38,15,2,38),(39,15,3,39),(40,15,4,40),(41,15,5,41),(42,15,6,42),(43,15,7,43),(44,15,8,44),(45,15,9,45),(46,16,1,46),(47,16,2,47),(48,16,3,48),(49,16,4,49),(50,16,5,50),(51,16,6,51),(52,16,7,52),(53,16,8,53),(54,16,9,54),(55,17,1,55),(56,17,2,56),(57,17,3,57),(58,17,4,58),(59,17,5,59),(60,17,6,60),(61,17,7,61),(62,17,8,62),(63,17,9,63),(64,18,1,64),(65,18,2,65),(66,18,3,66),(67,18,4,67),(68,18,5,68),(69,18,6,69),(70,18,7,70),(71,18,8,71),(72,18,9,72),(73,19,1,73),(74,19,2,74),(75,19,3,75),(76,19,4,76),(77,19,5,77),(78,19,6,78),(79,19,7,79),(80,19,8,80),(81,19,9,81),(82,20,1,82),(83,20,2,83),(84,20,3,84),(85,20,4,85),(86,20,5,86),(87,20,6,87),(88,20,7,88),(89,20,8,89),(90,20,9,90),(91,21,1,91),(92,21,2,92),(93,21,3,93),(94,21,4,94),(95,21,5,95),(96,21,6,96),(97,21,7,97),(98,21,8,98),(99,21,9,99),(100,22,1,100),(101,22,2,101),(102,22,3,102),(103,22,4,103),(104,22,5,104),(105,22,6,105),(106,22,7,106),(107,22,8,107),(108,22,9,108),(109,23,1,109),(110,23,2,110),(111,23,3,111),(112,23,4,112),(113,23,5,113),(114,23,6,114),(115,23,7,115),(116,23,8,116),(117,23,9,117),(118,24,1,118),(119,24,2,119),(120,24,3,120),(121,24,4,121),(122,24,5,122),(123,24,6,123),(124,24,7,124),(125,24,8,125),(126,24,9,126),(127,25,1,127),(128,25,2,128),(129,25,3,129),(130,25,4,130),(131,25,5,131),(132,25,6,132),(133,25,7,133),(134,25,8,134),(135,25,9,135),(136,26,1,136),(137,26,2,137),(138,26,3,138),(139,26,4,139),(140,26,5,140),(141,26,6,141),(142,26,7,142),(143,26,8,143),(144,26,9,144),(145,27,1,145),(146,27,2,146),(147,27,3,147),(148,27,4,148),(149,27,5,149),(150,27,6,150),(151,27,7,151),(152,27,8,152),(153,27,9,153),(154,28,1,154),(155,28,2,155),(156,28,3,156),(157,28,4,157),(158,28,5,158),(159,28,6,159),(160,28,7,160),(161,28,8,161),(162,28,9,162),(163,29,1,163),(164,29,2,164),(165,29,3,165),(166,29,4,166),(167,29,5,167),(168,29,6,168),(169,29,7,169),(170,29,8,170),(171,29,9,171),(172,30,1,172),(173,30,2,173),(174,30,3,174),(175,30,4,175),(176,30,5,176),(177,30,6,177),(178,30,7,178),(179,30,8,179),(180,30,9,180),(181,31,1,181),(182,31,2,182),(183,31,3,183),(184,31,4,184),(185,31,5,185),(186,31,6,186),(187,31,7,187),(188,31,8,188),(189,31,9,189),(190,9,1,0),(191,10,2,0),(192,7,3,0),(193,5,4,0),(194,6,5,0),(195,32,6,0),(196,8,7,0),(197,4,8,0),(198,3,9,0);
/*!40000 ALTER TABLE `user_module` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_role`
--

DROP TABLE IF EXISTS `user_role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_role` (
  `user_role_id` int NOT NULL,
  `user_id` int DEFAULT NULL,
  `role_id` int DEFAULT NULL,
  PRIMARY KEY (`user_role_id`),
  KEY `user_id` (`user_id`),
  KEY `role_id` (`role_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_role`
--

LOCK TABLES `user_role` WRITE;
/*!40000 ALTER TABLE `user_role` DISABLE KEYS */;
INSERT INTO `user_role` VALUES (1,1,1),(2,2,1),(3,3,2),(4,4,2),(5,5,2),(6,6,2),(7,7,2),(8,8,2),(9,9,2),(10,10,2),(11,11,3),(12,12,3),(13,13,3),(14,14,3),(15,15,3),(16,16,3),(17,17,3),(18,18,3),(19,19,3),(20,20,3),(21,21,3),(22,22,3),(23,23,3),(24,24,3),(25,25,3),(26,26,3),(27,27,3),(28,28,3),(29,29,3),(30,30,3),(31,31,3),(32,32,2);
/*!40000 ALTER TABLE `user_role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'assignment_db'
--

--
-- Dumping routines for database 'assignment_db'
--
/*!50003 DROP PROCEDURE IF EXISTS `selecting_user` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `selecting_user`(p_user_name text,p_password text)
BEGIN
	SELECT * FROM assignment_db.tus_user where user_name=p_user_name and password = p_password;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-05 13:45:30
