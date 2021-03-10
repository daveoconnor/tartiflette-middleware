import pytest
from tartiflette_middleware.server import aiohttp
from unittest.mock import MagicMock


class ExampleRequestContextHooks:
    async def __aenter__(self):
        """fake enter"""

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """fake exit"""

    async def __call__(self, *args, **kwargs):
        """fake call"""


# take this from test_header_access
async def handler(request):
    h = MagicMock()
    h.request = request
    return h


# take this from test_header_access
class mock_middleware:
    def __init__(self, func):
        self.func = func

    @pytest.mark.asyncio
    async def __call__(self, *args, **kwargs):
        kwargs['request'] = MagicMock()
        kwargs['handler'] = handler
        return await self.func(*args, **kwargs)


class TestAiohttp:
    @pytest.mark.asyncio
    async def test_request_context_factory(self, monkeypatch):
        monkeypatch.setattr(
            aiohttp,
            'middleware',
            mock_middleware
        )
        service = ExampleRequestContextHooks()
        mw_enter_fail = aiohttp.get_hooks_service_middleware(
            context_service=service
        )
        await mw_enter_fail()
        assert isinstance(service.request, MagicMock)
        assert service.handler is handler
