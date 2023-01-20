import pytest

from raffaelo.contracts.erc20.contract import ERC20TokenContract
from raffaelo.providers.http.provider import HTTPProvider


class TestERC20TokenContract:

    mock = '0x0000000000000000000000000000000000000000'
    address = '0x0d500B1d8E8eF31E21C99d1Db9A6444d3ADf1270'
    provider = HTTPProvider(uri='https://rpc.ankr.com/polygon')

    contract = ERC20TokenContract(address=address, provider=provider)

    def testInstance(self):
        assert isinstance(self.contract, ERC20TokenContract)

    def testAddress(self):
        assert self.contract.contract.address == self.address

    def testProvider(self):
        assert self.contract.provider == self.provider

    def test_name(self):
        assert isinstance(self.contract.name(), str)

    def test_totalSupply(self):
        assert isinstance(self.contract.totalSupply(), int)

    def test_decimals(self):
        assert isinstance(self.contract.decimals(), int)

    def test_balanceOf(self):
        assert isinstance(self.contract.balanceOf(address=self.mock), int)

    def test_symbol(self):
        assert isinstance(self.contract.symbol(), str)

    def test_allowance(self):
        assert isinstance(self.contract.allowance(owner=self.mock, spender=self.mock), int)
