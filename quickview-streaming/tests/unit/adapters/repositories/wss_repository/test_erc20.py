import pytest
from raffaelo.contracts.erc20.contract import ERC20TokenContract

from app.adapters.repositories.quickswap_v3.repository import QuickSwapV3WSSRepository

try:
    from app.adapters.repositories.abstract import iRepository  # noqa: F401

    raise ImportError
except ImportError:
    ...


@pytest.mark.repositories
def test__wss_repository__token0__must_be_erc20(wss_repository: QuickSwapV3WSSRepository):  # noqa: D103
    assert isinstance(wss_repository._token0, ERC20TokenContract)


@pytest.mark.repositories
def test__wss_repository__token1__must_be_erc20(wss_repository: QuickSwapV3WSSRepository):  # noqa: D103
    assert isinstance(wss_repository._token1, ERC20TokenContract)
