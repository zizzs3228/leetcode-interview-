from binance.client import Client
import pandas as pd
import numpy as np
import time
import threading
import schedule
import datetime

def get_price_data_binance(ticker:str,limit:int,interval = Client.KLINE_INTERVAL_1DAY)->pd.DataFrame:
        api = 'api'         #Вставьте свой апи-ключ
        secret = 'secret'   #Вставьте свой секрет-апи
        client = Client(api, secret)
        df = pd.DataFrame(client.futures_klines(symbol=ticker, limit=limit, interval=interval))
        df.columns=['date','open','high','low','close','volume','close_time','d1','d2','d3','d4','d5']
        df = df.drop(['close_time','d1','d2','d3','d4','d5'],axis=1)
        df['date'] = pd.to_datetime(df['date']*1000000)
        df['open'] = df['open'].astype(float)
        df['high'] = df['high'].astype(float)
        df['low'] = df['low'].astype(float)
        df['close'] = df['close'].astype(float)
        return df
    

def main():
    thread = threading.Thread(target=trading)
    thread.start()
    
    
def trading():
    BTCdf = get_price_data_binance('BTCUSDT',270,interval=Client.KLINE_INTERVAL_1MINUTE)
    ETHdf = get_price_data_binance('ETHUSDT',270,interval=Client.KLINE_INTERVAL_1MINUTE)
    correlationETH = np.corrcoef(BTCdf.loc[:,'close'], ETHdf.loc[:,'close'])[0][1]
    time = datetime.datetime.now()
    
    if ETHdf.iloc[0]['close']<ETHdf.iloc[-1]['close']:
        movementpercentage = (ETHdf.iloc[-1]['close'] - ETHdf.loc[:,'low'].min())/ETHdf.loc[:,'low'].min()*100
        print(f'Корреляция - {correlationETH}',f'Процент движения за час = {movementpercentage}%',
              f'Этот ответ был реализован в {time.strftime("%d-%m-%Y %H:%M:%S")}')
        
    if ETHdf.iloc[0]['close']>ETHdf.iloc[-1]['close']:
        movementpercentage = (ETHdf.loc[:,'high'].max() - ETHdf.iloc[-1]['close'])/ETHdf.loc[:,'high'].max()*100
        print(f'Корреляция - {correlationETH}',f'Процент движения за час = {-movementpercentage}%',
              f'Этот ответ был реализован в {time.strftime("%d-%m-%Y %H:%M:%S")}')
        
    if correlationETH<0.8 and abs(movementpercentage)>=1:
        print("Сигнализирую о том, что ETHUSDT сдвинулся на 1% за час и корреляция с биткоином минимальна")
    
    
if __name__ == '__main__':
    while True:
        current_time = time.gmtime()
        if current_time.tm_sec % 10 == 0:
            break
    main()       
    schedule.every(10).seconds.do(main)

    while True:
        schedule.run_pending()