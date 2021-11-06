import json


username = input("what is your name?")


filename = 'username.json'
with open(filename,'w') as f:
    json.dump(username,f)
    print(f"we will remember your name when you back,{username}!")