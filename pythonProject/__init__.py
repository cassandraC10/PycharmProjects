# import pyWhatKit as pyWhatKit
import pywhatkit
from pywhatkit import pyWhatKit
from pywhatkit import *

# pywhatkit.sendmsg(“receiver’s mobile number”, “message to be sent”, hours, minutes)
# pywhatkit.sendwhatmsg_to_group_instantly("Dekanorbs cohort 10", "HI, i am using python terminal to send you a message")

import pywhatkit as pwk

# using Exception Handling to avoid unexpected errors
try:
    # sending message in Whatsapp in India so using Indian dial code (+91)
    pwk.sendwhats_image("+2348102661150", "Hi, i'm using python terminal to send you a whatsapp message?", 17, 57)

    print("Message Sent!")  # Prints success message in console

    # error message
except:
    print("Error in sending the message")
