'''3. Create a dictionary with 5 key-value pairs and then print the value of
the third key.'''
dic = {
    "sanjog": "gautam", 
    "helish": "maharjan", 
    "sarbajit": "napit", 
    "swagat": "khanal", 
    "susan": "chaudhary"
}

# The WRONG way: print(dic[3]) -> Causes KeyError
# The RIGHT way: Use the key name
print(dic["sarbajit"])
