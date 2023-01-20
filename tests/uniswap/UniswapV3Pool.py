import pytest

from d3f1nance.uniswap.UniswapV3Pool import UniSwapV3PoolContract
from raffaelo.providers.http.provider import HTTPProvider


class TestUniSwapV3PoolContract:

    mock = '0x0000000000000000000000000000000000000000'
    address = '0xA374094527e1673A86dE625aa59517c5dE346d32'
    provider = HTTPProvider(uri='https://rpc.ankr.com/polygon')

    contract = UniSwapV3PoolContract(address=address, provider=provider)

    def testInstance(self):
        assert isinstance(self.contract, UniSwapV3PoolContract)

    def testAddress(self):
        assert self.contract.contract.address == self.address

    def testProvider(self):
        assert self.contract.provider == self.provider

    def test_factory(self):
        assert isinstance(self.contract.factory(), str)

    def test_fee(self):
        assert isinstance(self.contract.fee(), int)

    def test_feeGrowthGlobal0X128(self):
        assert isinstance(self.contract.feeGrowthGlobal0X128(), int)

    def test_feeGrowthGlobal1X128(self):
        assert isinstance(self.contract.feeGrowthGlobal1X128(), int)

    def test_liquidity(self):
        assert isinstance(self.contract.liquidity(), int)

    def test_maxLiquidityPerTick(self):
        assert isinstance(self.contract.maxLiquidityPerTick(), int)

    def test_observations(self):
        assert isinstance(self.contract.observations(i=0), list)

    def test_observe(self):
        assert isinstance(self.contract.observe(secondsAgos=[0]), list)

    def test_positions(self):
        assert isinstance(self.contract.positions(i=bytes('a'.encode())), list)

    def test_protocolFees(self):
        assert isinstance(self.contract.protocolFees(), list)

    def test_slot0(self):
        assert isinstance(self.contract.slot0(), list)

    def test_snapshotCumulativesInside(self):
        assert isinstance(self.contract.snapshotCumulativesInside(tickLower=-277990, tickUpper=-277590), list)

    def test_tickBitmap(self):
        assert isinstance(self.contract.tickBitmap(i=0), int)

    def test_tickSpacing(self):
        assert isinstance(self.contract.tickSpacing(), int)

    def test_ticks(self):
        assert isinstance(self.contract.ticks(i=0), list)

    def test_token0(self):
        assert isinstance(self.contract.token0(), str)

    def test_token1(self):
        assert isinstance(self.contract.token1(), str)
