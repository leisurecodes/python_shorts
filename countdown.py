# Python code for Countdown Timer

import time

try:
    print()
    t = int(input("Enter Countdown(Sec): "))
    while t >= 0:
        h, r = divmod(t, 3600)
        m, s = divmod(r, 60)

        timer = f"{h:02d}:{m:02d}:{s:02d}"
        print(f"\r{timer}", end="")

        if t == 0:
            break
        time.sleep(1)
        t -= 1
    print("\nTime's Up!!")

except ValueError:
    print("\nInvalid Input!Enter valid numbr.")
except KeyboardInterrupt:
    print("\nProgram Stopped Forcefully.")
except Exception as e:
    print(f"\nUnexpected Exception: {e}")
