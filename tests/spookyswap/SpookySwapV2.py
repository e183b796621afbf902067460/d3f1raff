import pytest

from d3f1nance.spookyswap.SpookySwapV2Pair import SpookySwapV2PairContract
from tests.uniswap.UniswapV2Pair import TestUniSwapV2PairContract
from raffaelo.providers.http.provider import HTTPProvider


class TestSpookySwapV2PairContract(TestUniSwapV2PairContract):

    mock = '0x0000000000000000000000000000000000000000'
    address = '0x2b4C76d0dc16BE1C31D4C1DC53bF9B45987Fc75c'
    provider = HTTPProvider(uri='https://rpc.ankr.com/fantom')

    contract = SpookySwapV2PairContract(address=address, provider=provider)

    def testInstance(self):
        assert isinstance(self.contract, SpookySwapV2PairContract)

    def testAddress(self):
        assert self.contract.contract.address == self.address

    def testProvider(self):
        assert self.contract.provider == self.provider
