import pytest

from d3f1raff.pancakeswap.MasterChefV2 import PancakeSwapMasterChefV2Contract
from raffaelo.providers.http.provider import HTTPProvider


class TestMasterChefV2Contract:

    mock = '0x0000000000000000000000000000000000000000'
    address = '0xa5f8C5Dbd5F286960b9d90548680aE5ebFf07652'
    provider = HTTPProvider(uri='https://rpc.ankr.com/bsc')

    contract = PancakeSwapMasterChefV2Contract(address=address, provider=provider)

    def testInstance(self):
        assert isinstance(self.contract, PancakeSwapMasterChefV2Contract)

    def testAddress(self):
        assert self.contract.contract.address == self.address

    def testProvider(self):
        assert self.contract.provider == self.provider

    def test_ACC_CAKE_PRECISION(self):
        assert isinstance(self.contract.ACC_CAKE_PRECISION(), int)

    def test_BOOST_PRECISION(self):
        assert isinstance(self.contract.BOOST_PRECISION(), int)

    def test_CAKE(self):
        assert isinstance(self.contract.CAKE(), str)

    def test_CAKE_RATE_TOTAL_PRECISION(self):
        assert isinstance(self.contract.CAKE_RATE_TOTAL_PRECISION(), int)

    def test_MASTERCHEF_CAKE_PER_BLOCK(self):
        assert isinstance(self.contract.MASTERCHEF_CAKE_PER_BLOCK(), int)

    def test_MASTER_CHEF(self):
        assert isinstance(self.contract.MASTER_CHEF(), str)

    def test_MASTER_PID(self):
        assert isinstance(self.contract.MASTER_PID(), int)

    def test_MAX_BOOST_PRECISION(self):
        assert isinstance(self.contract.MAX_BOOST_PRECISION(), int)

    def test_boostContract(self):
        assert isinstance(self.contract.boostContract(), str)

    def test_burnAdmin(self):
        assert isinstance(self.contract.burnAdmin(), str)

    def test_cakePerBlock(self):
        assert isinstance(self.contract.cakePerBlock(_isRegular=True), int)

    def test_cakePerBlockToBurn(self):
        assert isinstance(self.contract.cakePerBlockToBurn(), int)

    def test_cakeRateToBurn(self):
        assert isinstance(self.contract.cakeRateToBurn(), int)

    def test_cakeRateToRegularFarm(self):
        assert isinstance(self.contract.cakeRateToRegularFarm(), int)

    def test_cakeRateToSpecialFarm(self):
        assert isinstance(self.contract.cakeRateToSpecialFarm(), int)

    def test_getBoostMultiplier(self):
        assert isinstance(self.contract.getBoostMultiplier(_user=self.mock, _pid=0), int)

    def test_lastBurnedBlock(self):
        assert isinstance(self.contract.lastBurnedBlock(), int)

    def test_lpToken(self):
        assert isinstance(self.contract.lpToken(i=0), str)

    def test_owner(self):
        assert isinstance(self.contract.owner(), str)

    def test_pendingCake(self):
        assert isinstance(self.contract.pendingCake(_pid=0, _user=self.mock), int)

    def test_poolInfo(self):
        assert isinstance(self.contract.poolInfo(i=0), list)

    def test_poolLength(self):
        assert isinstance(self.contract.poolLength(), int)

    def test_totalRegularAllocPoint(self):
        assert isinstance(self.contract.totalRegularAllocPoint(), int)

    def test_totalSpecialAllocPoint(self):
        assert isinstance(self.contract.totalSpecialAllocPoint(), int)

    def test_userInfo(self):
        assert isinstance(self.contract.userInfo(pid=0, address=self.mock), list)

    def test_whiteList(self):
        assert isinstance(self.contract.whiteList(address=self.mock), bool)
