import json
import os

def checkGuestExists(guest_name):
	file_path = "data/rsvps.json"

	if not os.path.exists(file_path):
		with open(file_path, 'w') as file:
			json.dump({}, file)
		return False

	with open(file_path, "r") as file:
		guests = json.load(file)
		if not isinstance(guests, dict):
			guests = {}

	return guest_name in guests

############################################
# Insert Functions
############################################

def insertGuestData(guest_name, food_item, food_category, liquor_preference, liquor_amount, mixer_preference, mixer_amount, status):
	with open("data/rsvps.json", "r") as file:
		guests = json.load(file)
		
		guests[guest_name] = {
			"food_item": food_item,
			"food_category": food_category,
			"liquor_preference": liquor_preference,
			"liquor_amount": liquor_amount,
			"mixer_preference": mixer_preference,
			"mixer_amount": mixer_amount,
			"status": status
		}
		
	with open("data/rsvps.json", "w") as file:
		json.dump(guests, file, indent=4)

def insertFoodData(guest_name, food_item, food_category):
	with open("data/food.json", "r") as file:
		food = json.load(file)
		
		food[guest_name] = {
			"food_item": food_item,
			"food_category": food_category
		}
		
	with open("data/food.json", "w") as file:
		json.dump(food, file, indent=4)

def insertLiquorData(guest_name, liquor_preference, liquor_amount):
	with open("data/liquor.json", "r") as file:
		liquor = json.load(file)
		
		liquor[guest_name] = {
			"liquor_preference": liquor_preference,
			"liquor_amount": liquor_amount
		}
		
	with open("data/liquor.json", "w") as file:
		json.dump(liquor, file, indent=4)

def insertMixerData(guest_name, mixer_preference, mixer_amount):
	with open("data/mixers.json", "r") as file:
		mixers = json.load(file)
		
		mixers[guest_name] = {
			"mixer_preference": mixer_preference,
			"mixer_amount": mixer_amount
		}
		
	with open("data/mixers.json", "w") as file:
		json.dump(mixers, file, indent=4)

############################################
# Update Functions
############################################

def updateGuestData(guest_name, food_item, food_category, liquor_preference, liquor_amount, mixer_preference, mixer_amount, status):
	with open("data/rsvps.json", "r") as file:
		guests = json.load(file)
		
		guests[guest_name] = {
			"food_item": food_item,
			"food_category": food_category,
			"liquor_preference": liquor_preference,
			"liquor_amount": liquor_amount,
			"mixer_preference": mixer_preference,
			"mixer_amount": mixer_amount,
			"status": status
		}
		
	with open("data/rsvps.json", "w") as file:
		json.dump(guests, file, indent=4)

def updateFoodData(guest_name, food_item, food_category):
	with open("data/food.json", "r") as file:
		food = json.load(file)
		
		food[guest_name] = {
			"food_item": food_item,
			"food_category": food_category
		}
		
	with open("data/food.json", "w") as file:
		json.dump(food, file, indent=4)

def updateLiquorData(guest_name, liquor_preference, liquor_amount):
	with open("data/liquor.json", "r") as file:
		liquor = json.load(file)
		
		liquor[guest_name] = {
			"liquor_preference": liquor_preference,
			"liquor_amount": liquor_amount
		}
		
	with open("data/liquor.json", "w") as file:
		json.dump(liquor, file, indent=4)

def updateMixerData(guest_name, mixer_preference, mixer_amount):
	with open("data/mixers.json", "r") as file:
		mixers = json.load(file)
		
		mixers[guest_name] = {
			"mixer_preference": mixer_preference,
			"mixer_amount": mixer_amount
		}
		
	with open("data/mixers.json", "w") as file:
		json.dump(mixers, file, indent=4)


############################################
# Get Functions
############################################

def getGuestData(guest_name):
	if not checkGuestExists(guest_name):
		return {
			"food_item": "",
			"food_category": "",
			"liquor_preference": "none",
			"liquor_amount": 0.0,
			"mixer_preference": "none",
			"mixer_amount": 0.0,
			"status": "maybe"
		}
	
	with open("data/rsvps.json", "r") as file:
		guests = json.load(file)
		
		return guests[guest_name]