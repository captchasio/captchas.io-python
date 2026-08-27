import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from CAPTCHAsIO import CAPTCHAsIO

# in this example we store the API key inside environment variables that can be set like:
# export APIKEY_CAPTCHAsIO=1abc234de56fab7c89012d34e56fa7b8 on Linux or macOS
# set APIKEY_CAPTCHAsIO=1abc234de56fab7c89012d34e56fa7b8 on Windows
# you can just set the API key directly to it's value like:
# api_key="1abc234de56fab7c89012d34e56fa7b8"

api_key = os.getenv('APIKEY_CAPTCHAsIO', 'YOUR_API_KEY')

solver = CAPTCHAsIO(api_key)

try:
    result = solver.recaptcha(
        sitekey='6LfdxboZAAAAAMtnONIt4DJ8J1t4wMC-kVG02zIO',
        url='https://CAPTCHAsIO.com/demo/recaptcha-v3',
        action='login',
        version='v3')

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
