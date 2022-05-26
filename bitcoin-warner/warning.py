import requests
import json
from playsound import playsound
import time
import sys


#This function will retreive current price of bitcoin using api from coincap
#Will return current price of bitcoin in USD
def get_current_btc_price():
    parameters = {"ids" : "bitcoin"}
    response = requests.get("https://api.coincap.io/v2/assets", params=parameters).json()

    price = round(float(response["data"][0]["priceUsd"]), 2)

    return price


#This function will check input.
#If it is correct will return list where first element is difference and second element is file name
def check_input():
    arr = []
    if len(sys.argv) == 5 and sys.argv[1] == '--diff' and sys.argv[3] == '--file':
        try:
            diff = float(sys.argv[2])
            file_name = str(sys.argv[4])
        except ValueError:
            print("Error during converting data")
            sys.exit()
    else:
        print("Wrong parameters!")
        print("Example: python warning.py -time 2 -file sound.mp3")
        sys.exit()
    
    arr.append(diff)
    arr.append(file_name)
    return arr


#Main function
def main():
    inputs = check_input()
    last_price = 0.0
    while True:
        print(f"Last price was: {last_price}")
    
        price = get_current_btc_price()

        if (abs(price - last_price)) > inputs[0]:
            playsound(inputs[1])

        last_price = price
        time.sleep(10)


main()