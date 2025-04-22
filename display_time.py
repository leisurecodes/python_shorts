# Display current date and time

import time
from datetime import datetime

try:
    print()
    print("Current Date and Time: ")
    while True:
        # get current date and time
        now = datetime.now()

        # format date and time
        ct = now.strftime("%d/%m/%Y %H:%M:%S")

        # \r carriage return - overwrite line
        print(f"\r{ct}", end="")

        # wait for 1 second
        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram Stopped.")

