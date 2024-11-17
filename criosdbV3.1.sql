-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: criosdb
-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (2,'pbkdf2_sha256$870000$R7a2adOd5v3qJGE76hbm0u$XvHrURD24jSy8DnBkNSctZuvmpHYmZeJEQ7l5qzHJi4=','2024-11-17 06:14:32.435954',1,'maxim','','','maximo_ferrarotti@hotmail.com',1,1,'2024-08-29 17:38:46.693918'),(11,'pbkdf2_sha256$870000$I7o51Ju3sv2Nj1RnvYraLM$yu1UM2dNr6x9qQ2lvbeCqaytMX5sCq0oJIdzMKNh8UE=','2024-10-17 19:46:03.626301',0,'willy','','','rojaswilfredo754@gmail.com',0,1,'2024-10-17 19:19:03.448166'),(12,'pbkdf2_sha256$870000$IeAx80besEcAG16yjdztUY$bqb3MQyR/qzpp1llOBiCBZtsSN4AbCSycZKj/7e/f0Y=',NULL,0,'maxim2','','','maximo.ferrarotti1@gmail.com',0,1,'2024-10-17 19:46:53.568664'),(14,'pbkdf2_sha256$870000$5hrg7hxvZO1fDyxu03K3nl$9Fl6Wt65INfgQHwFQc+33pM+ifiURO+rx9ZrK8Xs9U4=','2024-10-18 17:48:35.537450',0,'maximo','','','maximo.ferrarotti@gmail.com',0,1,'2024-10-18 17:43:44.326435');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `campos_estudios`
--

DROP TABLE IF EXISTS `campos_estudios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `campos_estudios` (
  `Id_CampoEstudio` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`Id_CampoEstudio`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `campos_estudios`
--

LOCK TABLES `campos_estudios` WRITE;
/*!40000 ALTER TABLE `campos_estudios` DISABLE KEYS */;
INSERT INTO `campos_estudios` VALUES (1,'Formación General'),(2,'Formación Específica'),(3,'Formación Profesional de Personas');
/*!40000 ALTER TABLE `campos_estudios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carreras`
--

DROP TABLE IF EXISTS `carreras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carreras` (
  `Id_Carrera` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(200) NOT NULL,
  `Descripcion` varchar(200) DEFAULT 'No agregada',
  PRIMARY KEY (`Id_Carrera`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carreras`
--

