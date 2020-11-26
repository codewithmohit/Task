import requests
import random

def otp(mobile):
    url = "https://www.fast2sms.com/dev/bulk"
    message=random.randint(123455,999999)
    querystring ={"authorization":"h3uDxFKQ9ti1MqAfXNgelCB0rVapwJcR4nkGI6bPSW7H28YdUjfUz93NStdEXj50lLB617vmY2IKAyMT","sender_id":"FSTSMS","message":f"{message}","language":"english","route":"p","numbers":f"{mobile}"}
    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response,message)
    return message

