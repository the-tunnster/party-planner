from database.db_conn import *

def delete_data_guests(guest_name):
	conn = open_conn()
	cursor = conn.cursor()

	sql = """
			DELETE FROM guests
				WHERE guest_name = %s;
		  """
	
	cursor.execute(sql, (guest_name,))
	conn.commit()
	conn.close()

	return (None)

def delete_data_transportation(guest_name):
	conn = open_conn()
	cursor = conn.cursor()

	sql = """
			DELETE FROM transportation
				WHERE guest_name = %s;
		  """
	
	cursor.execute(sql, (guest_name,))
	conn.commit()
	conn.close()

	return (None)

def delete_data_food(guest_name):
	conn = open_conn()
	cursor = conn.cursor()

	sql = """
			DELETE FROM food
				WHERE guest_name = %s;
		  """
	
	cursor.execute(sql, (guest_name,))
	conn.commit()
	conn.close()

	return (None)

def delete_data_liquor(guest_name):
	conn = open_conn()
	cursor = conn.cursor()

	sql = """
			DELETE FROM liquor
				WHERE guest_name = %s;
		  """
	
	cursor.execute(sql, (guest_name,))
	conn.commit()
	conn.close()

	return (None)

def delete_data_mixers(guest_name):
	conn = open_conn()
	cursor = conn.cursor()

	sql = """
			DELETE FROM mixers
				WHERE guest_name = %s;
		  """
	
	cursor.execute(sql, (guest_name,))
	conn.commit()
	conn.close()

	return (None)
