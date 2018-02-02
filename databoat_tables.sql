
-- NAME: Emma Delucchi, Carol Joplin
-- ASSIGNMENT: Project 3
-- DATE: November 15, 2017
-- CLASS: CPSC 321
-- FILE: databoat.sql
 
-- to enforce various constraints
SET sql_mode = STRICT_ALL_TABLES;

-- start over
DROP TABLE IF EXISTS workout;
DROP TABLE IF EXISTS test;
DROP TABLE IF EXISTS pr;
DROP TABLE IF EXISTS workout_type;
DROP TABLE IF EXISTS athlete;


CREATE TABLE athlete (
   athlete_id INT NOT NULL AUTO_INCREMENT, --changed this 11/25 to auto increment
   first_name VARCHAR(255),
   last_name VARCHAR(255),
   weight DOUBLE(4,2),
   --height INT, --got rid of pr key 11/25
   team BOOLEAN,
   PRIMARY KEY (athlete_id)
) ENGINE = InnoDB;

CREATE TABLE workout_type(
    type_id INT NOT NULL AUTO_INCREMENT,
    workout_type VARCHAR(255),
    workout_name VARCHAR(255),
    length_duration TIME,
    PRIMARY KEY (type_id)
)ENGINE = InnoDB;

CREATE TABLE pr (
    pr_id INT NOT NULL,
    athlete INT NOT NULL,
    pr_2k VARCHAR(255),
    pr_6k VARCHAR(255),
    pr_10k VARCHAR(255),
    PRIMARY KEY (pr_id),
    FOREIGN KEY (athlete) REFERENCES athlete(athlete_id)
) ENGINE = InnoDB;

CREATE TABLE test(
    test_id INT NOT NULL AUTO_INCREMENT,
    athlete INT NOT NULL,
    workout_type INT, 
    pr_boolean BOOLEAN,
    test_date DATE,
    total_time TIME,
    average_split TIME,
    average_stroke_rate INT,
    percent_gold DOUBLE(2,2), --changed from INT 11/26
    PRIMARY KEY (test_id),
    FOREIGN KEY (athlete) REFERENCES athlete(athlete_id),
    FOREIGN KEY (workout_type) REFERENCES workout_type(type_id)
) ENGINE = InnoDB;

CREATE TABLE workout(
    workout_id INT NOT NULL,
    athlete INT NOT NULL,
    workout_type INT, 
    pr_boolean BOOLEAN,
    test_date DATE,
    total_time TIME,
    average_split TIME,
    average_stroke_rate INT,
    pr_delta INT,
    piece_1 TIME,
    piece_2 TIME,
    piece_3 TIME,
    piece_4 TIME,
    piece_5 TIME,
    piece_6 TIME,
    piece_7 TIME,
    piece_8 TIME,
    piece_9 TIME,
    piece_10 TIME,
    piece_11 TIME,
    piece_12 TIME,
    PRIMARY KEY (workout_id),
    FOREIGN KEY (athlete) REFERENCES athlete(athlete_id),
    FOREIGN KEY (workout_type) REFERENCES workout_type(type_id)
) ENGINE = InnoDB;

