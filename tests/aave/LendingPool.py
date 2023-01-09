import pytest

from d3f1raff.aave.LendingPool import AaveLendingPoolV2Contract
from raffaelo.providers.http.provider import HTTPProvider


class TestAaveLendingPoolV2Contract:

    mock = '0x0000000000000000000000000000000000000000'
    address = '0x7d2768dE32b0b80b7a3454c06BdAc94A69DDc7A9'
    provider = HTTPProvider(uri='https://rpc.ankr.com/eth')

    contract = AaveLendingPoolV2Contract(address=address, provider=provider)

    def testInstance(self):
        assert isinstance(self.contract, AaveLendingPoolV2Contract)

    def testAddress(self):
        assert self.contract.contract.address == self.address

    def testProvider(self):
        assert self.contract.provider == self.provider

    def test_FLASHLOAN_PREMIUM_TOTAL(self):
        assert isinstance(self.contract.FLASHLOAN_PREMIUM_TOTAL(), int)

    def test_LENDINGPOOL_REVISION(self):
        assert isinstance(self.contract.LENDINGPOOL_REVISION(), int)

    def test_MAX_NUMBER_RESERVES(self):
        assert isinstance(self.contract.MAX_NUMBER_RESERVES(), int)

    def test_MAX_STABLE_RATE_BORROW_SIZE_PERCENT(self):
        assert isinstance(self.contract.MAX_STABLE_RATE_BORROW_SIZE_PERCENT(), int)

    def test_getAddressesProvider(self):
        assert isinstance(self.contract.getAddressesProvider(), str)

    def test_getConfiguration(self):
        assert isinstance(self.contract.getConfiguration(asset=self.mock), tuple)

    def test_getReserveData(self):
        assert isinstance(self.contract.getReserveData(asset=self.mock), tuple)

    def test_getReserveNormalizedIncome(self):
        assert isinstance(self.contract.getReserveNormalizedIncome(asset=self.mock), int)

    def test_getReserveNormalizedVariableDebt(self):
        assert isinstance(self.contract.getReserveNormalizedVariableDebt(asset=self.mock), int)

    def test_getReservesList(self):
        assert isinstance(self.contract.getReservesList(), list)

    def test_getUserAccountData(self):
        assert isinstance(self.contract.getUserAccountData(address=self.mock), list)

    def test_getUserConfiguration(self):
        assert isinstance(self.contract.getUserConfiguration(address=self.mock), tuple)

    def test_paused(self):
        assert isinstance(self.contract.paused(), bool)
