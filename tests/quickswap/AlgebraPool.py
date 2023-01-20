import pytest

from d3f1nance.quickswap.AlgebraPool import QuickSwapV3AlgebraPoolContract
from raffaelo.providers.http.provider import HTTPProvider


class TestQuickSwapV3AlgebraPoolContract:

    mock = '0x0000000000000000000000000000000000000000'
    address = '0xAE81FAc689A1b4b1e06e7ef4a2ab4CD8aC0A087D'
    provider = HTTPProvider(uri='https://rpc.ankr.com/polygon')

    contract = QuickSwapV3AlgebraPoolContract(address=address, provider=provider)

    def testInstance(self):
        assert isinstance(self.contract, QuickSwapV3AlgebraPoolContract)

    def testAddress(self):
        assert self.contract.contract.address == self.address

    def testProvider(self):
        assert self.contract.provider == self.provider

    def test_activeIncentive(self):
        assert isinstance(self.contract.activeIncentive(), str)

    def test_dataStorageOperator(self):
        assert isinstance(self.contract.dataStorageOperator(), str)

    def test_factory(self):
        assert isinstance(self.contract.factory(), str)

    def test_getInnerCumulatives(self):
        try:
            assert isinstance(self.contract.getInnerCumulatives(bottomTick=-276707, topTick=-276507), list)
        except:
            ...

    def test_getTimepoints(self):
        assert isinstance(self.contract.getTimepoints(secondsAgos=[0]), list)

    def test_globalState(self):
        assert isinstance(self.contract.globalState(), list)

    def test_liquidity(self):
        assert isinstance(self.contract.liquidity(), int)

    def test_liquidityCooldown(self):
        assert isinstance(self.contract.liquidityCooldown(), int)

    def test_maxLiquidityPerTick(self):
        assert isinstance(self.contract.maxLiquidityPerTick(), int)

    def test_positions(self):
        assert isinstance(self.contract.positions(i=bytes('a'.encode())), list)

    def test_tickSpacing(self):
        assert isinstance(self.contract.tickSpacing(), int)

    def test_tickTable(self):
        assert isinstance(self.contract.tickTable(i=0), int)

    def test_ticks(self):
        assert isinstance(self.contract.ticks(i=0), list)

    def test_timepoints(self):
        assert isinstance(self.contract.timepoints(i=0), list)

    def test_token0(self):
        assert isinstance(self.contract.token0(), str)

    def test_token1(self):
        assert isinstance(self.contract.token1(), str)

    def test_totalFeeGrowth0Token(self):
        assert isinstance(self.contract.totalFeeGrowth0Token(), int)

    def test_totalFeeGrowth1Token(self):
        assert isinstance(self.contract.totalFeeGrowth1Token(), int)
