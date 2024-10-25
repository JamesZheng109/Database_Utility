# Database_Utility
Some functions using the sqlite3 library for python
## What's available
The file has function that can do the following:
- Create a table
- Drop a table
- Get list of tables
- Return column names for specified tables
- Generic Query (Type what ever type of query you want)
- Insert Query
- Delete Query
- Union Query
- Query that includes ```GROUP BY```
- Query that includes ```HAVING```
- Query that includes ```ORDER BY```
## General Information About Functions
This section provides informations regarding parameters that will appear in multiple functins.
### All Functions Ask For This
All functions have a the parameter "con". This is where you place the ```sqlite3.connect()``` object.
```
import sqlite3
con=sqlite3.connect('Your_sqlite_file.db')
```
### Regarding Table Functions
The functions such as ```make_table()```, ```drop_table()```, ```get_tables```, ```get_column()```, and  ```delete_query()``` all a parameter that asks for a table. This is represented by the string variable ```table``` (except ```make_table()``` which is named ```tablename```).
### Regarding Query Functions
The functions such as ```query()```, ```insert_query()```, ```delete_query()```, ```union_query()```, ```group_by_query()```, ```having_query()```, and ```order_by_query()``` all have a parameter for the query. This is represented by the string variable ```query``` 
(except ```union_query()``` which has two: ```query1``` and ```query2```).
## Specific Information About Functions
This section provides a list of parameter that each function has with an explantion on what to pass into said parameter.
### make_table(con,tablename:str,values:dict,foreign_key:dict=None)
- con: Reference section "All Functions Ask For This"
- tablename: Reference section "Regarding Table Functions"
- values: dictionary with the column name as the key and the value being information such as data type or if primary key
- foregin_key: dictionary with the foregin key being the key and the value being which table is being referenced
It should be noted that the function does not account for ```UNIQUE``` keyword.

To make a table, you do the following:
```
import sqlite3
con=sqlite3.connect('Your_sqlite_file.db')

tablename="name_of_table"
values={'column1':'INT PRIMARY KEY',
        'column2':'TEXT NOT NULL'}
make_table(con,tablename,values)
```
To make a table that references another table, you do the following:
```
import sqlite3
con=sqlite3.connect('Your_sqlite_file.db')
# Table 1
tablename="name_of_table"
values={'column1':'INT PRIMARY KEY',
        'column2':'TEXT NOT NULL'}
make_table(con,tablename,values)
# Table 2
tablename2="name_of_table2"
values2={'column1':'INT PRIMARY KEY',
        'column2':'INT NOT NULL'
        'column3':'BOOL NOT NULL'}
foregin_key={'column2':tablename}
make_table(con,tablename2,values2,foregin_key)
```
