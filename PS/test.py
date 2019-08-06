import request

url = 'https://www.geniecontents.com/fortune/internal/v1/daily?targetYear=2019&targetMonth=08&targetDay=06&birthYear='
    birth = request.GET.get('birth')
    res = requests.get(url+birth)  
    print(res)
    lucky = res.get('summary')