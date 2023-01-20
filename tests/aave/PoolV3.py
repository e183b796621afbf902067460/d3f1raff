import pytest

from d3f1nance.aave.PoolV3 import AaveLendingPoolV3Contract
from raffaelo.providers.http.provider import HTTPProvider


class TestAaveLendingPoolV3Contract:

    mock = '0x0000000000000000000000000000000000000000'
    address = '0x794a61358D6845594F94dc1DB02A252b5b4814aD'
    provider = HTTPProvider(uri='https://rpc.ankr.com/polygon')

    contract = AaveLendingPoolV3Contract(address=address, provider=provider)

    def testInstance(self):
        assert isinstance(self.contract, AaveLendingPoolV3Contract)

    def testAddress(self):
        assert self.contract.contract.address == self.address

    def testProvider(self):
        assert self.contract.provider == self.provider

    def test_ADDRESSES_PROVIDER(self):
        assert isinstance(self.contract.ADDRESSES_PROVIDER(), str)

    def test_BRIDGE_PROTOCOL_FEE(self):
        assert isinstance(self.contract.BRIDGE_PROTOCOL_FEE(), int)

    def test_FLASHLOAN_PREMIUM_TOTAL(self):
        assert isinstance(self.contract.FLASHLOAN_PREMIUM_TOTAL(), int)

    def test_FLASHLOAN_PREMIUM_TO_PROTOCOL(self):
        assert isinstance(self.contract.FLASHLOAN_PREMIUM_TO_PROTOCOL(), int)

    def test_POOL_REVISION(self):
        assert isinstance(self.contract.POOL_REVISION(), int)

    def test_MAX_NUMBER_RESERVES(self):
        assert isinstance(self.contract.MAX_NUMBER_RESERVES(), int)

    def test_MAX_STABLE_RATE_BORROW_SIZE_PERCENT(self):
        assert isinstance(self.contract.MAX_STABLE_RATE_BORROW_SIZE_PERCENT(), int)

    def test_getConfiguration(self):
        assert isinstance(self.contract.getConfiguration(asset=self.mock), tuple)

    def test_getEModeCategoryData(self):
        assert isinstance(self.contract.getEModeCategoryData(id_=0), tuple)

    def test_getReserveAddressById(self):
        assert isinstance(self.contract.getReserveAddressById(id_=0), str)

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

    def test_getUserEmode(self):
        assert isinstance(self.contract.getUserEMode(address=self.mock), int)
