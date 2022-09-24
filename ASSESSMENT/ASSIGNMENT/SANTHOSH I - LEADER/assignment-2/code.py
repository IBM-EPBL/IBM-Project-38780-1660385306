import random
import time

while (1):
    temp = random.randint(0, 100)
    humidity = random.randint(0, 100)
    if temp>90 or humidity>90:
        print("ALERT!! Detected temperature: "+str(temp)+"°C")
        print("ALERT!! Detected humidity: "+str(humidity)+"°C")
        time.sleep(5)
    else:
        print("Normal temperature:" +str(temp)+"°C")
        print("Normal humidity:" +str(temp)+"°C")
        time.sleep(5)
