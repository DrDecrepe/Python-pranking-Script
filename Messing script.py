import webbrowser
import time
import random

while True:
    sites = random.choice(['google.com','youtube.com'])
    visit = "https://[]".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(5,15)
    time.sleep(seconds)




    
print ("Hello World")


