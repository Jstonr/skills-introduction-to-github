import time

count = 0

while True:
    print(count, end='\r')  # Use '\r' to overwrite the previous number
    count += 1
    time.sleep(2)  # Wait for 1 second before printing the next number