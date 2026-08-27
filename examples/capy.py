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
    result = solver.capy(
        sitekey='PUZZLE_Cz04hZLjuZRMYC3ee10C32D3uNms5w',
        url='https://www.mysite.com/page/captcha/',
        api_server="https://jp.api.capy.me/",
    )

except Exception as e:
    sys.exit(e)

else:
    sys.exit('result: ' + str(result))
