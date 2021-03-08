# robo_advisor.py

import csv
import os
import json
import string
from datetime import datetime
from dotenv import load_dotenv
import requests

load_dotenv() #this loads contents of .env file into script environment

## Description and Defining Functions

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

def ticker_symbol(inputString):
    return any(char.isdigit() for char in inputString)


#
# INFO INPUTS
#

symbol = input("Please input Stock ticker symbol (ex. MSFT): ") 
symbol = symbol.upper() #PUTS LETTERS IN UPPERCASE 


api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

requests_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

response = requests.get(requests_url)

parsed_response = json.loads(response.text)
#print(parsed_response.keys())
#print(type(parsed_response))

substring = "Error"

full_string = str(parsed_response)



try:
    if len(symbol) < 2:
        raise ValueError()
    elif len(symbol) > 5:
        raise ValueError()
    elif ticker_symbol(symbol) == True:
        raise ValueError()
    elif substring in full_string:
        raise ValueError()
except ValueError:
    print("Please enter a valid ticker symbol, like 'MSFT' or 'PTON'")
    exit()


last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys()) 

latest_day = dates[0]

latest_close = tsd[latest_day]["4. close"]


high_prices = []

low_prices = []

for date in dates:
    high_price = tsd[latest_day]["2. high"]
    low_price = tsd[latest_day]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))

# Finding max of all high prices
# Finding min of all low prices
recent_high = max(high_prices)
recent_low = min(low_prices)


#
# INFO OUTPUTS
#

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp","open","high","low","close","volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    
    # looping
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

high_contraint = float(recent_low)* 1.25

if high_contraint > float(tsd[date]["4. close"]):
    reccomendation = "Buy"
    reasoning = "The closing price has jumped by at least 25% compared to its recent low."
else:
    reccomendation = "Don't Buy"
    reasoning = "The closing price of {latest_close} has not risen by more than 25% above its recent low. We recommend not buying."
    

now = datetime.now()
dt_string = now.strftime("%m/%d/%Y, %I:%M%p")


print("-------------------------")
print(f"SELECTED SYMBOL: {symbol}")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print(f"REQUEST AT: {dt_string}") 
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print(f"RECOMMENDATION: {reccomendation}") 
print(f"RECOMMENDATION REASON: {reasoning}") 
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}") 
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


