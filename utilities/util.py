import json

def getConfig(config_name:str):
	with open(f"configs/{config_name}.json") as config:
		return json.load(config)
