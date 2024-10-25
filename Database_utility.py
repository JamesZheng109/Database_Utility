import sqlite3
#Make table
def make_table(con,tablename:str,values:dict,foreign_key:dict=None):
    '''
values format: {'ColumnName':'Additional Info (i.e data type or if column is a primary key)'}
foreign_key format:{'ColumnName':'Table being referenced'}
'''
    query=f'CREATE TABLE IF NOT EXISTS {tablename}(\n'
    for i in values.keys():
        query+=f'{i} {values[i]},\n'
    if foreign_key!=None:
        for i in foreign_key.keys():
            query+=f'FOREIGN KEY ({i}) REFERENCES {foreign_key[i]}({i}),\n'
    query=query[:-2]+');'
    cursor=con.execute(query)
#Drop table
def drop_table(con,table:str):
    cursor=con.execute(f'DROP TABLE {table};')
#Get info
def get_tables(con):
    cursor=con.execute('''SELECT name
    FROM sqlite_master
    WHERE type='table';
    ''')
    return cursor.fetchall()
def get_column(con,table:str):
    cursor=con.execute(f'''SELECT *
FROM {table};
''')
    column_names=[columns[0] for columns in cursor.description]
    return column_names
#Query
def query(con,query:str):
    cursor=con.execute(query)
    return cursor.fetchall()
def insert_query(con,query:str,values:tuple):
    cursor=con.execute(query,values)
    return cursor.fetchall()
def delete_query(con,table:str,where:str=None):
    if where==None:
        cursor=con.execute(f'''DELETE
    FROM {table};
    ''')
    elif where!=None:
        cursor=con.execute(f'''DELETE
    FROM {table}
    WHERE {where};
    ''')        
def union_query(con,query1:str,query2:str):
    query=f'''{query1} UNION {query2};'''
    cursor=con.execute(query)
    return cursor.fetchall()
def group_by_query(con,query:str,group:str):
    query=f'''{query} GROUP BY {group};'''
    cursor=con.execute(query)
    return cursor.fetchall()
def having_query(con,query:str,group:str,having:str):
    query=f'''{query} GROUP BY {group} HAVING {having};'''
    cursor=con.execute(query)
    return cursor.fetchall()
def order_by_query(con,query:str,order:str,desc=False):
    if not desc:
        query=f'''{query} ORDER BY {order} ASC;'''
    elif desc:
        query=f'''{query} ORDER BY {order} DESC;'''
    cursor=con.execute(query)
    return cursor.fetchall()
