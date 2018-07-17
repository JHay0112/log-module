'''
    Author: Jordan Hay
    First Version Made: 25/06/18
    Latest Version Made: 06/07/18
    Version: 6.3.1
    
    Description:
     A really terrible python module thing that logs stuff. 

    Compatible with:
     - Python 3.6
     - Python 3.7

    Tested on:
     - Linux Mint 18.3
     - Windows 10

    What's New:
     - Formatting "error_type" efficently
     - I want to die, just kidding, that's not new
'''

# ------------------------------ Imports ------------------------------

import datetime

# ----------------------------- Functions -----------------------------

# - Return Current Time -
def ctime():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    return(now)

# - Log Program Start -
def start():
    with open("log.txt", "a") as f:
        f.write("-------- Program Started {} -------- \n".format(ctime()))
        f.write("\n")
        f.close()

# - General Log -
def write(log_message):
    with open("log.txt", "a") as f:
        f.write("{}: {} \n".format(ctime(), log_message))
        f.close()

# - Error Log -
def error(error_type):
    
    error_type = error_type.lower()
    error_type = error_type.replace(" error", "")
    error_type = error_type.capitalize()
    
    con = ""
    
    if(error_type[0].lower() in ["a", "e", "i", "o", "u"]):
        con = "An"
        if(error_type[:4].lower in ["user", "unit"]):
            con = "A"
    else:
        con = "A"
    with open("log.txt", "a") as f:
        f.write("{}: {} '{}' Error Occured \n".format(ctime(), con, error_type))   
        f.close()

# - Log Program End -
def end():
    with open("log.txt", "a") as f:
        f.write("\n")
        f.write("--------- Program Ended {} --------- \n".format(ctime()))
        f.write("\n")
        f.close()
