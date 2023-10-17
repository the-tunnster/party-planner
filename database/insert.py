from database.db_conn import *

def insert_data_guests(guest_name, confirmed):
	conn = open_conn()
	cursor = conn.cursor()

	sql = """
			INSERT INTO guests
				VALUES (%s, %s);
		  """

	cursor.execute(sql, (guest_name, confirmed))
	conn.commit()
	conn.close()

	return (None)

def insert_data_transportation(guest_name, transportation_self, transportation_others):
	conn = open_conn()
	cursor = conn.cursor()

	sql = """
			INSERT INTO transportation
				VALUES(%s, %s, %s);
		  """
	
	cursor.execute(sql, (guest_name, transportation_self, transportation_others))
	conn.commit()
	conn.close()

	return (None)

def insert_data_food(guest_name, food_item, food_category, vegetarian):
	conn = open_conn()
	cursor = conn.cursor()

	sql = """
			INSERT INTO food
				VALUES(%s, %s, %s, %s);
		  """
	
	cursor.execute(sql, (guest_name, food_item, food_category, vegetarian))
	conn.commit()
	conn.close()

	return (None)

def insert_data_liquor(guest_name, liquor_preference, liquor_amount):
	conn = open_conn()
	cursor = conn.cursor()

	sql = """
			INSERT INTO liquor
				VALUES(%s, %s, %s);
		  """
	
	cursor.execute(sql, (guest_name, liquor_preference, liquor_amount))
	conn.commit()
	conn.close()

	return (None)

def insert_data_mixers(guest_name, mixer_preference, mixer_amount):
	conn = open_conn()
	cursor = conn.cursor()

	sql = """
			INSERT INTO mixers
				VALUES(%s, %s, %s);
		  """
	
	cursor.execute(sql, (guest_name, mixer_preference, mixer_amount))
	conn.commit()
	conn.close()

	return (None)

