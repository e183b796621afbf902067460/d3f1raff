import py

from tests.erc20.ERC20Token import TestERC20TokenContract
from d3f1nance.convex.ConvexToken import ConvexTokenContract
from raffaelo.providers.http.provider import HTTPProvider


class TestConvexToken(TestERC20TokenContract):
    address = '0x4e3FBD56CD56c3e72c1403e103b45Db9da5B9D2B'
    provider = HTTPProvider(uri='https://rpc.ankr.com/eth')

    contract = ConvexTokenContract(address=address, provider=provider)

    def testInstance(self):
        assert isinstance(self.contract, ConvexTokenContract)

    def testAddress(self):
        assert self.contract.contract.address == self.address

    def testProvider(self):
        assert self.contract.provider == self.provider

    def test_maxSupply(self):
        assert isinstance(self.contract.maxSupply(), int)

    def test_operator(self):
        assert isinstance(self.contract.operator(), str)

    def test_reductionPerCliff(self):
        assert isinstance(self.contract.reductionPerCliff(), int)

    def test_totalCliffs(self):
        assert isinstance(self.contract.totalCliffs(), int)

    def test_vecrvProxy(self):
        assert isinstance(self.contract.vecrvProxy(), str)

