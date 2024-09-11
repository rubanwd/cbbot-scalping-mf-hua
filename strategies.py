# strategy.py

import pandas as pd
from indicators import Indicators

class Strategies:
    def __init__(self):
        self.indicators = Indicators()

    def prepare_dataframe(self, historical_data):
        df = pd.DataFrame(historical_data)
        df.columns = ["timestamp", "open", "high", "low", "close", "volume", "turnover"]
        df['close'] = df['close'].astype(float)
        df.sort_values('timestamp', inplace=True)
        return df

    def scalping_strategy(self, df):
        current_price = df['close'].iloc[-1]
        bollinger_upper = df['Bollinger_upper'].iloc[-1]
        bollinger_lower = df['Bollinger_lower'].iloc[-1]

        support = bollinger_lower
        resistance = bollinger_upper

        # Place a long trade at support and a short trade at resistance
        if current_price <= support:
            return 'long', support, resistance
        elif current_price >= resistance:
            return 'short', support, resistance
        return None, support, resistance

