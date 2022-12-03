import psycopg2

sqluser = 'username'
sqlpass = 'password'
dbname = 'postgres'
host = 'localhost'
port = '5432'

fd = open('migration/create_tables.sql', 'r')
create_tables = fd.read()
fd.close()

try:
    # connect to the database
    con = psycopg2.connect(dbname=dbname, user=sqluser, password=sqlpass, host=host, port=port)
    
    cursor = con.cursor()
    cursor.execute(create_tables)
    con.commit()

    print('create user_info table')
    con.close()
except:
    print("An exception occurred")
