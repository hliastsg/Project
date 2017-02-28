import datetime
import urllib2
import json
import requests
import re

def PrintHeaderInfo():
    print(datetime.datetime.now())
    print("Hlias Tsiggelis")
    print("------------------------------------")
    print("Project11 gets a random beer using the API  https://punkapi.com ")
    print("and sends it via mail to a recipient using http://www.mailgun.com/")
    print("Random beer is attached as text file (beer.txt) and into main mail body")
    print("------------------------------------")
    print("Using python 2.7")
    print("------------------------------------")
    print("Prerequisite: Need to register to http://www.mailgun.com/")
    print("------------------------------------")

def get_the_random_beer():
    url = "https://api.punkapi.com/v2/beers/random"
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    the_page = response.read()
    data = json.loads(the_page)
    return data

def save_the_beer_into_file(beer):
    with open('beer.txt', 'w') as outfile:
        json.dump(beer, outfile)

def verify_email(recipient):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', recipient)
    if match == None:
        print('Bad Syntax')
        return 0
        raise ValueError('Bad Syntax')


def send_simple_message(recipient,beer):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox0a49301f99d640c6b9d5ceca8b67003a.mailgun.org/messages",
        auth=("api", "key-c0b5d2b46a1cb9b4717d5e3197963161"),
        files=[("attachment", open("beer.txt"))],
        data={"from": "Mailgun Sandbox <postmaster@sandbox0a49301f99d640c6b9d5ceca8b67003a.mailgun.org>",
              "to": recipient ,
              "subject": "Hello there from Hlias Tsiggelis",
              "text": "Hi from Hlias, this is my random beer. Bottoms Up!!!!\n\n"+ str(beer)})

if __name__ == '__main__':
        PrintHeaderInfo()
        recipient_mail = raw_input('User, please give me the recipient mail for sending the random beer...')
        if verify_email(recipient_mail) == 0:
            print("invalid email")
        else:
            random_beer = get_the_random_beer()
            save_the_beer_into_file(random_beer)
            send_simple_message(recipient_mail,random_beer)
            print("Beer was served!!!")

