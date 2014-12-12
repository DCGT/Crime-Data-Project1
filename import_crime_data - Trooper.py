import psycopg2
import sys
def main():
    #Define our connection string
    conn_string = "host='localhost' dbname='postgres' user='postgres' password='postgres'"
    # print the connection string we will use to connect
    print "Connecting to database\n	->%s" % (conn_string)
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)   
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    print "Connected!\n"
    cursor.execute("CREATE TABLE crime_data (id integer,neighborhood_cluster text,neighborhood text,population_2010 integer, prop_value float,reportdat timestamp,report_month text,report_year integer,report_day text,report_time text,offense text,method text,block text, yblock float,xblock float,latitude float,longitude float);")
    cursor.execute("COPY crime_data FROM '/Users/Shared/CrimeData.csv' with delimiter as ',' csv header")
    conn.commit()
    print "crime_data table created"
if __name__ == "__main__":
    main()

