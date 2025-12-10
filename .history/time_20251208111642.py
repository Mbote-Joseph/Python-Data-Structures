import time

my_time = int(input("Enter the time in seconds:"))

for x in range(my_time, 0 , -1):
    seconds = x % 60
    minutes = (x - seconds) / 60
    print(f"00:{minutes}:{seconds}")
    time.sleep(1)
    
print("End !")