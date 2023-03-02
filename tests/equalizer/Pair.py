import pytest

from d3f1nance.equalizer.Pair import EqualizerPairContract
from tests.velodrome.Pair import TestVelodromePairContract
from raffaelo.providers.http.provider import HTTPProvider


class TestEqualizerPairContract(TestVelodromePairContract):

    mock = '0x0000000000000000000000000000000000000000'
    address = '0x7547d05dFf1DA6B4A2eBB3f0833aFE3C62ABD9a1'
    provider = HTTPProvider(uri='https://rpc.ankr.com/fantom')

    contract = EqualizerPairContract(address=address, provider=provider)

    def testInstance(self):
        assert isinstance(self.contract, EqualizerPairContract)

    def testAddress(self):
        assert self.contract.contract.address == self.address

    def testProvider(self):
        assert self.contract.provider == self.provider

    def test_factory(self):
        assert isinstance(self.contract.factory(), str)

