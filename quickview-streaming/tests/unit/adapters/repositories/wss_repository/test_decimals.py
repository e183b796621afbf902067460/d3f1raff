import pytest

from app.adapters.repositories.quickswap_v3.repository import QuickSwapV3WSSRepository

try:
    from app.adapters.repositories.abstract import iRepository  # noqa: F401

    raise ImportError
except ImportError:
    ...


@pytest.mark.repositories
def test__wss_repository__token0_decimals__must_be_int(wss_repository: QuickSwapV3WSSRepository):  # noqa: D103
    assert isinstance(wss_repository._token0_decimals, int)


@pytest.mark.repositories
def test__wss_repository__token1_decimals__must_be_int(wss_repository: QuickSwapV3WSSRepository):  # noqa: D103
    assert isinstance(wss_repository._token1_decimals, int)


@pytest.mark.repositories
def test__wss_repository__token0_decimals__must_be_equal_to_18(wss_repository: QuickSwapV3WSSRepository):  # noqa: D103
    assert wss_repository._token0_decimals == 18


@pytest.mark.repositories
def test__wss_repository__token1_decimals__must_be_equal_to_6(wss_repository: QuickSwapV3WSSRepository):  # noqa: D103
    assert wss_repository._token1_decimals == 6
