import pytest

from app.adapters.repositories.quickswap_v3.repository import QuickSwapV3WSSRepository
from app.services.quickswap_v3.service import QuickSwapV3WSSService
from app.settings import settings

try:
    from app.adapters.repositories.abstract import iRepository  # noqa: F401
    from app.services.abstract import iService  # noqa: F401

    raise ImportError
except ImportError:
    ...


@pytest.fixture(scope="package")
def wss_service() -> QuickSwapV3WSSService:  # noqa: D103
    return QuickSwapV3WSSService(address=settings.ADDRESS, is_reverse=False)


@pytest.fixture(scope="package")
def wss_repository(wss_service: QuickSwapV3WSSService) -> QuickSwapV3WSSRepository:  # noqa: D103
    return wss_service._repository
