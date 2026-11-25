class CoinConversor:
    COIN_LIST: dict[str, str];

    def __init__(self, list: dict[str, str]) -> None:
        self.COIN_LIST = list;

    def convert(self, qu: float, fr: str, to: str) -> float:
        if not self.COIN_LIST:
            raise ValueError("No currency rates are available.");

        if fr not in self.COIN_LIST:
            raise ValueError(f"Unknown source currency: {fr}");

        if to not in self.COIN_LIST:
            raise ValueError(f"Unknown target currency: {to}");

        amount_in_eur = qu / float(self.COIN_LIST[fr]);
        
        return amount_in_eur * float(self.COIN_LIST[to]);