import pandas as pd
import sqlite3 as db
import functions
file_name = 'ecars.db'
connection = db.connect(file_name)
my_cursor = connection.cursor()
countries = my_cursor.execute ('select * from countries')
rows= my_cursor.fetchall()
countries_df = pd.DataFrame(rows)
functions.print_it('df from query result: ', countries_df)
#alternative way 
countries_df2 = pd.read_sql('Select * from countries', connection)
functions.print_it('df directly from query result: ', countries_df2)
