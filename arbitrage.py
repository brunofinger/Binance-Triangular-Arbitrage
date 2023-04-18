from binance.client import Client
from binance.enums import *
import time

api_key = 'your API key here'
api_secret = 'your API secret here'

client = Client(api_key, api_secret)

# Settings
symbols = ['ETHBTC', 'BNBBTC', 'ETHBNB']  # The 3 currency pairs for arbitrage
trade_amount = 0.1  # The amount of each currency to trade
min_profit = 0.005  # The minimum desired profit for each trade
sleep_time = 2  # The time in seconds to wait between trades

# Fetch the prices of the currency pairs
prices = client.get_all_tickers()
symbol_prices = {}
for price in prices:
    symbol_prices[price['symbol']] = float(price['price'])

# Calculate the arbitrage opportunities
for i in range(len(symbols)):
    for j in range(len(symbols)):
        if i == j:
            continue
        for k in range(len(symbols)):
            if i == k or j == k:
                continue
            symbol1 = symbols[i]
            symbol2 = symbols[j]
            symbol3 = symbols[k]
            if symbol_prices[symbol1] * symbol_prices[symbol2] * symbol_prices[symbol3] > 1:
                # Arbitrage opportunity found
                print(f'Arbitrage opportunity: {symbol1} -> {symbol2} -> {symbol3}')

                # Calculate the quantities and prices for the buy and sell trades
                quantity1 = trade_amount / symbol_prices[symbol1]
                quantity2 = quantity1 / symbol_prices[symbol2]
                quantity3 = quantity2 * symbol_prices[symbol3]
                if quantity3 > trade_amount:
                    # Execute the buy and sell trades
                    print('Executing trades...')
                    order1 = client.create_order(
                        symbol=symbol1,
                        side=SIDE_SELL,
                        type=ORDER_TYPE_MARKET,
                        quantity=quantity1)
                    time.sleep(sleep_time)
                    order2 = client.create_order(
                        symbol=symbol2,
                        side=SIDE_BUY,
                        type=ORDER_TYPE_MARKET,
                        quantity=quantity2)
                    time.sleep(sleep_time)
                    order3 = client.create_order(
                        symbol=symbol3,
                        side=SIDE_BUY,
                        type=ORDER_TYPE_MARKET,
                        quantity=trade_amount)
                    time.sleep(sleep_time)
                    order4 = client.create_order(
                        symbol=symbol1,
                        side=SIDE_BUY,
                        type=ORDER_TYPE_MARKET,
                        quantity=quantity1)
                    time.sleep(sleep_time)
                    profit = (quantity3 * symbol_prices[symbol1]) - trade_amount
                    print(f'Profit: {profit:.8f} {symbol1}')
                    if profit >= min_profit:
                        # Profit is sufficient, break out of the loop
                        print('Sufficient profit, exiting...')
                        break
            else:
                # No arbitrage opportunity found
                pass
