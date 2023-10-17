from database.db_conn import *

def init_setup():
	conn = open_conn()
	cursor = conn.cursor()

	initial_setup = """
	
		CREATE TABLE IF NOT EXISTS guests (
			guest_name VARCHAR(20) NOT NULL,
			confirmed VARCHAR(10) NOT NULL
		);

		CREATE TABLE IF NOT EXISTS transportation (
			guest_name VARCHAR(20) NOT NULL,
			transportation_self VARCHAR(10) NOT NULL,
			transportation_others INT NOT NULL
		);

		CREATE TABLE IF NOT EXISTS food (
			guest_name VARCHAR(20) NOT NULL,
			food_item VARCHAR(30) NOT NULL,
			food_category VARCHAR(10) NOT NULL,
			vegetarian VARCHAR(5) NOT NULL
		);

		CREATE TABLE IF NOT EXISTS liquor (
			guest_name VARCHAR(20) NOT NULL,
			liquor_preference VARCHAR(30) NOT NULL,
			liquor_amount FLOAT NOT NULL
		);

		CREATE TABLE IF NOT EXISTS mixers (
			guest_name VARCHAR(20) NOT NULL,
			mixer_preference VARCHAR(30) NOT NULL,
			mixer_amount FLOAT NOT NULL
		);
		
	"""
	cursor.execute(initial_setup)
	conn.commit()

	conn.close()
