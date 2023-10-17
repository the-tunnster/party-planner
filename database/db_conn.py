import mysql.connector

def open_conn():
	return mysql.connector.connect(
        host="0.0.0.0",
        user="root",
        password="root_password",
        database="partyDB"
    )

