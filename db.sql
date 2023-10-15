/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.4.22-MariaDB : Database - counterfiet medicine recommendation
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`counterfiet medicine recommendation` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `counterfiet medicine recommendation`;

/*Table structure for table `distributor` */

DROP TABLE IF EXISTS `distributor`;

CREATE TABLE `distributor` (
  `distributor_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`distributor_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `distributor` */

insert  into `distributor`(`distributor_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`) values (1,3,'distributor1','distributor1','kodungallur','963852741','dist1@mail'),(2,5,'distributor2','distributor2','ernakulam','3164753','dist2@mail'),(3,11,'Distributor10','Distributor10','thrissur','123456789','dist10@mail');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `feedback` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`user_id`,`feedback`,`date`) values (1,8,'vnjnvierninvkdvknv','10-12-2022'),(2,0,'2','2023-02-01'),(3,0,'2','2023-02-01'),(4,2,'bdjsdhjsksnsbs','2023-02-01');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'manu1@mail','123','manufacturer'),(3,'dist1@mail','123','distributor'),(4,'manu2@mail','123','manufacturer'),(5,'dist2@mail','123','distributor'),(6,'phar1@mail','123','pharmacy'),(7,'phar2@mail','123','pharmacy'),(8,'user1@mail','123','user'),(9,'','','pending'),(10,'amma@mail','123','pending'),(11,'dist10@mail','123','pending'),(12,'user1','user1','user'),(13,'user2','user2','user');

/*Table structure for table `manufacture` */

DROP TABLE IF EXISTS `manufacture`;

