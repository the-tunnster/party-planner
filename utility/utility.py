import pandas

def load_dataset(file_name : str):
	dataFrame = pandas.read_csv(f"data/{file_name}.csv", header=0, sep=",")
	return (dataFrame)

def check_exists(guest_name : str):
	guest_dataFrame = pandas.read_csv("data/guests.csv", header=0)

	exists = False
	for i in range(len(guest_dataFrame)):
		if guest_name == guest_dataFrame["guest_name"][i]:
			exists = True
			break
	
	return (exists)

def insert_data(file_name, args):
	dataFrame = pandas.DataFrame(args)
	dataFrame.to_csv(f"data/{file_name}.csv", mode='a', index=False, header=False)
	return (None)

import pandas as pd

def update_data(file_name, guest_name, args):
    dataFrame = pd.read_csv(f"data/{file_name}.csv", header=0, sep=",")
    row = pd.DataFrame(args, columns=dataFrame.columns)
    
    idx = dataFrame.loc[dataFrame['guest_name'] == guest_name].index
    dataFrame.loc[idx[0]] = row.iloc[0]
    dataFrame.to_csv(f"data/{file_name}.csv", mode="w", index=False)
    
    return None


