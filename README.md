# Simple_SQLAlchemy
Simple python SQLAlchemy script to pull all tables and data using a provided MySQL+PyMySQL database string. Created to assist with HackTheBox (HTB) challenge: Agile.

There are several methods online for extracting credentials from the database or querying through the hosted site, but I found myself with the database connection 
string early on and went down that path to gain further access into the machine. The script will query and print all tables and associated data in the database.

Insert your database string into the script in the place of:
"mysql+pymysql://username:password@localhost/database"

Then run the script:
Python AlchemySimp.py

