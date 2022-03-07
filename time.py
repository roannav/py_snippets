# Module time
import time 

print(dir(time))

# print everything in time module, one per line
for i in dir(time):
    print(i)

print(time)         # <module 'time' (built-in)>
print(time.time)    # <built-in function time>

#time.time()  # Returns current time (in seconds).
              # Useful for reporting elapsed time.

print(f"Start time: {time.time()}")
time.sleep(3.5)  # pause for 3.5 seconds
print(f"  End time: {time.time()}")

print(time.asctime())  # 'Thu May 11 11:40:19 2017' 
