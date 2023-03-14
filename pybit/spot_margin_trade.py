from enum import Enum


class SpotMarginTrade(str, Enum):
    TOGGLE_MARGIN_TRADE = "/v5/spot-margin-trade/switch-mode"
    SET_LEVERAGE = "/v5/spot-margin-trade/set-leverage"

    def __str__(self) -> str:
        return self.value
