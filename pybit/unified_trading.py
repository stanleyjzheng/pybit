from ._http_manager import _V5HTTPManager

BYBIT_API_VERSION = "/v5"


class HTTP(_V5HTTPManager):
    def get_kline(self, **kwargs):
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}/v5/market/kline",
            query=kwargs,
        )

    def get_mark_price_kline(self, **kwargs):
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}/v5/market/mark-price-kline",
            query=kwargs,
        )

    def get_index_price_kline(self, **kwargs):
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}/v5/market/index-price-kline",
            query=kwargs,
        )

    def get_tickers(self, **kwargs):
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}/v5/market/tickers",
            query=kwargs,
        )

    def get_wallet_balance(self, **kwargs):
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}/v5/account/wallet-balance",
            query=kwargs,
            auth=True,
        )

    def place_order(self, **kwargs):
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}/v5/order/create",
            query=kwargs,
            auth=True,
        )

    def place_batch_order(self, **kwargs):
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}/v5/order/create-batch",
            query=kwargs,
            auth=True,
        )

    def cancel_order(self, **kwargs):
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}/v5/order/cancel",
            query=kwargs,
            auth=True,
        )

    def cancel_batch_order(self, **kwargs):
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}/v5/order/cancel-batch",
            query=kwargs,
            auth=True,
        )

    def cancel_all_orders(self, **kwargs):
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}/v5/order/cancel-all",
            query=kwargs,
            auth=True,
        )

    def get_position_info(self, **kwargs):
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}/v5/position/list",
            query=kwargs,
            auth=True,
        )

    def set_trading_stop(self, **kwargs):
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}/v5/position/trading-stop",
            query=kwargs,
            auth=True,
        )

    def get_open_orders(self, **kwargs):
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}/v5/order/realtime",
            query=kwargs,
            auth=True,
        )

    def get_closed_pnl(self, **kwargs):
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}/v5/position/closed-pnl",
            query=kwargs,
            auth=True,
        )

    def get_asset_info(self, **kwargs):
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}/v5/asset/transfer/query-asset-info",
            query=kwargs,
            auth=True,
        )
