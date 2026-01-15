import time
import sys

def countdown(t):
    """
    Displays a countdown timer for a given number of seconds.
    """
    while t >= 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f"Time Remaining: {timer}", end="\r")
        time.sleep(1)
        t-=1
    print("Time Remaining: 00:00")
    print("BLAST OFF!")

seconds_input = input("Enter the countdown in seconds: ")

try:
    total_seconds = int(seconds_input)
    if total_seconds < 0:
        print("Please enter a non-negative integer.")
    else:
        countdown(total_seconds)
except ValueError:
    print("Invalid input. Please enter an integer.")