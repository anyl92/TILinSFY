import requests
from decouple import config

url = 'https://www.geniecontents.com/fortune/internal/v1/daily?targetYear=2019&targetMonth=08&targetDay=06&birthYear='
birth = 1999
res = requests.get(url+str(birth))

print(res)
# lucky = res.get('summary')