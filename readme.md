# Getting Started Guide for Setting Up API Keys with Your Application

This guide will help new users obtain and set up the necessary API keys from CoinMarketCap (CMC) and Helius to use with the provided Python script. This script is designed to fetch cryptocurrency prices and their 24-hour percentage change using these services.

## Step 1: Obtaining API Keys

### CoinMarketCap (CMC) API Key

1. **Create an Account:**
   - Visit [CoinMarketCap](https://coinmarketcap.com/api/) and sign up for an account if you don't already have one.
2. **Get the API Key:**
   - Once logged in, navigate to the API section and select a plan that suits your needs. The basic plan should suffice for getting started.
   - After selecting your plan, you will be provided with an API key. This key is required for making requests to CoinMarketCap's API.

### Helius API Key

- **Create an Account:**
   - https://dev.helius.xyz/dashboard/app
   - Sign up for an account if you don't already have one.
- **Get the API Key:**
   - Once logged in, navigate to the API section and select a plan that suits your needs. The basic plan should suffice for getting started.
   - After selecting your plan, you will be provided with an API key. This key is required for making requests to Helius's API.
   - BASIC PLAN IS FINE FOR PERSONAL USE!
## Step 2: Setting Up Your Environment

1. **Install Required Libraries:**
   - Ensure you have Python installed on your system.
   - Install the `requests` and `python-dotenv` libraries by running:
     ```bash
     pip install -r requirements.txt
     ```

2. **Create a `.env` File:**
   - In your project directory, create a file named `.env`. This file will store your API keys and other sensitive information, keeping them out of your main codebase.

3. **Add API Keys to `.env` File:**
   - Open the `.env` file in a text editor and add your API keys in the following format:
     ```
     CMC_API_KEY='your_cmc_api_key_here'
     HELIUS_RPC_URL='your_helius_rpc_url_here'
     ```
   - Replace `'your_cmc_api_key_here'` with the API key you obtained from CoinMarketCap.
   - Replace `'your_helius_rpc_url_here'` with the Helius RPC URL. If you're using a specific endpoint provided by Helius for fetching asset information, that URL goes here.

## Step 3: Running Your Application

1. **Load Environment Variables:**
   - The `load_dotenv()` function call in your script automatically loads the variables defined in your `.env` file for use in your Python application.

2. **Accessing Environment Variables in Python:**
   - Use `os.getenv("VARIABLE_NAME")` to access the environment variables in your code. For example:
     ```python
     cmc_api_key = os.getenv("CMC_API_KEY")
     helius_rpc_url = os.getenv("HELIUS_RPC_URL")
     ```
   - This method keeps your keys secure and your code clean.

3. **Execution:**
   - Run your Python script as usual. If everything is set up correctly, the script will use the API keys from your `.env` file to fetch and display the cryptocurrency data.

   ```bash
   python main.py
   ```

## Conclusion

The Dog Has a Hat and now a Clock


Forked with love by @Rxbbn