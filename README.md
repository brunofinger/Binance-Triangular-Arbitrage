
# Triangular Arbitrage Bot

This Python script performs triangular arbitrage on the Binance cryptocurrency exchange using their API. Triangular arbitrage is a trading strategy that involves buying and selling three different currency pairs to profit from price discrepancies.

## How It Works

The script fetches the current prices of all available currency pairs and stores them in a dictionary. It then loops through all possible combinations of the three currency pairs and checks whether there is an arbitrage opportunity. If there is, the script calculates the quantities and prices for the buy and sell trades and executes them using Binance's API.

The script calculates the profit from the trades and checks whether it meets the minimum desired profit. If it does, the script exits the loop and prints the profit. Otherwise, it continues searching for another arbitrage opportunity.

## How To Use

To use this script, you will need a Binance account and API key. You will also need to install the `python-binance` package by running `pip install python-binance`.

Once you have your API key, update the `API_KEY` and `API_SECRET` variables in the script with your own values. You can also update other settings such as the currency pairs to use, the amount to trade, and the minimum desired profit.

To run the script, simply execute `python triangular_arbitrage.py` in your terminal. The script will start searching for arbitrage opportunities and will print the profit if it finds one.

## Disclaimer

This script is provided as-is and should not be used for actual trading without thorough testing and modification to fit specific requirements. The author and contributors of this script are not responsible for any losses or damages that may arise from its use.

## Conclusion

This script provides a simple example of triangular arbitrage using Python and Binance's API. By using this script as a starting point, you can customize and optimize it for your own trading needs. Happy trading!
