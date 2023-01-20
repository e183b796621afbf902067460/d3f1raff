import pytest

from d3f1nance.aave.IncentivesController import AaveIncentivesControllerV2Contract
from raffaelo.providers.http.provider import HTTPProvider


class TestAaveIncentivesControllerV2Contract:

    mock = '0x0000000000000000000000000000000000000000'
    address = '0xd784927Ff2f95ba542BfC824c8a8a98F3495f6b5'
    provider = HTTPProvider(uri='https://rpc.ankr.com/eth')

    contract = AaveIncentivesControllerV2Contract(address=address, provider=provider)

    def testInstance(self):
        assert isinstance(self.contract, AaveIncentivesControllerV2Contract)

    def testAddress(self):
        assert self.contract.contract.address == self.address

    def testProvider(self):
        assert self.contract.provider == self.provider

    def test_DISTRIBUTION_END(self):
        assert isinstance(self.contract.DISTRIBUTION_END(), int)

    def test_EMISSION_MANAGER(self):
        assert isinstance(self.contract.EMISSION_MANAGER(), str)

    def test_PRECISION(self):
        assert isinstance(self.contract.PRECISION(), int)

    def test_REVISION(self):
        assert isinstance(self.contract.REVISION(), int)

    def test_REWARD_TOKEN(self):
        assert isinstance(self.contract.REWARD_TOKEN(), str)

    def test_STAKE_TOKEN(self):
        assert isinstance(self.contract.STAKE_TOKEN(), str)

    def test_assets(self):
        assert isinstance(self.contract.assets(address=self.mock), list)

    def test_getAssetData(self):
        assert isinstance(self.contract.getAssetData(asset=self.mock), list)

    def test_getClaimer(self):
        assert isinstance(self.contract.getClaimer(address=self.mock), str)

    def test_getDistributionEnd(self):
        assert isinstance(self.contract.getDistributionEnd(), int)

    def test_getRewardsBalance(self):
        assets = ['0x9ff58f4fFB29fA2266Ab25e75e2A8b3503311656']
        assert isinstance(self.contract.getRewardsBalance(address=self.mock, assets=assets), int)

    def test_getUserAssetData(self):
        assert isinstance(self.contract.getUserAssetData(user=self.mock, asset=self.mock), int)

    def test_getUserUnclaimedRewards(self):
        assert isinstance(self.contract.getUserUnclaimedRewards(user=self.mock), int)
