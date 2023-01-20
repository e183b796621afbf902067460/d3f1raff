import pytest

from d3f1nance.pancakeswap.PancakePair import PancakePairContract
from raffaelo.providers.http.provider import HTTPProvider

from tests.uniswap.UniswapV2Pair import TestUniSwapV2PairContract


class TestPancakePairContract(TestUniSwapV2PairContract):

    mock = '0x0000000000000000000000000000000000000000'
    address = '0x0eD7e52944161450477ee417DE9Cd3a859b14fD0'
    provider = HTTPProvider(uri='https://rpc.ankr.com/bsc')

    contract = PancakePairContract(address=address, provider=provider)

    def testInstance(self):
        assert isinstance(self.contract, PancakePairContract)
