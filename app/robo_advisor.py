# this is the "app/robo_advisor.py" file

import csv
import json 
import os

from dotenv import load_dotenv
import requests




load_dotenv() #this loads contents of .env file into script environment

# DEFINE FUNCTIONS 

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

def ticker_numbers(inputString):
    return any(char.isdigit() for char in inputString)





### INFO INPUTS

api_key = os.environ.get("ALPHANTAGE_API_KEY")

symbol = "MSFT"#input("Please enter the stock symbol (ex. MSFT): ") 
symbol = symbol.upper() #puts letts in upper case


request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}IBM&apikey={api_key}"

response = requests.get(request_url)

parsed_response = json.loads(response.text)
print(parsed_response.keys())
substring = "Error"
full_string = str(parsed_response)

#last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

#tsd = parsed_response["Time Series (Daily)"]



try:
    if len(symbol) < 3:
        raise ValueError()
    elif len(symbol) > 5:
        raise ValueError()
    elif ticker_numbers(symbol) == True:
        raise ValueError()
except ValueError:
    print("That ticker symbol is invalid. Please enter the correct symbol: ")
    exit()






dates = list(tsd.keys())

latest_day = dates[0] #assuming latest date is first, might need to make sorting step 

latest_close = tsd[latest_day]["4. close"]


high_prices = []
low_prices = []


for date in dates: 
    high_price = tsd[latest_day]["2. high"]
    low_price = tsd[latest_day]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)


### INFO OUTPUTS 


csv_file_path = os.path.join(os.path.dirname(__file__),"..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"]
        }) 


now = datetime.now()
date_time_str = now.strftime("%B %d, %Y %H: %M")      
   


print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: {date_time_str}")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}")
print("HAPPY INVESTING!")
print("-------------------------")