CREATE TABLE `manufacture` (
  `manufacture_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `discription` varchar(200) DEFAULT NULL,
  `image` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`manufacture_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `manufacture` */

insert  into `manufacture`(`manufacture_id`,`login_id`,`name`,`phone`,`email`,`place`,`discription`,`image`) values (1,2,'manufacturer1','741852963','manu1@mail','thrissur','descriptiondescriptiondescriptiondescription','static/678ad19d-b4b1-4bab-bc05-7de8f0c59d72w1.jpg'),(2,4,'manufacurer2','741852321','manu1@mail','edappal','descriptionhere','static/14dec814-f6a7-4bf1-9d79-c2d1a9613698w.webp'),(3,9,'','','','','','static/f5f38a09-db08-4f66-b89a-d01048eccb7b');

/*Table structure for table `medicine` */

DROP TABLE IF EXISTS `medicine`;

CREATE TABLE `medicine` (
  `medicine_id` int(11) NOT NULL AUTO_INCREMENT,
  `manufacture_id` int(11) DEFAULT NULL,
  `med_name` varchar(50) DEFAULT NULL,
  `ty` varchar(50) DEFAULT NULL,
  `a` varchar(50) DEFAULT NULL,
  `cn` varchar(50) DEFAULT NULL,
  `n` varchar(50) DEFAULT NULL,
  `ul` varchar(50) DEFAULT NULL,
  `se` varchar(50) DEFAULT NULL,
  `s` varchar(50) DEFAULT NULL,
  `ed` varchar(50) DEFAULT NULL,
  `qr_code` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`medicine_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

/*Data for the table `medicine` */

insert  into `medicine`(`medicine_id`,`manufacture_id`,`med_name`,`ty`,`a`,`cn`,`n`,`ul`,`se`,`s`,`ed`,`qr_code`) values (1,1,'Medicine1','type1','200','cn1','n1','ul1','se1','s1','2023-02-17',NULL),(2,1,'medicine2','type2','500','cn2','n2','ul2','se2','s2','2023-05-24',NULL),(3,1,'medicine3','t3','100','cn3','n3','ul3','se3','s3','2023-03-16',NULL),(4,2,'medicine4','t4','400','cn4','n4','ul4','se4','s4','2023-02-21',NULL),(5,2,'medicine5','t5','600','cn5','n5','ul5','se5','s5','2023-02-17',NULL),(6,2,'medicine6','t6','700','cn6','n6','ul6','se6','s6','2023-10-19',NULL),(7,1,'','','','','','','','','',NULL),(8,1,'dollo','qwerty','50','asdfghj','dfgdfg','grwgc','cetgcs','gewcerg','2023-02-28','static/qr_code/90af0896-022e-4e9a-8273-175c11fc6293.png'),(9,2,'Paracetamol','antipyretic drug','20','awsedrftyghuihgd','cvgbhjnh','cvhgjn','tfyjbhdxgh','rdxrdhdfv','2023-02-28','static/qr_code/a8df6781-7a0a-40c6-8cb3-2a1b46d02980.png');

/*Table structure for table `order` */

DROP TABLE IF EXISTS `order`;

CREATE TABLE `order` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_master_id` int(11) DEFAULT NULL,
  `med_id` int(11) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4;

/*Data for the table `order` */

insert  into `order`(`order_id`,`order_master_id`,`med_id`,`quantity`) values (1,1,1,'5'),(2,1,2,'6'),(3,1,3,'7'),(4,0,0,'2'),(5,2,8,'50'),(6,2,8,'5'),(7,2,8,'2'),(8,2,8,'1'),(9,2,8,'1'),(10,2,8,'1'),(11,2,8,'1'),(12,2,8,'1'),(13,2,8,'1'),(14,2,8,'1'),(15,2,8,'1'),(16,2,8,'1'),(17,2,8,'1'),(18,2,8,'1'),(19,2,8,'1');

/*Table structure for table `order_master` */

DROP TABLE IF EXISTS `order_master`;

CREATE TABLE `order_master` (
  `order_master_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `total` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`order_master_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

/*Data for the table `order_master` */

insert  into `order_master`(`order_master_id`,`user_id`,`total`,`status`,`date`) values (1,20,'0','cart','12365'),(2,2,'3450','booked','2023-02-07');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `pharmacy_id` int(11) DEFAULT NULL,
  `stock_id` int(11) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`pharmacy_id`,`stock_id`,`amount`,`date`) values (1,1,2,'1500','2023/1/1');

/*Table structure for table `payment_cart` */

DROP TABLE IF EXISTS `payment_cart`;

CREATE TABLE `payment_cart` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

/*Data for the table `payment_cart` */

insert  into `payment_cart`(`payment_id`,`user_id`,`amount`,`date`) values (1,2,'3450','2023-02-07');

/*Table structure for table `pharmacy` */

DROP TABLE IF EXISTS `pharmacy`;

CREATE TABLE `pharmacy` (
  `pharmacy_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `pharmacy_name` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `license` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`pharmacy_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `pharmacy` */

insert  into `pharmacy`(`pharmacy_id`,`login_id`,`pharmacy_name`,`place`,`city`,`email`,`phone`,`license`) values (1,6,'pharmacy1','ottapalam','palakkad','phar1@mail','74534196','753951852456'),(2,7,'pharmacy2','kadavanthra','ernakulam','phar2@mail','754219630','9635285241'),(3,10,'amma medicals','thrissur','thrissur','amma@mail','852741963','75395174185296');

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `pharmacy_id` int(11) DEFAULT NULL,
  `distributor_id` int(11) DEFAULT NULL,
  `manufacture_id` int(11) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `medicine_id` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4;

/*Data for the table `request` */

insert  into `request`(`request_id`,`pharmacy_id`,`distributor_id`,`manufacture_id`,`quantity`,`medicine_id`,`status`) values (1,1,0,1,'20',1,'4'),(2,1,0,2,'50',4,'4'),(3,1,2,1,'15',2,'send'),(4,1,1,1,'20',3,'send'),(5,1,2,1,'30',3,'4'),(6,1,1,2,'50',5,'4'),(7,1,2,2,'100',6,'4'),(8,1,2,1,'500',2,'approved'),(9,1,1,1,'100',2,'send'),(10,2,1,1,'300',2,'approved'),(11,1,1,1,'200',3,'send'),(12,1,1,1,'12345',1,'pending'),(13,1,1,1,'12345',1,'pending'),(14,1,2,1,'123455',1,'pending'),(15,1,2,2,'147852',5,'pending'),(16,2,2,2,'100000',6,'send'),(17,1,1,2,'12345',4,'send'),(18,1,1,1,'14',1,'pending'),(19,1,1,1,'12',1,'pending'),(20,1,1,1,'50',8,'send'),(21,1,1,2,'100',9,'send');

/*Table structure for table `stock` */

DROP TABLE IF EXISTS `stock`;

CREATE TABLE `stock` (
  `stock_id` int(11) NOT NULL AUTO_INCREMENT,
  `medicine_id` int(11) DEFAULT NULL,
  `manufacture_id` int(11) DEFAULT NULL,
  `distributor_id` int(11) DEFAULT NULL,
  `pharmacy_id` int(11) DEFAULT NULL,
  `stock` varchar(50) DEFAULT NULL,
  `mfg` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `qr_code` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`stock_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `stock` */

insert  into `stock`(`stock_id`,`medicine_id`,`manufacture_id`,`distributor_id`,`pharmacy_id`,`stock`,`mfg`,`date`,`qr_code`) values (1,2,1,2,1,'200','2022-12-07','2022-12-30','null'),(2,1,1,1,1,'35','2022-12-07','2022-12-30','null'),(3,9,2,1,1,'200','2023-02-01','2023-02-07','null');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `dob` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `district` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`fname`,`lname`,`dob`,`phone`,`email`,`place`,`district`) values (1,20,'aaa','aaa',NULL,NULL,NULL,NULL,NULL),(2,12,'nzv','bcc','nzv','bzc','nxv','bsnz','bz'),(3,13,'bdjs','gajs','hsjs','gsjs','bsjsn','vsjjs','bsjsn');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
