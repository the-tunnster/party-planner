from database.db_conn import *

def update_data_guests(guest_name, confirmed):
	conn = open_conn()
	cursor = conn.cursor()

	sql = """
			UPDATE guests
				SET guest_name = %s,
					confirmed = %s
						WHERE guest_name = %s;
		  """

	cursor.execute(sql, (guest_name, confirmed, guest_name))
	conn.commit()
	conn.close()

	return (None)

def update_data_transportation(guest_name, transportation_self, transportation_others):
	conn = open_conn()
	cursor = conn.cursor()

	sql = """
			UPDATE transportation
				SET guest_name = %s,
					transportation_self = %s,
					transportation_others = %s
						WHERE guest_name = %s;
		  """
	
	cursor.execute(sql, (guest_name, transportation_self, transportation_others, guest_name))
	conn.commit()
	conn.close()

	return (None)

def update_data_food(guest_name, food_item, food_category, vegetarian):
	conn = open_conn()
	cursor = conn.cursor()

	sql = """
			UPDATE food
				SET guest_name = %s,
					food_item = %s,
					food_category = %s,
					vegetarian = %s
						WHERE guest_name = %s;
		  """
	
	cursor.execute(sql, (guest_name, food_item, food_category, vegetarian, guest_name))
	conn.commit()
	conn.close()

	return (None)

def update_data_liquor(guest_name, liquor_preference, liquor_amount):
	conn = open_conn()
	cursor = conn.cursor()

	sql = """
			UPDATE liquor
				SET guest_name = %s,
					liquor_preference = %s,
					liquor_amount = %s
						WHERE guest_name = %s;
		  """
	
	cursor.execute(sql, (guest_name, liquor_preference, liquor_amount, guest_name))
	conn.commit()
	conn.close()

	return (None)

def update_data_mixers(guest_name, mixer_preference, mixer_amount):
	conn = open_conn()
	cursor = conn.cursor()

	sql = """
			UPDATE mixers
				SET guest_name = %s,
					mixer_preference = %s,
					mixer_amount = %s
						WHERE guest_name = %s;
		  """
	
	cursor.execute(sql, (guest_name, mixer_preference, mixer_amount, guest_name))
	conn.commit()
	conn.close()

	return (None)
