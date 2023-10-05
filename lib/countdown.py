# your code goes here!
import time  # Import the time module for sleep in countdown_with_sleep

# Function to perform a countdown without sleep
def countdown(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
    print("HAPPY NEW YEAR!")

# Function to perform a countdown with sleep
def countdown_with_sleep(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        time.sleep(1)  # Sleep for 1 second
        number -= 1
    print("HAPPY NEW YEAR!")

# Test your functions here if needed
# countdown(10)  # Uncomment to test the countdown function
# countdown_with_sleep(10)  # Uncomment to test the countdown_with_sleep function

