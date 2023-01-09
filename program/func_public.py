from constants import RESOLUTION
from func_utils import get_ISO_times
import pandas as pd
import numpy as np
from pprint import pprint
import time


#Get relevant time periods for iso from an to
ISO_TIMES = get_ISO_times()

#Get candles recent
def get_candles_recent(client,market):

    #Define output
    close_prices = []

    #Protect API
    time.sleep(0.2)

    #Get data

    candles = client.public.get_candles(
        market= market,
        resolution = RESOLUTION,
        limit = 100
    )

    # Strucutre data
    for candle in candles.data["candles"]:
        close_prices.append(candle["close"])

    #Construct and return price series
    close_prices.reverse()
    prices_result = np.array(close_prices).astype(np.float)
    return prices_result
        
#Get candles historical
def get_candles_historical(client, market):

    #define output
    close_prices = []

    #extract historical price data for each timeframe
    for timeframe in ISO_TIMES.keys():

        #Confirm times needed
        tf_obj = ISO_TIMES[timeframe]
        from_iso = tf_obj["from_iso"]
        to_iso =tf_obj["to_iso"]

        #protect rate limits
        time.sleep(0.2)

        #get data
        candles = client.public.get_candles(
            market = market,
            resolution = RESOLUTION,
            from_iso=from_iso,
            to_iso=to_iso,
            limit=100
        )

        #Structure Data
        for candle in candles.data["candles"]:
            close_prices.append({"datetime": candle["startedAt"],market: candle["close"]})
        
    #Construct and return Dataframe
    close_prices.reverse()
    return close_prices

#Construct market prices
def construct_market_prices(client):
    
    #Declare variables
    tradeable_markets = []
    markets = client.public.get_markets()

    #Find tradeale pairs
    for market in markets.data["markets"].keys():
        market_info = markets.data["markets"][market]
        if market_info["status"] == "ONLINE" and market_info["type"] == "PERPETUAL":
            tradeable_markets.append(market)

    #Set initial Dataframe
    close_prices = get_candles_historical(client,tradeable_markets[0])

    df = pd.DataFrame(close_prices)
    df.set_index("datetime",inplace=True)
    print(df.head())

    #append other prices to Dataframe
    #You can limit the amount to loop though here to save time in development
    for market in tradeable_markets[1:]:
        close_prices_add = get_candles_historical(client,market)
        df_add = pd.DataFrame(close_prices_add)
        df_add.set_index("datetime", inplace=True)
        df = pd.merge(df,df_add, how="outer",on="datetime",copy =False)
        del df_add

    #Check any columns with NaNs
    nans = df.columns[df.isna().any()].tolist()
    if len(nans) > 0:
        print("Dropping columns: ")
        print(nans)
        df.drop(columns=nans, inplace=True)

    #Return result

    return df