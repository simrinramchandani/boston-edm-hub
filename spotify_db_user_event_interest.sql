CREATE DATABASE  IF NOT EXISTS `spotify_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
use spotify_db;

DROP TABLE IF EXISTS `user_event_interest`;
CREATE TABLE user_event_interest (
  User_ID varchar(50),
  Event_ID int,
  Interest_Type text check (Interest_Type IN ('viewed', 'interested', 'attending')),
  Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (User_ID, Event_ID),
  FOREIGN KEY (User_ID) REFERENCES spotify_users(User_ID),
  FOREIGN KEY (Event_ID) REFERENCES ticketmaster_events(Event_ID)
);

INSERT INTO user_event_interest (User_ID, Event_ID, Interest_Type) VALUES
('582003', 12, 'viewed'),
('alyrocks19', 45, 'interested'),
('simrinr-us', 67, 'attending'),
('lexi672177', 3, 'viewed');
