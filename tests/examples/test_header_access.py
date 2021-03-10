import pytest
from unittest.mock import MagicMock, PropertyMock, Mock, patch
from tartiflette_middleware.server import aiohttp
from tartiflette_middleware.examples.header_access import HeaderAccessMiddleware


class MockRequest(dict):
    headers = {'foo': 'bar'}


class TestHeaderAccessMiddleware:
    def test_header_access_example_init(self):
        HeaderAccessMiddleware()

    @pytest.mark.asyncio
    async def test_header_access_example_enter(self, monkeypatch):
        service = HeaderAccessMiddleware()
        service.request = MockRequest()
        async with service:
            pass
        assert await service() == 'bar'

    # todo: add a test that request data can't be copied forward
