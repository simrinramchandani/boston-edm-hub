use spotify_db;

select * from edm_Artists;
select * from spotify_users;
select * from ticketmaster_events;
select * from user_playlists;
select * from user_event_interest;


-- 1. Recommend events based on a user's top artists, playlist genres, or previous interests
-- case 1: user (alyrocks19)

SELECT DISTINCT su.Display_Name, e.Event, e.Date, e.Venue, e.Artist, e.Subgenre
FROM spotify_users su
LEFT JOIN user_event_interest uei ON su.User_ID = uei.User_ID
LEFT JOIN user_playlists up ON su.User_ID = up.User_ID
JOIN ticketmaster_events e 
  ON INSTR(su.Top_Artists, e.Artist) > 0 
     OR INSTR(e.Subgenre, up.Genre) > 0
     OR uei.Event_ID = e.Event_ID
WHERE su.User_ID = 'alyrocks19'
ORDER BY e.Date;


-- case 2: user (simrinr-us)
SELECT DISTINCT su.Display_Name, e.Event, e.Date, e.Venue, e.Artist, e.Subgenre
FROM spotify_users su
LEFT JOIN user_event_interest uei ON su.User_ID = uei.User_ID
LEFT JOIN user_playlists up ON su.User_ID = up.User_ID
JOIN ticketmaster_events e 
  ON INSTR(su.Top_Artists, e.Artist) > 0 
     OR INSTR(e.Subgenre, up.Genre) > 0
     OR uei.Event_ID = e.Event_ID
WHERE su.User_ID = 'simrinr-us'
ORDER BY e.Date;


-- 2. Find the most active venues for EDM events
SELECT Venue, COUNT(*) AS Total_Events
FROM ticketmaster_events
GROUP BY Venue
ORDER BY Total_Events DESC
LIMIT 5;


-- Most active venues, limited to events users have viewed, saved, or attended
SELECT e.Venue, COUNT(*) AS Total_Interested_Events
FROM ticketmaster_events e
JOIN user_event_interest uei ON e.Event_ID = uei.Event_ID
GROUP BY e.Venue
ORDER BY Total_Interested_Events DESC
LIMIT 5;


-- 3. What are the most popular subgenres based on events users interacted with?
SELECT e.Subgenre, COUNT(*) AS Interested_Event_Count
FROM ticketmaster_events e
JOIN user_event_interest uei ON e.Event_ID = uei.Event_ID
GROUP BY e.Subgenre
ORDER BY Interested_Event_Count DESC;


-- 4. Find the cheapest EDM events happening this month
SELECT Event, Artist, Venue, Date, Median_Ticket_Price_$
FROM ticketmaster_events
WHERE MONTH(Date) = MONTH(CURDATE())
  AND YEAR(Date) = YEAR(CURDATE())
  AND Median_Ticket_Price_$ IS NOT NULL
ORDER BY Median_Ticket_Price_$ ASC
LIMIT 5;


-- 5. Recommend artists based on shared genre with user's top genres
SELECT DISTINCT a.Artist, a.Subgenre
FROM edm_artists a
JOIN spotify_users su ON INSTR(su.Top_Genres, a.Subgenre) > 0
WHERE su.User_ID = '582003';


-- 6. Get average ticket prices by subgenre
SELECT Subgenre, ROUND(AVG(Median_Ticket_Price_$), 2) AS Avg_Ticket_Price
FROM ticketmaster_events
WHERE Median_Ticket_Price_$ IS NOT NULL
GROUP BY Subgenre
ORDER BY Avg_Ticket_Price;


-- 7. Show cities with the most upcoming EDM events
SELECT City, COUNT(*) AS Event_Count
FROM ticketmaster_events
GROUP BY City
ORDER BY Event_Count DESC;


-- 8. What are the top cities with the most events that users interacted with?
SELECT e.City, COUNT(*) AS Interested_Event_Count
FROM ticketmaster_events e
JOIN user_event_interest uei ON e.Event_ID = uei.Event_ID
GROUP BY e.City
ORDER BY Interested_Event_Count DESC;



