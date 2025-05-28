CREATE DATABASE  IF NOT EXISTS `spotify_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

use spotify_db;

DROP TABLE IF EXISTS `user_playlists`;
CREATE TABLE user_playlists (
  Playlist_ID int auto_increment primary key,
  User_ID varchar(50),
  Playlist_Name text,
  Description text,
  Genre text,
  FOREIGN KEY (User_ID) REFERENCES spotify_users(User_ID)
);


INSERT INTO user_playlists (User_ID, Playlist_Name, Description, Genre)
VALUES 
  ('582003', 'Hockey Practice','Tunes for practing with the guys', 'Witchstep'),
  ('alyrocks19', 'Summer 2025', 'Summer Vibes','House'),
  ('simrinr-us', 'Driving with the Windows Down', 'Fun music to jam out to','Dance/Electronic'),
  ('lexi672177', 'Dance Playlist','Dancing with the girls','Club Dance');
  
  
