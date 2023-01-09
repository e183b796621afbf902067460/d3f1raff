import pytest

from d3f1raff.curve.Pool import CurvePoolContract
from raffaelo.providers.http.provider import HTTPProvider


class TestCurvePoolContract:

    address = '0xbEbc44782C7dB0a1A60Cb6fe97d0b483032FF1C7'
    provider = HTTPProvider(uri='https://rpc.ankr.com/eth')

    contract = CurvePoolContract(address=address, provider=provider)

    def testInstance(self):
        assert isinstance(self.contract, CurvePoolContract)

    def testAddress(self):
        assert self.contract.contract.address == self.address

    def testProvider(self):
        assert self.contract.provider == self.provider

    def test_A(self):
        assert isinstance(self.contract.A(), int)

    def test_get_virtual_price(self):
        assert isinstance(self.contract.get_virtual_price(), int)

    def test_calc_token_amount(self):
        assert isinstance(self.contract.calc_token_amount(amounts=[1, 2, 3], deposit=True), int)

    def test_get_dy(self):
        assert isinstance(self.contract.get_dy(i=0, j=1, dx=2), int)

    def test_get_dy_underlying(self):
        assert isinstance(self.contract.get_dy_underlying(i=0, j=1, dx=2), int)

    def test_calc_withdraw_one_coin(self):
        assert isinstance(self.contract.calc_withdraw_one_coin(_token_amount=1, i=0), int)

    def test_admin_balances(self):
        assert isinstance(self.contract.admin_balances(i=0), int)

    def test_coins(self):
        assert isinstance(self.contract.coins(arg0=0), str)

    def test_balances(self):
        assert isinstance(self.contract.balances(arg0=0), int)

    def test_fee(self):
        assert isinstance(self.contract.fee(), int)

    def test_admin_fee(self):
        assert isinstance(self.contract.admin_fee(), int)

    def test_owner(self):
        assert isinstance(self.contract.owner(), str)

    def test_initial_A(self):
        assert isinstance(self.contract.initial_A(), int)

    def test_future_A(self):
        assert isinstance(self.contract.future_A(), int)

    def test_initial_A_time(self):
        assert isinstance(self.contract.initial_A_time(), int)

    def test_future_A_time(self):
        assert isinstance(self.contract.future_A_time(), int)

    def test_admin_actions_deadline(self):
        assert isinstance(self.contract.admin_actions_deadline(), int)

    def test_transfer_ownership_deadline(self):
        assert isinstance(self.contract.transfer_ownership_deadline(), int)

    def test_future_fee(self):
        assert isinstance(self.contract.future_fee(), int)

    def test_future_admin_fee(self):
        assert isinstance(self.contract.future_admin_fee(), int)

    def test_future_owner(self):
        assert isinstance(self.contract.future_owner(), str)
