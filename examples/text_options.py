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

solver = CAPTCHAsIO(api_key, defaultTimeout=40, pollingInterval=10)

try:
    result = solver.text('If tomorrow is Saturday, what day is today?',
                         lang='en')

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
