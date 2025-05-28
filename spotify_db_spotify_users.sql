CREATE DATABASE  IF NOT EXISTS `spotify_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `spotify_db`;
-- MySQL dump 10.13  Distrib 8.0.40, for macos14 (arm64)
--
-- Host: localhost    Database: spotify_db
-- ------------------------------------------------------
-- Server version	8.0.40


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
-- Table structure for table `spotify_users`
--

DROP TABLE IF EXISTS `spotify_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `spotify_users` (
  `ID` int,
  `User_ID` varchar(50) primary key,
  `Display_Name` text,
  `Email` text,
  `Country` text,
  `Top_Artists` text,
  `Top_Genres` text,
  `Top_Tracks` text,
  `Saved_Tracks` text,
  `Followed_Artists` text,
  `Playlists` text,
  `Audio_Features_(Danceability)` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `spotify_users`
--

LOCK TABLES `spotify_users` WRITE;
/*!40000 ALTER TABLE `spotify_users` DISABLE KEYS */;
INSERT INTO `spotify_users` VALUES ('1','582003','Alex Kowalewski','akowski30@gmail.com',NULL,'Drake, Larry June, RL Grime, Martin Garrix, G Perico','west coast hip hop, electronica, g-funk, future bass, edm, rap, progressive house, edm trap, hip hop','Jewel, Breach, Empty, No Sleep (feat. Bonn), High On Life (feat. Bonn)','Rock Ur World, Coast Is Clear (with Chance the Rapper and The Social Experiment), Make U SWEAT!, Innerbloom - What So Not Remix, 94589','ILLENIUM, Dom Dolla, D.O.D, ALLBLACK, LaRussell','millennial 2000s wednesday afternoon, Stank Shit for Anthony, Green Day Discography, Need for Speed: Most Wanted (2012), Garrix Concert Mix',''),('2','lexi672177','Lexi Borek','lexi672177@gmail.com',NULL,'Noah Kahan, Rihanna, Drake, Martin Garrix, Larry June','progressive house, rap, hip hop, edm, electronica','Orange Juice, False Confidence, A Bar Song (Tipsy), Forever, Please','light years (feat. Inéz), tv off (feat. lefty gunplay), Body Dancing, Chasing Paradise, Dear Old Friend','Music Farm, Noah Kahan','Where You Are, 21st , Good vibes , The Campfire Spinoff, Formal pre',''),('3','wlc25','wlc25','wlc25kw@gmail.com',NULL,'','','','','','',''),('4','alyrocks19','alyrocks19','alysha@advani.us',NULL,'Calvin Harris, Don Toliver, Bad Bunny, The Weeknd, Drake','reggaeton, urbano latino, latin, edm, rap, hip hop, trap latino','Thinking About You (feat. Ayah Marar), Morad: Bzrp Music Sessions, Vol. 47, Be Honest (feat. Burna Boy), Miracle (with Ellie Goulding), King','Moves Like Jagger - Studio Recording From \"The Voice\" Performance, Or What (feat. 41 & Kyle Richh) - Orchestra Mix, Under Control (feat. Hurts), Baby Don\'t Hurt Me, YOU\'RE THE ONE','','blend, PnB Rock - Unforgettable Freestyle [Remix], 735, ☀️?️??⛱️, groovy summer ?',''),('5','simrinr-us','simmy','simrinr@hotmail.com',NULL,'The Weeknd, Barry Can\'t Swim, Khruangbin, ANOTR, HUGEL','tech house, afro house, house, latin house, jazz house','Yamore, Baptized In Fear, Jolie Fille, How You Feel (Ft. Leven Kali), Les Saints','Stay, Stick-Up, Burn This House (feat. Little Boots), I Only Smoke When I Drink - Claptone Remix, Pick N Choose','Barry Can\'t Swim','KEINEMUSIK AFRO HOUSE 2025 | KEINEMUSIK Set ☁️ (Top 100), top 10, SD, ??, khabi khushi kahbie gham','');
/*!40000 ALTER TABLE `spotify_users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-02 19:31:27
