import sys
import requests
import os
import math


r = requests.get("https://coreyms.com")
print(r.status_code)
print(r.ok)
