from pymongo import MongoClient

# Establish connection to MongoDB
con = MongoClient('mongodb://localhost:27017/')  # Replace with your MongoDB URI if different

# Select the database
db = con['crud']

# Select the collection
col = db['Intern']

# Optional: Print confirmation
print("MongoDB connected successfully")