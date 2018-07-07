'''
    Author: Jordan Hay
    Date: 07/07/18
    Version: N/a
    Description: Testing Log Module
'''

# ------------------------------ Imports ------------------------------

import log

# ----------------------------- Functions -----------------------------

# N/a

# ---------------------------- Main Module ----------------------------

log.start() # Log program start to log.txt

if(__name__ == "__main__"):

    log.write("Main Module Started") # Write to log.txt

    try:
        x = str(input("What is your name?: "))
    except:
        print("Error Occured")
        log.error("Input Error") # Log input error to log.txt

    print(f"Hi {x}")
    log.write(f"User name is {x}") # Write to log.txt

log.end() # Log succesful program end
