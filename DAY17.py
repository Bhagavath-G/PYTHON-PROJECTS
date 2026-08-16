'''PROJECT 17'''

import random
username = input("Enter your username:")
vibes = ["its_","attitudeboy_","why_not","crazy_","your_"]
for i in range(5):
    print(username + random.choice(vibes) + str(random.randint(5,15)))
