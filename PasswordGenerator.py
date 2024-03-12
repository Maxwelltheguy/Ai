#Programmer: Maxwell Moss
#Date: 3-12-2024
#Program: Password Generator
#Resource: https://youtu.be/jRAAaDll34Q?si=SZq8WSYzjrmuAoIA

import hashlib
import os

def hash_password(password, salt):
    hashed_password = hashlib.sha256((password + salt).encode('utf-8')).hexdigest()
    return hashed_password

# Get user input for password
password = input("Enter your password: ")

# Generate a random salt
salt = os.urandom(16).hex()

# Hash the password with the salt
hashed_password = hash_password(password, salt)

# Print the hashed password and salt
print(f"Password: {password}")
print(f"Salt: {salt}")
print(f"Hashed Password: {hashed_password}")
