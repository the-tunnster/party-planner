from database import cursor

def load_data(table_name):
	query = f"SELECT * from {table_name};"
	cursor.execute(query)
	data = cursor.fetchall()
	return (data)

def check_guest_exists(guest_name, cursor):
	query = f"""SELECT * FROM guests
				WHERE guest_name = {guest_name};"""
	
	cursor.execute(query)
	data = cursor.fetchall()

	if len(data) > 0:
		return True
	
	return False

def insert_data_guests(cursor, guest_name, status):
	query = f"""
			INSERT INTO guests
				VALUES({guest_name}, {status});
			"""
	cursor.execute(query)
	return (None)

def insert_data_transportation(cursor, guest_name, transportation_self, transportation_others):
	query = f"""
			INSERT INTO transportation
				VALUES({guest_name}, {transportation_self}, {transportation_others});
			"""
	cursor.execute(query)
	return (None)

def insert_data_food(cursor, guest_name, food_item, food_category, vegetarian):
	query = f"""
			INSERT INTO food
				VALUES({guest_name}, {food_item}, {food_category}, {vegetarian});
			"""
	cursor.execute(query)
	return (None)

def insert_data_liquor(cursor, guest_name, liquor_preference, liquor_amount):
	query = f"""
			INSERT INTO liquor
				VALUES({guest_name}, {liquor_preference}, {liquor_amount});
			"""
	cursor.execute(query)
	return (None)

def insert_data_mixers(cursor, guest_name, mixer_preference, mixer_amount):
	query = f"""
			INSERT INTO liquor
				VALUES({guest_name}, {mixer_preference}, {mixer_amount});
			"""
	cursor.execute(query)
	return (None)

def update_data(file_name, guest_name, args):
    dataFrame = pd.read_csv(f"data/{file_name}.csv", header=0, sep=",")
    row = pd.DataFrame(args, columns=dataFrame.columns)
    
    idx = dataFrame.loc[dataFrame['guest_name'] == guest_name].index
    dataFrame.loc[idx[0]] = row.iloc[0]
    dataFrame.to_csv(f"data/{file_name}.csv", mode="w", index=False)
    
    return None


