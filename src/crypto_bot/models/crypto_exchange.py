from enum import Enum


class CryptoExchange(Enum):
    BINANCE = "Binance"
    KUCOIN = "Kucoin"
    HUOBI = "Huobi"
    BYBIT = "Bybit"


class CryptoExchangeWithURL:
    def __init__(self, exchange: CryptoExchange):
        match exchange:
            case CryptoExchange.BINANCE:
                self.exchange = CryptoExchange.BINANCE.value
                self.url = "https://binance.com"
            case CryptoExchange.KUCOIN:
                self.exchange = CryptoExchange.KUCOIN.value
                self.url = "https://kucoin.com"
            case CryptoExchange.HUOBI:
                self.exchange = CryptoExchange.HUOBI.value
                self.url = "https://huobi.com"
            case CryptoExchange.BYBIT:
                self.exchange = CryptoExchange.BYBIT.value
                self.url = "https://bybit.com"


class CryptoExchanges:
    binance = CryptoExchangeWithURL(CryptoExchange.BINANCE)
    kucoin = CryptoExchangeWithURL(CryptoExchange.KUCOIN)
    huobi = CryptoExchangeWithURL(CryptoExchange.HUOBI)
    bybit = CryptoExchangeWithURL(CryptoExchange.BYBIT)
