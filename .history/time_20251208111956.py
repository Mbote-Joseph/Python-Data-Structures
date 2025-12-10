import time

my_time = int(input("Enter the time in seconds:"))

for x in range(my_time, 0 , -1):
    seconds = x % 60
    minutes = ((x - seconds) / 60) % 60
    hours = ((x - seconds) / 60) - minutes 
    print(f"00:{int(minutes):02}:{seconds:02}")
    time.sleep(1)
    
print("End !")