import os
import time
from datetime import datetime
import requests
from dotenv import load_dotenv

from pixoo import Pixoo, SimulatorConfig

# Load .env variables
load_dotenv()


def defined_value(value, default):
    return default if value is None else value


def ping():
    response = requests.get('https://api.coingecko.com/api/v3/ping')
    return 'gecko_says' in response.json()


def retrieve_current_price():
    helius_api_getAsset = os.getenv("HELIUS_RPC_URL")
    helius_headers = {
        'Content-Type': 'application/json',
    }
    helius_body_account = {
        "jsonrpc": "2.0",
        "id": "1",
        "method": "getAsset",
        "params": {
            "id": "EKpQGSJtjMFqKZ9KQanSqYXRcF8fBopzLHYxdM65zcjm",
        }

    }
    helius_response_asset = requests.post(helius_api_getAsset, headers=helius_headers, json=helius_body_account)
    helius_response_asset.raise_for_status()
    helius_account_data = helius_response_asset.json()
    ticker = helius_account_data.get('result', {}).get('token_info', {}).get('symbol')
    price = helius_account_data.get('result', {}).get('token_info', {}).get('price_info', {}).get('price_per_token', 0)
    

    return price, ticker

def retrieve_current_price_sol():
    helius_api_getAsset = os.getenv("HELIUS_RPC_URL")
    helius_headers = {
        'Content-Type': 'application/json',
    }
    helius_body_account = {
        "jsonrpc": "2.0",
        "id": "1",
        "method": "getAsset",
        "params": {
            "id": "So11111111111111111111111111111111111111112",
        }

    }
    helius_response_asset = requests.post(helius_api_getAsset, headers=helius_headers, json=helius_body_account)
    helius_response_asset.raise_for_status()
    helius_account_data = helius_response_asset.json()
    
    sol_price = helius_account_data.get('result', {}).get('token_info', {}).get('price_info', {}).get('price_per_token', 0)
    return sol_price

def retreive_percentage():
        # token_security_api = f"https://public-api.birdeye.so/defi/token_security"
        # token_overview_api = f"https://public-api.birdeye.so/defi/token_overview"

        # # Common headers for new API
        # headers = {"X-API-KEY": "b39737e5e9c84a7697f09ce2e23ca37e"}
        # # lp_status = get_liquidity_burn_status(token_address, "de86e841-fd34-41cb-87e8-195a443d70b7")
        # # Fetch token security data


        # # Fetch token overview data
        # overview_response = requests.get(f"{token_overview_api}?address=EKpQGSJtjMFqKZ9KQanSqYXRcF8fBopzLHYxdM65zcjm", headers=headers)
        # overview_response.raise_for_status()
        # overview_data = overview_response.json()["data"]
        # # print("Overview:", overview_data)

        # price = overview_data.get("price", 0)

        # marketcap = overview_data.get("mc", 0)
        # description = overview_data.get("extensions", {}).get("description", "Unknown") if overview_data.get("extensions") else "Unknown"
        # liquidity = overview_data.get("liquidity", 0)
        # unique_wallets = overview_data.get("uniqueWallet24h", "Unknown")
        # trade_history_30 = overview_data.get("priceChange30mPercent", 0)
        # trade_history_1 = overview_data.get("priceChange1hPercent", 0)
        # trade_history_6 = overview_data.get("priceChange6hPercent", 0)
        # trade_history_24 = overview_data.get("priceChange24hPercent", 0)
        quotes_api_url = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
    
    # Headers including the API key for CoinMarketCap
        headers = {"X-CMC_PRO_API_KEY": os.getenv("CMC_API_KEY")}
        parameters = {"symbol": "wif"}
        response = requests.get(quotes_api_url, headers=headers, params=parameters)
        data = response.json().get("data", {})
        symbol_data = data.get("wif", {})
        quote_data = symbol_data.get("quote", {}).get("USD", {})
        percent_change_24h = data['WIF'][0]['quote']['USD']['percent_change_24h']
        print(percent_change_24h)
        return percent_change_24h


def main():
    print('[.] Booting..')

    if ping():
        print('[.] CoingGecko API reachable')
    else:
        print(
            '[x] CoinGecko API is not reachable. Perhaps check your internet settings')
        return

    # Verify if the ip address is set, can't default this one
    ip_address = (os.environ.get('PIXOO_IP_ADDRESS'))
    if ip_address is None:
        print('[x] Please set the `PIXOO_IP_ADDRESS` value in the .env file')
        return

    # A pleasant green color. Like a yet-to-be-ripe banano
    green = (99, 199, 77)
    red = (255, 0, 68)
    white = (255, 255, 255)

    # Retrieve some config
    timeout = int(defined_value(os.environ.get('TIMEOUT'), 30))
    # Set up a connection and show the background
    pixoo = Pixoo(ip_address, simulated=False, simulation_config=SimulatorConfig(4), debug=False, size=64)
    pixoo.draw_image('wif.png')
    # pixoo.set_brightness(100) # Only used sometimes if the screen isn't bright enough
    pixoo.draw_text('DOG', (20, 49), green)
    pixoo.draw_text('WIF', (20, 43), green)
    pixoo.draw_text('HAT', (7, 57), green)
    pixoo.push()

    print('[.] Starting update loop in 2 seconds')
    time.sleep(2)
    while True:

        # Retrieve the current price and change percentage from the coingecko API
        current_price, ticker = retrieve_current_price()
        change_percentage = 0
        # Retrieve the current F@H score from their sort-of API
        change_percentage = retreive_percentage()
        sol_price = retrieve_current_price_sol()
        # Determine the color and symbol
        if change_percentage >= 0:
            color = green
            symbol = '+'
        else:
            color = red
            symbol = ''
            

        # Place the background again first,
        # no need to clear since it's screen sized

        if color == red:
            pixoo.draw_image('wifpixeldun.png')
            pixoo.draw_text(f'hats on', (31, 13), color)
            pixoo.draw_text(f'{symbol}{change_percentage:.1f}%', (5, 13), color)
            pixoo.draw_text(f'SOL - ${sol_price:.2f}', (5, 25), white)
            
        if color == green:
            pixoo.draw_image('wif.png')
            pixoo.draw_text(f'hats cozy', (31, 13), color)
            pixoo.draw_text(f'{symbol}{change_percentage:.1f}%', (5, 13), color)
            pixoo.draw_text(f'SOL - ${sol_price:.2f}', (5, 25), white)
            
        # Draw current price
        pixoo.draw_text(f'{ticker} ${current_price:.5f}', (5, 5), color)
        
        pixoo.draw_text(f'brrr', (35, 37), white)

        # Draw current F@H stats
        localtime = datetime.now().strftime('%H:%M:%S')
        pixoo.draw_text(f'{localtime}', (33, 57), white)
        # Push to the display
        pixoo.push()

        # Wait a bit before updating everything
        time.sleep(timeout)


if __name__ == '__main__':
    main()
    
