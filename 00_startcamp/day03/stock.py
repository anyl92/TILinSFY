from iexfinance.stocks import Stock

company = Stock('TSLA', token = '')

print(company.get_price())
print(company.get_quote())

# 1. 스크래핑 2. API 3. 패키지