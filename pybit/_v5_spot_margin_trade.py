from ._http_manager import _V5HTTPManager
from .spot_margin_trade import SpotMarginTrade


class SpotMarginTradeHTTP(_V5HTTPManager):
    def spot_margin_trade_toggle_margin_trade(self, **kwargs):
        """Turn spot margin trade on / off.

        Required args:
            spotMarginMode (string): 1: on, 0: off

        Returns:
            Request results as dictionary.

        Additional information:
            https://bybit-exchange.github.io/docs/v5/spot-margin/switch-mode
        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{SpotMarginTrade.TOGGLE_MARGIN_TRADE}",
            query=kwargs,
            auth=True,
        )

    def spot_margin_trade_set_leverage(self, **kwargs):
        """Set the user's maximum leverage in spot cross margin

        Required args:
            leverage (string): Leverage. [2, 5].

        Returns:
            Request results as dictionary.

        Additional information:
            https://bybit-exchange.github.io/docs/v5/spot-margin/set-leverage
        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{SpotMarginTrade.SET_LEVERAGE}",
            query=kwargs,
            auth=True,
        )
