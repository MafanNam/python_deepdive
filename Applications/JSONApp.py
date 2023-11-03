class Stock:
    def __init__(self, symbol, date, open_, high, low, close, volume):
        self.symbol = symbol
        self.date = date
        self.open = open_
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def __repr__(self):
        return f"Trade(symbol={self.symbol}, date={self.date})"

    def JSON_format(self):
        return vars(self)


class Trade:
    def __init__(self, symbol, timestamp, order, price, volume, commission):
        self.symbol = symbol
        self.timestamp = timestamp
        self.order = order
        self.price = price
        self.commission = commission
        self.volume = volume

    def __repr__(self):
        return f"Trade(symbol={self.symbol}, timestamp={self.timestamp})"

    def JSON_format(self):
        return vars(self)


from datetime import date, datetime
from decimal import Decimal

activity = {
    "quotes": [
        Stock('TSLA', date(2018, 11, 22),
              Decimal('338.19'), Decimal('338.64'), Decimal('337.60'), Decimal('338.19'), 365_607),
        Stock('AAPL', date(2018, 11, 22),
              Decimal('176.66'), Decimal('177.25'), Decimal('176.64'), Decimal('176.78'), 3_699_184),
        Stock('MSFT', date(2018, 11, 22),
              Decimal('103.25'), Decimal('103.48'), Decimal('103.07'), Decimal('103.11'), 4_493_689)
    ],

    "trades": [
        Trade('TSLA', datetime(2018, 11, 22, 10, 5, 12), 'buy', Decimal('338.25'), 100, Decimal('9.99')),
        Trade('AAPL', datetime(2018, 11, 22, 10, 30, 5), 'sell', Decimal('177.01'), 20, Decimal('9.99'))
    ]
}

import json


class JSONEncoderMy(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Stock) or isinstance(o, Trade):
            result = o.JSON_format()
            result['object'] = o.__class__.__name__
            return result
        elif isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        elif isinstance(o, datetime):
            return o.strftime('%Y-%m-%dT%H:%M:%S')
        elif isinstance(o, Decimal):
            return str(o)
        else:
            super().default(o)


encoded = json.dumps(activity, cls=JSONEncoderMy, indent=2)


# ---------------- Goal 2 ------------------

def decode_stock(d):
    s = Stock(d['symbol'],
              datetime.strptime(d['date'], '%Y-%m-%d').date(),
              Decimal(d['open']),
              Decimal(d['high']),
              Decimal(d['low']),
              Decimal(d['close']),
              int(d['volume']),
              )
    return s


def decode_trade(d):
    s = Trade(d['symbol'],
              datetime.strptime(d['timestamp'], '%Y-%m-%d').date(),
              d['order'],
              Decimal(d['price']),
              int(d['volume']),
              Decimal(d['commission']),
              )
    return s


def decode_financials(d):
    object_type = d.get('object', None)
    if object_type == 'Stock':
        return decode_stock(d)
    elif object_type == 'Trade':
        return decode_trade(d)
    return d


d_stock = {
    "symbol": "TSLA",
    "date": "2018-11-22",
    "open": "338.19",
    "high": "338.64",
    "low": "337.60",
    "close": "338.19",
    "volume": 365607,
    "object": "Stock"
}

d_trade = {
    "symbol": "AAPL",
    "timestamp": "2018-11-22",
    "order": "sell",
    "price": "177.01",
    "commission": "9.99",
    "volume": 20,
    "object": "Trade"
}

# print(decode_stock(d_stock))
# print(decode_trade(d_trade))
# print(decode_financials(d_stock))


from json import JSONDecoder, loads


class CustomDecoder(JSONDecoder):
    def decode(self, s, _w=...):
        data = loads(s)
        return self.parse_financials(data)

    def parse_financials(self, obj):
        if isinstance(obj, dict):
            obj = decode_financials(obj)
            if isinstance(obj, dict):
                for key, value in obj.items():
                    obj[key] = self.parse_financials(value)
        elif isinstance(obj, list):
            for index, item in enumerate(obj):
                obj[index] = self.parse_financials(item)
        return obj


decoded = loads(encoded, cls=CustomDecoder)
print(decoded)
