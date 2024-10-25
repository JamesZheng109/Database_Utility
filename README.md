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
```python
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
```python
import sqlite3
con=sqlite3.connect('Your_sqlite_file.db')

tablename="name_of_table"
values={'column1':'INT PRIMARY KEY',
        'column2':'TEXT NOT NULL'}
make_table(con,tablename,values)
```
To make a table that references another table, you do the following:
```python
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
### drop_table(con,table:str)
- con: Reference section "All Functions Ask For This"
- table: Reference section "Regarding Table Functions"

To drop a table, you do the following:
```python
import sqlite3
con=sqlite3.connect('Your_sqlite_file.db')
table="name_of_table"
drop_table(con,table)
```
### get_tables(con)
- con: Reference section "All Functions Ask For This"

To get a list of tables in the .db file, you do this:
```python
import sqlite3
con=sqlite3.connect('Your_sqlite_file.db')
get_tables(con)
```
### get_column(con,table:str)
- con: Reference section "All Functions Ask For This"
- table: Reference section "Regarding Table Functions"

To get the column names of a specific table, you do the following:
```python
import sqlite3
con=sqlite3.connect('Your_sqlite_file.db')
table="name_of_table"
get_column(con,table)
```
### query(con,query:str)
- con: Reference section "All Functions Ask For This"
- query: Reference section "Regarding Query Functions"

For this function, you can do any query you want for this one, so here is an example of a ```SELECT``` query:
```python
import sqlite3
con=sqlite3.connect('Your_sqlite_file.db')
query='''
      SELECT *
      FROM name_of_table
      '''
query(con,query)
```
### insert_query(con,query:str,values:tuple)
- con: Reference section "All Functions Ask For This"
- query: Reference section "Regarding Query Functions"
- values: Information that will be inserted into the table

To do an insert query, you do the following:
```python
import sqlite3
con=sqlite3.connect('Your_sqlite_file.db')
query='''
      INSERT INTO name_of_table(column1,column2)
      VALUE(?,?)
      '''
values=(0,"Some Text Here")
cursor=con.cursor()
cursor.execute(query,values)
```
### delete_query(con,table:str,where:str=None)
- con: Reference section "All Functions Ask For This"
- table: Reference section "Regarding Table Functions"
- where: If one wants to remove a sepecfic column(s)

To delete a table, you do the following:
```python
import sqlite3
con=sqlite3.connect('Your_sqlite_file.db')
table="name_of_table"
delete_query(con,table)
```
To delete a specific column(s), you do the following:
```python
import sqlite3
con=sqlite3.connect('Your_sqlite_file.db')
table="name_of_table"
where='''column2="something"'''
delete_query(con,table,where)
```
### union_query(con,query1:str,query2:str)
- con: Reference section "All Functions Ask For This"
- query1 & query2: Reference section "Regarding Query Functions"

To do a union query, you do the following:
```python
import sqlite3
con=sqlite3.connect('Your_sqlite_file.db')
query1='''
       SELECT column1
       FROM name_of_table
       WHERE column1=0
       '''
query2='''
       SELECT column1
       FROM name_of_table
       WHERE column1=1
       '''
union_query(con,query1,query2)
```
### group_by_query(con,query:str,group:str)
- con: Reference section "All Functions Ask For This"
- query: Reference section "Regarding Query Functions"
- group: What the query will be grouped by

To do a query with a ```GROUP BY```, you do the following:
```python
import sqlite3
con=sqlite3.connect('Your_sqlite_file.db')
query='''
      SELECT column1
      FROM name_of_table
      WHERE column1 BETWEEN 0 AND 1
      '''
group=column2
group_by_query(con,query,group)
```
### having_query(con,query:str,group:str,having:str)
- con: Reference section "All Functions Ask For This"
- query: Reference section "Regarding Query Functions"
- group: What the query will be grouped by
- having: What ```HAVING``` condition

To use a query with ```HAVING```, you do the following:
```python
import sqlite3
con=sqlite3.connect('Your_sqlite_file.db')
query='''
      SELECT column1, COUNT(column2) AS 'Count'
      FROM name_of_table
      WHERE column2 > 0
      '''
group=column2
having='''COUNT(column2)>0'''
having_query(con,query,group,having)
```
### order_by_query(con,query:str,order:str,desc=False)
- con: Reference section "All Functions Ask For This"
- query: Reference section "Regarding Query Functions"
- order: The query will be organized base on the specified column
- desc: Whether the query will be in ascending (FALSE) or decending order (TRUE)

To do a query with ```ORDER BY``` in ascending order, you do the following:
```python
import sqlite3
con=sqlite3.connect('Your_sqlite_file.db')
query='''
      SELECT column2
      FROM name_of_table
      '''
order='''column2'''
desc=FALSE
order_by_query(con,query,order,desc)
```
To do a query with ```ORDER BY``` in decending order, you do the following:
```python
import sqlite3
con=sqlite3.connect('Your_sqlite_file.db')
query='''
      SELECT column2
      FROM name_of_table
      '''
order='''column2'''
desc=TRUE
order_by_query(con,query,order,desc)
```
