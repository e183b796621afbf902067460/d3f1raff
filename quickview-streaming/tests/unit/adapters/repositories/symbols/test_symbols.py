import pytest

from app.adapters.repositories.quickswap_v3.repository import QuickSwapV3WSSRepository

try:
    from app.adapters.repositories.abstract import iRepository  # noqa: F401

    raise ImportError
except ImportError:
    ...


@pytest.mark.repositories
def test__wss_repository__token0_symbol__must_be_str(wss_repository: QuickSwapV3WSSRepository):  # noqa: D103
    assert isinstance(wss_repository._token0_symbol, str)


@pytest.mark.repositories
def test__wss_repository__token1_symbol__must_be_str(wss_repository: QuickSwapV3WSSRepository):  # noqa: D103
    assert isinstance(wss_repository._token1_symbol, str)


@pytest.mark.repositories
def test__wss_repository__token0_symbol__must_be_equal_to_(wss_repository: QuickSwapV3WSSRepository):  # noqa: D103
    assert wss_repository._token0_symbol == "WMATIC"


@pytest.mark.repositories
def test__wss_repository__token1_symbol__must_be_equal_to_(wss_repository: QuickSwapV3WSSRepository):  # noqa: D103
    assert wss_repository._token1_symbol == "USDC"
