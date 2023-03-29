import pickle5 as pickle

with open("Data/database.pickle", "rb") as f:
    database = pickle.load(f)

print(database[0])