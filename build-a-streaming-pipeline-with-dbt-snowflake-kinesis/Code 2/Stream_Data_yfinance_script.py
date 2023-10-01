import boto3
import yfinance as yf
import json
import time

def put_data_to_firehose(delivery_stream_name, data):
    firehose_client = boto3.client('firehose')
    data_str = json.dumps(data) + '\n'
    response = firehose_client.put_record(
        DeliveryStreamName=delivery_stream_name,
        Record={
            'Data': data_str
        }
    )
    return response

def fetch_stock_data(symbol):
    data = yf.download(symbol, period="1d", interval="1m")
    if not data.empty:
        return {
            'symbol': symbol,
            'timestamp': int(time.time()),
            'open': data.iloc[-1]['Open'],
            'high': data.iloc[-1]['High'],
            'low': data.iloc[-1]['Low'],
            'close': data.iloc[-1]['Close'],
            'volume': data.iloc[-1]['Volume']
        }
    return None

def main():
    delivery_stream_name = 'stock-market-data'  # Replace with your Kinesis Data Firehose Delivery Stream name
    symbols = ['AAPL', 'MSFT', 'GOOGL','NFLX','AMZN','META','ADBE','ABNB','NVDA']  # Add more stock symbols as needed
	#These are for the stocks Apple, Microsoft, Google, Netflix, Amazon, Meta, Adobe and Airbnb and Nvidia
    interval_seconds = 60  # Fetch data every 60 seconds

    while True:
        for symbol in symbols:
            data = fetch_stock_data(symbol)
            if data:
                response = put_data_to_firehose(delivery_stream_name, data)
                print(f"Data sent to Kinesis Firehose for {symbol}. RecordId: {response['RecordId']}")
        time.sleep(interval_seconds)

if __name__ == '__main__':
    main()