LOCK TABLES `carreras` WRITE;
/*!40000 ALTER TABLE `carreras` DISABLE KEYS */;
INSERT INTO `carreras` VALUES (1,'CRIOS - PROFESORADO DE EDUCACIÓN ESPECIAL CON ORIENTACIÓN EN SORDOS E HIPOACÚSICOS','Compuesto por Materias, Talleres, Trabajo Campo y Seminario-Taller');
/*!40000 ALTER TABLE `carreras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `correlativas_cursar`
--

DROP TABLE IF EXISTS `correlativas_cursar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `correlativas_cursar` (
  `Id_CorrelativaCursar` int NOT NULL AUTO_INCREMENT,
  `Id_Materia_CC` int DEFAULT NULL,
  `Descripcion` varchar(200) DEFAULT 'No agregada',
  PRIMARY KEY (`Id_CorrelativaCursar`),
  KEY `Id_Materia_idx` (`Id_Materia_CC`),
  CONSTRAINT `Id_Materia_CC` FOREIGN KEY (`Id_Materia_CC`) REFERENCES `materias` (`Id_Materia`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `correlativas_cursar`
--

LOCK TABLES `correlativas_cursar` WRITE;
/*!40000 ALTER TABLE `correlativas_cursar` DISABLE KEYS */;
/*!40000 ALTER TABLE `correlativas_cursar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `correlativas_rendir`
--

DROP TABLE IF EXISTS `correlativas_rendir`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `correlativas_rendir` (
  `Id_CorrelativaRendir` int NOT NULL AUTO_INCREMENT,
  `Id_Materia_CR` int DEFAULT NULL,
  `Descripcion` varchar(200) DEFAULT 'No agregada',
  PRIMARY KEY (`Id_CorrelativaRendir`),
  KEY `Id_Materia_CR_idx` (`Id_Materia_CR`),
  CONSTRAINT `Id_Materia_CR` FOREIGN KEY (`Id_Materia_CR`) REFERENCES `materias` (`Id_Materia`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `correlativas_rendir`
--

LOCK TABLES `correlativas_rendir` WRITE;
/*!40000 ALTER TABLE `correlativas_rendir` DISABLE KEYS */;
/*!40000 ALTER TABLE `correlativas_rendir` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cuotas`
--

DROP TABLE IF EXISTS `cuotas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cuotas` (
  `Id_Cuota` int NOT NULL AUTO_INCREMENT,
  `Mes_Cuota` varchar(45) NOT NULL,
  `Monto` float(9,2) NOT NULL,
  `Fecha_Vencimiento` date DEFAULT '1900-01-01',
  PRIMARY KEY (`Id_Cuota`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cuotas`
--

LOCK TABLES `cuotas` WRITE;
/*!40000 ALTER TABLE `cuotas` DISABLE KEYS */;
/*!40000 ALTER TABLE `cuotas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dat_insc`
--

DROP TABLE IF EXISTS `dat_insc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dat_insc` (
  `Id_DatInsc` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(200) NOT NULL,
  `Apellido` varchar(200) NOT NULL,
  `Fecha_Nac` date NOT NULL,
  `Provincia` varchar(45) NOT NULL,
  `DNI` varchar(10) NOT NULL,
  `Edad` char(2) NOT NULL,
  `Domicilio` varchar(200) NOT NULL,
  `Telefono_Fijo` varchar(12) DEFAULT 'No agregado',
  `Celular_Nro` varchar(12) NOT NULL,
  `Email` varchar(200) DEFAULT 'No agregado',
  `Estado_Civil` varchar(45) NOT NULL,
  `Hijos` int DEFAULT '0',
  `Lugar_Trabajo` varchar(200) DEFAULT 'No agregado',
  `Tel_Emergencia` varchar(12) NOT NULL,
  `Col_Egreso` varchar(200) NOT NULL,
  `Titulo` varchar(200) DEFAULT NULL,
  `Otro_Titulo` varchar(200) DEFAULT 'No agregado',
  `Anio_Egreso` char(4) DEFAULT '----',
  `Preg_1` int DEFAULT '0',
  `Resp_1` varchar(200) DEFAULT 'Sin responder',
  `Resp_2` int DEFAULT NULL,
  `Preg_2` varchar(200) DEFAULT 'Sin responder',
  `Matricula` int DEFAULT '0',
  `Legajo_Fisico` int DEFAULT '0',
  `Inscripto` int DEFAULT '0',
  PRIMARY KEY (`Id_DatInsc`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dat_insc`
--

LOCK TABLES `dat_insc` WRITE;
/*!40000 ALTER TABLE `dat_insc` DISABLE KEYS */;
INSERT INTO `dat_insc` VALUES (6,'Maximo Leon','Ferrarotti','2004-08-04','Salta','4969097450','32','Mi casa','','03876144010','maximo_ferrarotti@hotmail.com','Soltero/a',NULL,'','03876144010','Benita Campos','','','2022',NULL,NULL,NULL,NULL,1,0,1),(7,'Wilfredo','Rojas','2024-10-09','Salta','45863172','21','domicilio 2','','12453','','Soltero/a',NULL,'','68468386','colegio 2','','','2021',NULL,NULL,NULL,NULL,0,0,1),(9,'Exequiel','Martinez','2003-05-03','Salta','45863172','21','domicilio 2','','12453','','Soltero/a',NULL,'','5346467','colegio 2','','','2021',NULL,NULL,NULL,NULL,0,0,0),(10,'Juan','Amaya','2004-06-05','Salta','46636755','20','casa 3','','21255','','Soltero/a',NULL,'','643746','Escuela 2','','','2020',NULL,NULL,NULL,NULL,0,0,1);
/*!40000 ALTER TABLE `dat_insc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-09-26 06:15:07.963881','5','carlos',3,'',4,2),(2,'2024-09-26 06:15:07.964881','4','juan',3,'',4,2),(3,'2024-09-26 06:15:07.964881','3','pedro',3,'',4,2),(4,'2024-09-26 06:15:07.964881','1','tilin',3,'',4,2),(5,'2024-09-26 06:15:07.964881','6','user',3,'',4,2),(6,'2024-10-17 19:12:38.808145','9','willy',3,'',4,2),(7,'2024-10-17 19:12:38.808145','8','juan',3,'',4,2),(8,'2024-10-17 19:18:44.282186','10','willy',3,'',4,2),(9,'2024-10-17 19:20:59.111027','7','useradmin',3,'',4,2),(10,'2024-10-18 04:38:09.703741','13','exequiel',1,'[{\"added\": {}}]',4,2),(11,'2024-10-18 04:48:10.356674','13','exequiel',3,'',4,2);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-08-22 17:23:44.586528'),(2,'auth','0001_initial','2024-08-22 17:23:45.301941'),(3,'admin','0001_initial','2024-08-22 17:23:45.461952'),(4,'admin','0002_logentry_remove_auto_add','2024-08-22 17:23:45.469460'),(5,'admin','0003_logentry_add_action_flag_choices','2024-08-22 17:23:45.491064'),(6,'contenttypes','0002_remove_content_type_name','2024-08-22 17:23:45.575034'),(7,'auth','0002_alter_permission_name_max_length','2024-08-22 17:23:45.649423'),(8,'auth','0003_alter_user_email_max_length','2024-08-22 17:23:45.668455'),(9,'auth','0004_alter_user_username_opts','2024-08-22 17:23:45.676457'),(10,'auth','0005_alter_user_last_login_null','2024-08-22 17:23:45.737154'),(11,'auth','0006_require_contenttypes_0002','2024-08-22 17:23:45.740156'),(12,'auth','0007_alter_validators_add_error_messages','2024-08-22 17:23:45.746662'),(13,'auth','0008_alter_user_username_max_length','2024-08-22 17:23:45.845682'),(14,'auth','0009_alter_user_last_name_max_length','2024-08-22 17:23:45.916520'),(15,'auth','0010_alter_group_name_max_length','2024-08-22 17:23:45.933748'),(16,'auth','0011_update_proxy_permissions','2024-08-22 17:23:45.940759'),(17,'auth','0012_alter_user_first_name_max_length','2024-08-22 17:23:46.012325'),(18,'sessions','0001_initial','2024-08-22 17:23:46.049829');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1g87p0cgim8k2uho5j82nqge7re17s9a','.eJxVjEEOwiAQRe_C2hDAgQGX7j0DYQaQqmmT0q6Md7dNutDte-__t4hpXVpce5njkMVFGHH6ZZT4WcZd5Eca75PkaVzmgeSeyMN2eZtyeV2P9u-gpd62NTEFMuhsriF7D2hcIdDEWmlGa7xKqMB6YLCBTYDsHQJW3Hg9hyA-X9eWNwI:1sww0w:zbhjeJAesCCmN-YYd8K_mE8xMIorsreaTZK0XuZJR3I','2024-10-19 04:03:30.321606'),('769hladeooryhsyqtxsqyrog9jxpyzbh','.eJxVjEEOwiAQRe_C2hDAgQGX7j0DYQaQqmmT0q6Md7dNutDte-__t4hpXVpce5njkMVFGHH6ZZT4WcZd5Eca75PkaVzmgeSeyMN2eZtyeV2P9u-gpd62NTEFMuhsriF7D2hcIdDEWmlGa7xKqMB6YLCBTYDsHQJW3Hg9hyA-X9eWNwI:1swZKr:InpaomdsPyrstF8Si7fhDvqpUDY2geuRfQ2R9sgwwSI','2024-10-18 03:50:33.812603'),('f6ngk3v3uspmh2cxqcp59utt6jllojp9','.eJxVjEEOwiAQRe_C2hDAgQGX7j0DYQaQqmmT0q6Md7dNutDte-__t4hpXVpce5njkMVFGHH6ZZT4WcZd5Eca75PkaVzmgeSeyMN2eZtyeV2P9u-gpd62NTEFMuhsriF7D2hcIdDEWmlGa7xKqMB6YLCBTYDsHQJW3Hg9hyA-X9eWNwI:1slYae:d0rmJfWJMWKIMSkmdh8j_hyqbpgApXl1rxE3p7Jo5EY','2024-09-17 18:49:20.427478'),('gmpvgjs3c9ohozz81bbhdo9awqxdel2q','.eJxVjEEOwiAQRe_C2hDAgQGX7j0DYQaQqmmT0q6Md7dNutDte-__t4hpXVpce5njkMVFGHH6ZZT4WcZd5Eca75PkaVzmgeSeyMN2eZtyeV2P9u-gpd62NTEFMuhsriF7D2hcIdDEWmlGa7xKqMB6YLCBTYDsHQJW3Hg9hyA-X9eWNwI:1sk6e9:FeFZLcZvQj47swIffpi8DiO3EJDTACtvDUuPQrNQXU8','2024-09-13 18:46:57.569887'),('hiz7e8qs9ybnznpdpr8e3plz67wtrftt','.eJxVjEEOwiAQRe_C2hDAgQGX7j0DYQaQqmmT0q6Md7dNutDte-__t4hpXVpce5njkMVFGHH6ZZT4WcZd5Eca75PkaVzmgeSeyMN2eZtyeV2P9u-gpd62NTEFMuhsriF7D2hcIdDEWmlGa7xKqMB6YLCBTYDsHQJW3Hg9hyA-X9eWNwI:1t3Kw3:7RgP5BckjyBdxrGKmPs0SwdPQeFD2tBTT87CBTlh8h8','2024-11-05 19:52:55.056672'),('hr460xs5vsmysgc3siwvvkb2ghvdku94','.eJxVjEEOwiAQRe_C2hDAgQGX7j0DYQaQqmmT0q6Md7dNutDte-__t4hpXVpce5njkMVFGHH6ZZT4WcZd5Eca75PkaVzmgeSeyMN2eZtyeV2P9u-gpd62NTEFMuhsriF7D2hcIdDEWmlGa7xKqMB6YLCBTYDsHQJW3Hg9hyA-X9eWNwI:1tCYYK:g8BXEV2DYI01Zui-CiMgYKyGazTs_jiFuLjdJIkJ60U','2024-12-01 06:14:32.446010'),('lciihhf99s5j51iya9fio7zrl9yq3suu','.eJxVjEEOwiAQRe_C2hDAgQGX7j0DYQaQqmmT0q6Md7dNutDte-__t4hpXVpce5njkMVFGHH6ZZT4WcZd5Eca75PkaVzmgeSeyMN2eZtyeV2P9u-gpd62NTEFMuhsriF7D2hcIdDEWmlGa7xKqMB6YLCBTYDsHQJW3Hg9hyA-X9eWNwI:1sjj7J:YZ1dQrAFZaVOpwHQWU3HP4v1rIuTttynXf2edlipVb4','2024-09-12 17:39:29.328110'),('rv8t21c7j3kr5xgbn4aqzcoaemxltb6v','.eJxVjEEOwiAQRe_C2hDAgQGX7j0DYQaQqmmT0q6Md7dNutDte-__t4hpXVpce5njkMVFGHH6ZZT4WcZd5Eca75PkaVzmgeSeyMN2eZtyeV2P9u-gpd62NTEFMuhsriF7D2hcIdDEWmlGa7xKqMB6YLCBTYDsHQJW3Hg9hyA-X9eWNwI:1t974k:bMPO8qfbXqxk8y8yACFPaUsDzuSPQhSQlztJoXQTT7E','2024-11-21 18:17:46.069258'),('sik4hnf8pu3b7y8nbc5h8ysz5urqnae9','.eJxVjEEOwiAQRe_C2hDAgQGX7j0DYQaQqmmT0q6Md7dNutDte-__t4hpXVpce5njkMVFGHH6ZZT4WcZd5Eca75PkaVzmgeSeyMN2eZtyeV2P9u-gpd62NTEFMuhsriF7D2hcIdDEWmlGa7xKqMB6YLCBTYDsHQJW3Hg9hyA-X9eWNwI:1sx5kS:8OPCM-D2p-pKdEkLO_LjNq4xRVLDcdS95Glt4GwWWks','2024-10-19 14:27:08.275591'),('y2nwgv2p6km9xyn8w5vr8ewnwit2asel','.eJxVjEEOwiAQRe_C2hDAgQGX7j0DYQaQqmmT0q6Md7dNutDte-__t4hpXVpce5njkMVFGHH6ZZT4WcZd5Eca75PkaVzmgeSeyMN2eZtyeV2P9u-gpd62NTEFMuhsriF7D2hcIdDEWmlGa7xKqMB6YLCBTYDsHQJW3Hg9hyA-X9eWNwI:1syCwb:KvGVvnnIGDvqZRbriDdYbwSc3aGoZFgatkr5W5ghqrk','2024-10-22 16:20:17.546325');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empleados`
--

DROP TABLE IF EXISTS `empleados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleados` (
  `Id_Empleado` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(200) NOT NULL,
  `Apellido` varchar(200) NOT NULL,
  `DNI` bigint NOT NULL,
  `Telefono` varchar(12) NOT NULL,
  `Email` varchar(45) NOT NULL,
  PRIMARY KEY (`Id_Empleado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleados`
--

LOCK TABLES `empleados` WRITE;
/*!40000 ALTER TABLE `empleados` DISABLE KEYS */;
/*!40000 ALTER TABLE `empleados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estados_cuotas`
--

DROP TABLE IF EXISTS `estados_cuotas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estados_cuotas` (
  `Id_EstadoCuota` int NOT NULL AUTO_INCREMENT,
  `Id_PagCuot_EC` int DEFAULT NULL,
  `Vigencia_Cuota` tinyint NOT NULL,
  PRIMARY KEY (`Id_EstadoCuota`),
  KEY `Id_PagCuot_EC_idx` (`Id_PagCuot_EC`),
  CONSTRAINT `Id_PagCuot_EC` FOREIGN KEY (`Id_PagCuot_EC`) REFERENCES `pagos_cuotas` (`Id_PagCuot`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estados_cuotas`
--

LOCK TABLES `estados_cuotas` WRITE;
/*!40000 ALTER TABLE `estados_cuotas` DISABLE KEYS */;
/*!40000 ALTER TABLE `estados_cuotas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estados_curriculares`
--

DROP TABLE IF EXISTS `estados_curriculares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estados_curriculares` (
  `Id_EstadoCurricular` int NOT NULL AUTO_INCREMENT,
  `Id_MatXPlan_EstCur` int DEFAULT NULL,
  `Id_Estudiante_EstCur` int DEFAULT NULL,
  `Condicion_Nota` varchar(45) DEFAULT NULL,
  `Nota` int DEFAULT NULL,
  `Fecha_Finalizacion` date NOT NULL,
  `Folio` varchar(45) DEFAULT 'Sin especificar',
  PRIMARY KEY (`Id_EstadoCurricular`),
  KEY `Id_MatXPlan_EstCur_idx` (`Id_MatXPlan_EstCur`),
  KEY `Id_Estudiante_EstCur_idx` (`Id_Estudiante_EstCur`),
  CONSTRAINT `Id_Estudiante_EstCur` FOREIGN KEY (`Id_Estudiante_EstCur`) REFERENCES `estudiantes` (`Id_Estudiante`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Id_MatXPlan_EstCur` FOREIGN KEY (`Id_MatXPlan_EstCur`) REFERENCES `materiasxplanes_estudios` (`Id_MatXPlan`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estados_curriculares`
--

LOCK TABLES `estados_curriculares` WRITE;
/*!40000 ALTER TABLE `estados_curriculares` DISABLE KEYS */;
/*!40000 ALTER TABLE `estados_curriculares` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estudiantes`
--

DROP TABLE IF EXISTS `estudiantes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estudiantes` (
  `Id_Estudiante` int NOT NULL AUTO_INCREMENT,
  `Id_DatInsc` int DEFAULT NULL,
  `Anio_Insc` tinyint NOT NULL,
  `Nro_Legajo` varchar(45) DEFAULT 'No especificado',
  `Legajo_Digital` varchar(200) DEFAULT 'No adjuntado',
  PRIMARY KEY (`Id_Estudiante`),
  KEY `Id_DatInsc_idx` (`Id_DatInsc`),
  CONSTRAINT `Id_DatInsc` FOREIGN KEY (`Id_DatInsc`) REFERENCES `dat_insc` (`Id_DatInsc`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estudiantes`
--

LOCK TABLES `estudiantes` WRITE;
/*!40000 ALTER TABLE `estudiantes` DISABLE KEYS */;
INSERT INTO `estudiantes` VALUES (5,10,2,'F52952',NULL),(6,6,2,'F52954',NULL),(7,7,3,'F45892',NULL);
/*!40000 ALTER TABLE `estudiantes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `insc_carreras`
--

DROP TABLE IF EXISTS `insc_carreras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `insc_carreras` (
  `Id_InscCarrera` int NOT NULL AUTO_INCREMENT,
  `Id_Estudiante_IC` int DEFAULT NULL,
  `Id_Carrera_IC` int DEFAULT NULL,
  `Id_Empleado_IC` int DEFAULT NULL,
  `Fecha_Insc` date NOT NULL,
  PRIMARY KEY (`Id_InscCarrera`),
  KEY `Id_Empleado_idx` (`Id_Empleado_IC`),
  KEY `Id_Carrera_IC_idx` (`Id_Estudiante_IC`),
  KEY `Id_Carrera_IC_idx1` (`Id_Carrera_IC`),
  CONSTRAINT `Id_Carrera_IC` FOREIGN KEY (`Id_Carrera_IC`) REFERENCES `carreras` (`Id_Carrera`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Id_Empleado_IC` FOREIGN KEY (`Id_Empleado_IC`) REFERENCES `empleados` (`Id_Empleado`) ON UPDATE CASCADE,
  CONSTRAINT `Id_Estudiante_IC` FOREIGN KEY (`Id_Estudiante_IC`) REFERENCES `estudiantes` (`Id_Estudiante`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `insc_carreras`
--

LOCK TABLES `insc_carreras` WRITE;
/*!40000 ALTER TABLE `insc_carreras` DISABLE KEYS */;
INSERT INTO `insc_carreras` VALUES (1,5,1,NULL,'2024-11-16'),(3,6,1,NULL,'2024-11-16'),(4,7,1,NULL,'2024-11-16');
/*!40000 ALTER TABLE `insc_carreras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `insc_examenes`
--

DROP TABLE IF EXISTS `insc_examenes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `insc_examenes` (
  `Id_InscExamen` int NOT NULL AUTO_INCREMENT,
  `Id_MesaExamen` int DEFAULT NULL,
  `Id_Estudiante_IE` int DEFAULT NULL,
  `Id_EstadoCuota_IE` int DEFAULT NULL,
  `Id_Empleado_IE` int DEFAULT NULL,
  PRIMARY KEY (`Id_InscExamen`),
  KEY `Id_Estudiante_IE_idx` (`Id_Estudiante_IE`),
  KEY `Id_EstadoCuota_IE_idx` (`Id_EstadoCuota_IE`),
  KEY `Id_Empleado_IE_idx` (`Id_Empleado_IE`),
  KEY `Id_MesaExamen_idx` (`Id_MesaExamen`),
  CONSTRAINT `Id_Empleado_IE` FOREIGN KEY (`Id_Empleado_IE`) REFERENCES `empleados` (`Id_Empleado`) ON UPDATE CASCADE,
  CONSTRAINT `Id_EstadoCuota_IE` FOREIGN KEY (`Id_EstadoCuota_IE`) REFERENCES `estados_cuotas` (`Id_EstadoCuota`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Id_Estudiante_IE` FOREIGN KEY (`Id_Estudiante_IE`) REFERENCES `estudiantes` (`Id_Estudiante`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Id_MesaExamen` FOREIGN KEY (`Id_MesaExamen`) REFERENCES `mesas_examenes` (`Id_MesaExamen`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `insc_examenes`
--

LOCK TABLES `insc_examenes` WRITE;
/*!40000 ALTER TABLE `insc_examenes` DISABLE KEYS */;
/*!40000 ALTER TABLE `insc_examenes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materias`
--

DROP TABLE IF EXISTS `materias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materias` (
  `Id_Materia` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(200) NOT NULL,
  `Id_Unidad` int DEFAULT NULL,
  `Cuatrimestral/Anual` tinyint DEFAULT '0',
  `Correlatividad` tinyint DEFAULT '0',
  PRIMARY KEY (`Id_Materia`),
  KEY `Id_Unidad_idx` (`Id_Unidad`),
  CONSTRAINT `Id_Unidad` FOREIGN KEY (`Id_Unidad`) REFERENCES `tipos_unidades` (`Id_Unidad`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materias`
--

LOCK TABLES `materias` WRITE;
/*!40000 ALTER TABLE `materias` DISABLE KEYS */;
INSERT INTO `materias` VALUES (1,'Pedagogia',1,0,0),(2,'Lectura y Escritura Académica',2,0,0),(3,'Didáctica General',1,0,0),(4,'Historia Argentina y Latinoamericana',1,0,0),(5,'Educacion Especial: Perspectiva y Estado Actual',1,0,0),(6,'Bases Neuropsicobiológicas del Aprendizaje',1,0,0),(7,'Sujeto de la Educación Especial',1,0,0),(8,'Comunicación y Lenguaje',1,0,0),(9,'Expresión Dramática y Comunicación',1,0,0),(10,'Práctica Doc I - Contexto, Comunidad y Escuela',3,0,0),(11,'Métodos y Técnicas de Indagación',2,0,0),(12,'Instituciones Educativas',4,0,0),(13,'Lengua de señas I',2,0,0);
/*!40000 ALTER TABLE `materias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materiasxplanes_estudios`
--

DROP TABLE IF EXISTS `materiasxplanes_estudios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materiasxplanes_estudios` (
  `Id_MatXPlan` int NOT NULL AUTO_INCREMENT,
  `Id_PlanEstudio` int DEFAULT NULL,
  `Id_CampoEstudio` int DEFAULT NULL,
  `Id_Materia` int DEFAULT NULL,
  `Anio_Materia` tinyint NOT NULL,
  PRIMARY KEY (`Id_MatXPlan`),
  KEY `Id_PlanEstudio_idx` (`Id_PlanEstudio`),
  KEY `Id_Materia_idx` (`Id_Materia`),
  KEY `Id_CampoEstudio_idx` (`Id_CampoEstudio`),
  CONSTRAINT `Id_CampoEstudio` FOREIGN KEY (`Id_CampoEstudio`) REFERENCES `campos_estudios` (`Id_CampoEstudio`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Id_Materia` FOREIGN KEY (`Id_Materia`) REFERENCES `materias` (`Id_Materia`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Id_PlanEstudio` FOREIGN KEY (`Id_PlanEstudio`) REFERENCES `planes_estudios` (`Id_PlanEstudio`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materiasxplanes_estudios`
--

LOCK TABLES `materiasxplanes_estudios` WRITE;
/*!40000 ALTER TABLE `materiasxplanes_estudios` DISABLE KEYS */;
INSERT INTO `materiasxplanes_estudios` VALUES (1,1,1,1,0),(2,1,1,2,0),(3,1,1,3,0),(4,1,1,4,0),(5,1,2,5,0),(6,1,2,6,0),(7,1,2,7,0),(8,1,2,8,0),(9,1,2,9,0),(10,1,3,10,0),(11,1,3,11,0),(12,1,3,12,0),(13,1,2,13,0);
/*!40000 ALTER TABLE `materiasxplanes_estudios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mesas_examenes`
--

DROP TABLE IF EXISTS `mesas_examenes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mesas_examenes` (
  `Id_MesaExamen` int NOT NULL,
  `Id_MatXPlan_ME` int DEFAULT NULL,
  `Fecha_Examen` date NOT NULL DEFAULT '1900-01-01',
  `Hora_Examen` time DEFAULT NULL,
  PRIMARY KEY (`Id_MesaExamen`),
  KEY `ID_idx` (`Id_MatXPlan_ME`),
  CONSTRAINT `Id_MatXPlan_ME` FOREIGN KEY (`Id_MatXPlan_ME`) REFERENCES `materiasxplanes_estudios` (`Id_MatXPlan`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mesas_examenes`
--

LOCK TABLES `mesas_examenes` WRITE;
/*!40000 ALTER TABLE `mesas_examenes` DISABLE KEYS */;
/*!40000 ALTER TABLE `mesas_examenes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagos_cuotas`
--

DROP TABLE IF EXISTS `pagos_cuotas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagos_cuotas` (
  `Id_PagCuot` int NOT NULL AUTO_INCREMENT,
  `Id_Cuota_PG` int DEFAULT NULL,
  `Id_Estudiante_PG` int DEFAULT NULL,
  `Fecha_Pago` date NOT NULL,
  `Monto` float(9,2) NOT NULL,
  `Condicion_Pago` tinyint NOT NULL DEFAULT '0',
  PRIMARY KEY (`Id_PagCuot`),
  KEY `Id_Cuota_PG_idx` (`Id_Cuota_PG`),
  KEY `Id_Estudiante_idx` (`Id_Estudiante_PG`),
  CONSTRAINT `Id_Cuota_PG` FOREIGN KEY (`Id_Cuota_PG`) REFERENCES `cuotas` (`Id_Cuota`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Id_Estudiante` FOREIGN KEY (`Id_Estudiante_PG`) REFERENCES `estudiantes` (`Id_Estudiante`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagos_cuotas`
--

LOCK TABLES `pagos_cuotas` WRITE;
/*!40000 ALTER TABLE `pagos_cuotas` DISABLE KEYS */;
/*!40000 ALTER TABLE `pagos_cuotas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `planes_estudios`
--

DROP TABLE IF EXISTS `planes_estudios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `planes_estudios` (
  `Id_PlanEstudio` int NOT NULL AUTO_INCREMENT,
  `Id_Carrera` int DEFAULT NULL,
  `Anio_Plan` year NOT NULL,
  `Descripcion` varchar(200) DEFAULT 'No agregada',
  PRIMARY KEY (`Id_PlanEstudio`),
  KEY `Id_Carrera_idx` (`Id_Carrera`),
  CONSTRAINT `Id_Carrera` FOREIGN KEY (`Id_Carrera`) REFERENCES `carreras` (`Id_Carrera`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `planes_estudios`
--

LOCK TABLES `planes_estudios` WRITE;
/*!40000 ALTER TABLE `planes_estudios` DISABLE KEYS */;
INSERT INTO `planes_estudios` VALUES (1,1,0000,'Plan de Estudio 2022');
/*!40000 ALTER TABLE `planes_estudios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipos_unidades`
--

DROP TABLE IF EXISTS `tipos_unidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipos_unidades` (
  `Id_Unidad` int NOT NULL AUTO_INCREMENT,
  `Tipo` varchar(200) NOT NULL,
  PRIMARY KEY (`Id_Unidad`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipos_unidades`
--

LOCK TABLES `tipos_unidades` WRITE;
/*!40000 ALTER TABLE `tipos_unidades` DISABLE KEYS */;
INSERT INTO `tipos_unidades` VALUES (1,'Materia'),(2,'Taller'),(3,'Trabajo Campo'),(4,'Seminario -Taller');
/*!40000 ALTER TABLE `tipos_unidades` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-17  3:41:18
