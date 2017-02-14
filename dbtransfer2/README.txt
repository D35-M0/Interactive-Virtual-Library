Setting Up the New Database:

Given: dbtransfer2 folder
Contains:
	

Step 1: SET UP NEW SCHEMA
Make a new schema where our new database will be held.

Call it seniordesign

Step 2:Add Books Table 
Run this sql script to make the new table Books for the seniordesign schema

# Script to create books table

CREATE TABLE books
(
	
book_id int ,
    
title varchar(450) default 'default_title',
    
author varchar(65) default 'default_author',
    
genres varchar(630) default 'default_genres',
    
book_length int default 0,    
    
primary key(book_id)    
);

Step 3: Run python script.
Make sure you open the script and change the variable in conn and fr to match your system.
(Basically make conn point to your DB on your machine and then make fr point to the file I am attaching called tranferFile which
contains the text version of our database)