import yfinance as yf
#import pandas as pd
import boto3
from botocore.exceptions import NoCredentialsError

# Define the list of stock symbols
stock_symbols = ['AAPL', 'MSFT', 'GOOGL', 'NFLX', 'AMZN', 'META', 'ADBE', 'ABNB', 'NVDA']

# Fetch stock data using yfinance
def fetch_stock_data(symbols, start_date, end_date):
    df = yf.download(stock_symbols, group_by='Ticker', period='2y')
    data = df.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)
    return data

# Upload data to S3
def upload_to_s3(data, bucket_name, s3_path):
    s3 = boto3.client('s3')

    try:
        # Convert the data to CSV format
        csv_data = data.to_csv(index=True).encode('utf-8')
        
        # Upload the data to S3
        s3.put_object(Bucket=bucket_name, Key=s3_path, Body=csv_data)
        print(f'Data uploaded to s3://{bucket_name}/{s3_path}')
    except NoCredentialsError:
        print("Credentials not available")

def main():
    # Specify the start and end dates for fetching data
    start_date = '2021-08-07'
    end_date = '2023-08-07'

    # Fetch stock data
    stock_data = fetch_stock_data(stock_symbols, start_date, end_date)

    # Select desired columns
    selected_columns = ['Ticker','Open', 'High', 'Low', 'Close', 'Volume']
    stock_data = stock_data[selected_columns]

    # Specify your S3 bucket name and path
    bucket_name = 'stock-market-streaming-data-dbt-snowflake'
    s3_path = 'batch/batch_stock_data.csv'

    # Upload data to S3
    upload_to_s3(stock_data, bucket_name, s3_path)

if __name__ == "__main__":
    main()
