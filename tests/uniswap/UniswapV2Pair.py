import pytest

from d3f1nance.uniswap.UniswapV2Pair import UniSwapV2PairContract
from raffaelo.providers.http.provider import HTTPProvider


class TestUniSwapV2PairContract:

    mock = '0x0000000000000000000000000000000000000000'
    address = '0xB4e16d0168e52d35CaCD2c6185b44281Ec28C9Dc'
    provider = HTTPProvider(uri='https://rpc.ankr.com/eth')

    contract = UniSwapV2PairContract(address=address, provider=provider)

    def testInstance(self):
        assert isinstance(self.contract, UniSwapV2PairContract)

    def testAddress(self):
        assert self.contract.contract.address == self.address

    def testProvider(self):
        assert self.contract.provider == self.provider

    def test_DOMAIN_SEPARATOR(self):
        assert isinstance(self.contract.DOMAIN_SEPARATOR(), bytes)

    def test_MINIMUM_LIQUIDITY(self):
        assert isinstance(self.contract.MINIMUM_LIQUIDITY(), int)

    def test_PERMIT_TYPEHASH(self):
        assert isinstance(self.contract.PERMIT_TYPEHASH(), bytes)

    def test_allowance(self):
        assert isinstance(self.contract.allowance(arg0=self.mock, arg1=self.mock), int)

    def test_balanceOf(self):
        assert isinstance(self.contract.balanceOf(address=self.mock), int)

    def test_decimals(self):
        assert isinstance(self.contract.decimals(), int)

    def test_factory(self):
        assert isinstance(self.contract.factory(), str)

    def test_getReserves(self):
        assert isinstance(self.contract.getReserves(), list)

    def test_kLast(self):
        assert isinstance(self.contract.kLast(), int)

    def test_name(self):
        assert isinstance(self.contract.name(), str)

    def test_nonces(self):
        assert isinstance(self.contract.nonces(address=self.mock), int)

    def test_price0CumulativeLast(self):
        assert isinstance(self.contract.price0CumulativeLast(), int)

    def test_price1CumulativeLast(self):
        assert isinstance(self.contract.price1CumulativeLast(), int)

    def test_symbol(self):
        assert isinstance(self.contract.symbol(), str)

    def test_token0(self):
        assert isinstance(self.contract.token0(), str)

    def test_token1(self):
        assert isinstance(self.contract.token1(), str)

    def test_totalSupply(self):
        assert isinstance(self.contract.totalSupply(), int)
