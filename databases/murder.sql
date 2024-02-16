SELECT * FROM crime_scene_report WHERE city = "SQL City" and date = 20180115 and type = 'murder';

SELECT * FROM person where address_street_name = "Northwestern Dr" order by address_number;
SELECT * FROM person where (address_street_name ="Franklin Ave" and name LIKE "Annabel%");


select * FROM interview WHERE person_id = 14887 or person_id = 16371;

select * from get_fit_now_member WHERE id like "48Z%" and membership_status = "gold"; 

select * from get_fit_now_check_in where check_in_date = 20180109 and (membership_id = "48Z7A" or membership_id = "48Z55"); 

select * from drivers_license WHERE plate_number like "%H42W%";

select * from person where id = 28819 or id = 67318;

-- jeremy bowers 67318

INSERT INTO solution values (1, "Jeremy Bowers");
SELECT value from solution; 

select * from interview where person_id = 67318;

select * from drivers_license where (height > 65 and height<67) and hair_color = "red" and car_make = "Tesla" and car_model = "Model S";

SELECT * from facebook_event_checkin 
where event_name = "SQL Symphony Concert" and date > 20171201 and date < 20180101
GROUP BY person_id
HAVING COUNT(*) = 3;

select * from person where id = 24556 or id = 99716;

INSERT INTO solution values (1, "Miranda Priestly");
SELECT value from solution; 

