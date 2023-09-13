import mysql.connector as sql
from mysql.connector.errors import Error
import pandas as pd

def connection_open():

    try:
        connection,mycursor = mysql('root',"root","localhost","bizcard")
        return connection,mycursor
    except:
        e = mysql('roo',"root","localhost","bizcard")
        print("Error is ",e)

# Create a MySQL connection

def mysql(username,password,host,databasename):
    db_username = username
    db_password =password
    db_host = host
    db_name = databasename
    try:
        connection = sql.connect(
            host=db_host,
            database=db_name,
            user=db_username,
            password=db_password
        )
        mycursor = connection.cursor(buffered=True)
        print("connected")
        return connection,mycursor
    except Error as e:
        return e

# closing the connections

def closing_connection(connection,mycursor):
    mycursor = mycursor 
    connection = connection
    mycursor.close()
    connection.close()
    print("sql connection is closed")
  


def upload(df):
    df = df
    try:
        connection,mycursor = connection_open()
        values =  tuple(df["Value"])
        query = """insert into bizcard.card values (%s,%s,%s,%s,%s,%s,%s,%s)"""
        mycursor.execute(query,values)
        connection.commit()
        closing_connection(mycursor,connection)
        return 1
    except:
        closing_connection(mycursor,connection)
        return 0


def creating_dim_tables():
    connection,mycursor = connection_open()
    try:
        query_year = """create table card (
                        compamy_mame varchar(20) primary key,
                        cardholder_name varchar(20),
                        designation varchar(20),
                        mobile_number varchar(20),
                        email varchar(20),
                        WebsiteURL varchar(20),
                        state varchar(20),
                        pincode int
                        )"""
        
        mycursor.execute(query_year)
       
    except Error as e:
        print("error is",e)

    closing_connection(mycursor,connection)



def retrival():
    try:
            
        connection,mycursor = connection_open()
        query = """select * from bizcard.card"""
        mycursor.execute(query)

        # Fetch the results
        result = mycursor.fetchall()
        
        column_names = [desc[0] for desc in mycursor.description]
        
        df = pd.DataFrame(result,columns=column_names)

        closing_connection(connection,mycursor)
        return df
    except:
        closing_connection(connection,mycursor)