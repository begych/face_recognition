import os
import cv2
import pickle5 as pickle

with open("Data/database.pickle", "rb") as f:
    database = pickle.load(f)

data = database[0]

print(data['encodings'])