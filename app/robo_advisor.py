# this is the "app/robo_advisor.py" file

import csv
import requests
import os
import json 

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

# INFO INPUTS

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"
response = requests.get(request_url)
#print(type(response))
#print(response.status_code)
#print(response.text)


parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]



#breakpoint()

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys())

latest_day = dates[0] #assuming latest date is first, might need to make sorting step 

latest_close = parsed_response["Time Series (Daily)"][latest_day]["4. close"]


high_prices = []
low_prices = []


for date in dates: 
    high_price = tsd[latest_day]["2. high"]
    low_price = tsd[latest_day]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)


# INFO OUTPUTS 


#csv_file_path = "data/prices.csv"
csv_file_path = os.path.join(os.path.dirname(__file__),"..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()

    writer.writerow({
        "timestamp":
        "open": 
        "high":
        "low":
        "close": 
        "volume":
    })
    writer.writerow({
        "timestamp":
        "open": 
        "high":
        "low":
        "close": 
        "volume":


print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
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


