import pytest

from d3f1nance.convex.VirtualBalanceRewardPool import ConvexVirtualBalanceRewardPoolContract
from raffaelo.providers.http.provider import HTTPProvider


class TestConvexVirtualBalanceRewardPoolContract:

    mock = '0x0000000000000000000000000000000000000000'
    address = '0x81fCe3E10D12Da6c7266a1A169c4C96813435263'
    provider = HTTPProvider(uri='https://rpc.ankr.com/eth')

    contract = ConvexVirtualBalanceRewardPoolContract(address=address, provider=provider)

    def testInstance(self):
        assert isinstance(self.contract, ConvexVirtualBalanceRewardPoolContract)

    def testAddress(self):
        assert self.contract.contract.address == self.address

    def testProvider(self):
        assert self.contract.provider == self.provider

    def test_balanceOf(self):
        assert isinstance(self.contract.balanceOf(address=self.mock), int)

    def test_currentRewards(self):
        assert isinstance(self.contract.currentRewards(), int)

    def test_deposits(self):
        assert isinstance(self.contract.deposits(), str)

    def test_duration(self):
        assert isinstance(self.contract.duration(), int)

    def test_earned(self):
        assert isinstance(self.contract.earned(address=self.mock), int)

    def test_historicalRewards(self):
        assert isinstance(self.contract.historicalRewards(), int)

    def test_lastTimeRewardApplicable(self):
        assert isinstance(self.contract.lastTimeRewardApplicable(), int)

    def test_lastUpdateTime(self):
        assert isinstance(self.contract.lastUpdateTime(), int)

    def test_newRewardRatio(self):
        assert isinstance(self.contract.newRewardRatio(), int)

    def test_operator(self):
        assert isinstance(self.contract.operator(), str)

    def test_periodFinish(self):
        assert isinstance(self.contract.periodFinish(), int)

    def test_queuedRewards(self):
        assert isinstance(self.contract.queuedRewards(), int)

    def test_rewardPerToken(self):
        assert isinstance(self.contract.rewardPerToken(), int)

    def test_rewardPerTokenStored(self):
        assert isinstance(self.contract.rewardPerTokenStored(), int)

    def test_rewardRate(self):
        assert isinstance(self.contract.rewardRate(), int)

    def test_rewardToken(self):
        assert isinstance(self.contract.rewardToken(), str)

    def test_rewards(self):
        assert isinstance(self.contract.rewards(address=self.mock), int)

    def test_totalSupply(self):
        assert isinstance(self.contract.totalSupply(), int)

    def test_userRewardPerTokenPaid(self):
        assert isinstance(self.contract.userRewardPerTokenPaid(address=self.mock), int)
