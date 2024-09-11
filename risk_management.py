
# risk_management.py

import pandas as pd  # Add this import

class RiskManagement:
    def __init__(self, atr_period=14, atr_multiplier=1.5, risk_ratio=1.5):
        self.atr_period = atr_period
        self.atr_multiplier = atr_multiplier
        self.risk_ratio = risk_ratio

    def calculate_atr(self, df):
        high = df['high'].astype(float)
        low = df['low'].astype(float)
        close = df['close'].astype(float)
        df['previous_close'] = close.shift(1)
        df['tr'] = pd.concat([high - low, (high - df['previous_close']).abs(), (low - df['previous_close']).abs()], axis=1).max(axis=1)
        atr = df['tr'].rolling(window=self.atr_period).mean().iloc[-1]
        return atr

    def calculate_scalping_risk_management(self, current_price, trend):
        stop_loss_distance = current_price * 0.005  # 0.5% stop loss
        take_profit_distance = current_price * 0.01  # 1% take profit

        if trend == 'long':
            stop_loss = current_price - stop_loss_distance
            take_profit = current_price + take_profit_distance
        elif trend == 'short':
            stop_loss = current_price + stop_loss_distance
            take_profit = current_price - take_profit_distance
        else:
            raise ValueError("Trend must be either 'long' or 'short'")

        return stop_loss, take_profit

