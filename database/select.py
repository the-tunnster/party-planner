import pandas

from database.db_conn import *

def load_data(table_name):
	conn = open_conn()
	cursor = conn.cursor()

	sql = f"""
			SELECT *
				FROM {table_name};
		   """
	
	cursor.execute(sql)
	data = cursor.fetchall()

	conn.close()

	column_names = [i[0] for i in cursor.description]
	dataFrame = pandas.DataFrame(data, columns=column_names)

	return (dataFrame)

def check_guest_exists(guest_name):
	conn = open_conn()
	cursor = conn.cursor()

	sql = """
			SELECT COUNT(*)
				FROM guests
					WHERE guest_name = %s;
		  """

	cursor.execute(sql, (guest_name, ))	
	data = cursor.fetchone()[0]

	conn.close()

	return (not data==0)
