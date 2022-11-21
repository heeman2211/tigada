import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\t')
        time.sleep(1)
        time_sec -= 1

    print("stop")
a = int(input("Enter Seconds: "))
countdown(a)
