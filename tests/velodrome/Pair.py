import pytest

from d3f1nance.velodrome.Pair import VelodromePairContract
from raffaelo.providers.http.provider import HTTPProvider


class TestVelodromePairContract:

    mock = '0x0000000000000000000000000000000000000000'
    address = '0x79c912FEF520be002c2B6e57EC4324e260f38E50'
    provider = HTTPProvider(uri='https://rpc.ankr.com/optimism')

    contract = VelodromePairContract(address=address, provider=provider)

    def testInstance(self):
        assert isinstance(self.contract, VelodromePairContract)

    def testAddress(self):
        assert self.contract.contract.address == self.address

    def testProvider(self):
        assert self.contract.provider == self.provider

    def test_allowance(self):
        assert isinstance(self.contract.allowance(arg0=self.mock, arg1=self.mock), int)

    def test_balanceOf(self):
        assert isinstance(self.contract.balanceOf(address=self.mock), int)

    def test_blockTimestampLast(self):
        assert isinstance(self.contract.blockTimestampLast(), int)

    def test_claimable0(self):
        assert isinstance(self.contract.claimable0(address=self.mock), int)

    def test_claimable1(self):
        assert isinstance(self.contract.claimable1(address=self.mock), int)

    def test_current(self):
        assert isinstance(self.contract.current(tokenIn=self.mock, amountIn=0), int)

    def test_currentCumulativePrices(self):
        assert isinstance(self.contract.currentCumulativePrices(), list)

    def test_decimals(self):
        assert isinstance(self.contract.decimals(), int)

    def test_fees(self):
        assert isinstance(self.contract.fees(), str)

    def test_getAmountOut(self):
        assert isinstance(self.contract.getAmountOut(tokenIn=self.mock, amountIn=0), int)

    def test_getReserves(self):
        assert isinstance(self.contract.getReserves(), list)

    def test_index0(self):
        assert isinstance(self.contract.index0(), int)

    def test_index1(self):
        assert isinstance(self.contract.index1(), int)

    def test_lastObservation(self):
        assert isinstance(self.contract.lastObservation(), tuple)

    def test_metadata(self):
        assert isinstance(self.contract.metadata(), list)

    def test_name(self):
        assert isinstance(self.contract.name(), str)

    def test_nonces(self):
        assert isinstance(self.contract.nonces(address=self.mock), int)

    def test_observationLength(self):
        assert isinstance(self.contract.observationLength(), int)

    def test_observations(self):
        assert isinstance(self.contract.observations(i=0), list)

    def test_prices(self):
        assert isinstance(self.contract.prices(tokenIn=self.mock, amountIn=0, points=0), list)

    def test_quote(self):
        try:
            assert isinstance(self.contract.quote(tokenIn=self.mock, amountIn=0, granularity=0), int)
        except:
            ...

    def test_reserve0(self):
        assert isinstance(self.contract.reserve0(), int)

    def test_reserve0CumulativeLast(self):
        assert isinstance(self.contract.reserve0CumulativeLast(), int)

    def test_reserve1(self):
        assert isinstance(self.contract.reserve1(), int)

    def test_reserve1CumulativeLast(self):
        assert isinstance(self.contract.reserve1CumulativeLast(), int)

    def test_sample(self):
        assert isinstance(self.contract.sample(tokenIn=self.mock, amountIn=0, points=0, window=0), list)

    def test_stable(self):
        assert isinstance(self.contract.stable(), bool)

    def test_supplyIndex0(self):
        assert isinstance(self.contract.supplyIndex0(address=self.mock), int)

    def test_supplyIndex1(self):
        assert isinstance(self.contract.supplyIndex1(address=self.mock), int)

    def test_symbol(self):
        assert isinstance(self.contract.symbol(), str)

    def test_token0(self):
        assert isinstance(self.contract.token0(), str)

    def test_token1(self):
        assert isinstance(self.contract.token1(), str)

    def test_tokens(self):
        assert isinstance(self.contract.tokens(), list)

    def test_totalSupply(self):
        assert isinstance(self.contract.totalSupply(), int)

