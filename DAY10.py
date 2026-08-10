
'''PROJECTS 10'''

import random 
chars = "!@#$%^&*abcdefghijklmnopqrstuvwxyx1234567890"

password = ""
for i in range(8):
    password+=random.choice(chars)
print("GENERATED PASSWORD IS :",password)
