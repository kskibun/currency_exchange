from itertools import product
from typing import KeysView


class DataProcessing:

    @staticmethod
    def currencies_pair_preparation(components: KeysView[str]) -> list:
        return [f'{pair[0]}{pair[1]}=X'for pair in list(product(components, repeat=2)) if pair[0] != pair[1]]


